"""Simulace k přednášce o akustickém tomografu.

Skript vygeneruje všechny obrázky použité v přednášce (soubory obr_*.png
ve stejné složce) a vypíše čísla, která jsou v textu citována.

Spuštění:   python simulace.py

Potřebuje jen numpy a matplotlib. Všechny výpočty jsou obyčejné maticové
operace: součin matic, transponování a řešení soustavy lineárních rovnic.
Matematicky skript odpovídá metodám SIRT a FBP z knihovny tomotree.
"""

import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

SLOZKA = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.size": 9, "figure.dpi": 110, "savefig.bbox": "tight"})

V_ZDRAVE = 1500.0   # rychlost zvuku ve zdravém dřevě [m/s]
V_DUTINA = 500.0    # rychlost v poškozeném dřevě [m/s]
POLOMER = 0.30      # poloměr kmene [m]
CMAP = "RdYlGn"
VMIN, VMAX = 400.0, 1600.0


# ----------------------------------------------------------------------
# Fantomy: funkce, které bodu (x, y) přiřadí rychlost zvuku
# ----------------------------------------------------------------------

def kruhy(*seznam):
    """Fantom s kruhovými vadami; každá vada je (x0, y0, polomer, rychlost)."""
    def v(x, y):
        out = np.full(np.shape(x), V_ZDRAVE)
        for x0, y0, r, rychlost in seznam:
            out = np.where(np.hypot(x - x0, y - y0) < r, rychlost, out)
        return out
    return v


def prstenec(x, y):
    """Hniloba ve tvaru mezikruží."""
    r = np.hypot(x, y)
    return np.where((r > 0.10) & (r < 0.17), 800.0, V_ZDRAVE)


DUTINA = kruhy((0.05, 0.03, 0.09, V_DUTINA))
FANTOMY = {
    "středová dutina": kruhy((0, 0, 0.10, V_DUTINA)),
    "dutina mimo střed": kruhy((0.12, 0.05, 0.08, V_DUTINA)),
    "dvě dutiny": kruhy((-0.12, 0.05, 0.07, V_DUTINA), (0.12, -0.08, 0.06, V_DUTINA)),
    "prstenec hniloby": prstenec,
}
BODOVA_VADA = kruhy((0.08, 0.05, 0.03, V_DUTINA))


# ----------------------------------------------------------------------
# Úloha: čidla, paprsky, síť a matice soustavy
# ----------------------------------------------------------------------

def uvnitr_mnohouhelniku(body, vrcholy):
    """Které body leží uvnitř mnohoúhelníku (počítáme průsečíky polopřímky s hranami)."""
    x, y = body.T
    uvnitr = np.zeros(len(body), dtype=bool)
    for (x1, y1), (x2, y2) in zip(vrcholy, np.roll(vrcholy, -1, axis=0)):
        if y1 != y2:
            protina = ((y1 > y) != (y2 > y)) & (x < x1 + (y - y1) * (x2 - x1) / (y2 - y1))
            uvnitr ^= protina
    return uvnitr


class Uloha:
    """Geometrie tomografu a matice soustavy A x = b."""

    def __init__(self, pocet_cidel=12, n=42, cidla=None):
        if cidla is None:                            # čidla rovnoměrně na kružnici, č. 1 nahoře
            uhly = np.pi / 2 + 2 * np.pi * np.arange(pocet_cidel) / pocet_cidel
            self.cidla = POLOMER * np.column_stack([np.cos(uhly), np.sin(uhly)])
            self.H = 1.05 * POLOMER                  # polovina strany čtvercové sítě
        else:                                        # změřené polohy čidel na stromě
            cidla = np.asarray(cidla, dtype=float)
            self.cidla = cidla - (cidla.max(axis=0) + cidla.min(axis=0)) / 2
            self.H = 1.05 * np.abs(self.cidla).max()
            pocet_cidel = len(cidla)
        self.pary = [(i, j) for i in range(pocet_cidel) for j in range(i + 1, pocet_cidel)]
        self.n = n
        self.hrany = np.linspace(-self.H, self.H, n + 1)
        self.h = self.hrany[1] - self.hrany[0]       # velikost buňky
        s = (self.hrany[:-1] + self.hrany[1:]) / 2
        X, Y = np.meshgrid(s, s, indexing="ij")
        self.stredy_vse = np.column_stack([X.ravel(), Y.ravel()])
        self.L = np.array([np.linalg.norm(self.cidla[j] - self.cidla[i]) for i, j in self.pary])

        A_vse = self._matice_tenkych_paprsku()
        # neznámé: buňky uvnitř kmene a buňky, kterými prochází nějaký paprsek
        if cidla is None:
            uvnitr = np.hypot(*self.stredy_vse.T) <= POLOMER
        else:
            uvnitr = uvnitr_mnohouhelniku(self.stredy_vse, self.cidla)
        self.maska = uvnitr | (A_vse.sum(axis=0) > 0)
        self.stredy = self.stredy_vse[self.maska]
        self.A = A_vse[:, self.maska]                # tenké paprsky
        self.Af = self._matice_tlustych_paprsku()    # tlusté paprsky
        self.D = self._laplace()
        self.m, self.pocet_bunek = self.A.shape

    def _matice_tenkych_paprsku(self):
        """a_ij = délka paprsku i v buňce j."""
        n, hrany = self.n, self.hrany
        A = np.zeros((len(self.pary), n * n))
        for r, (i, j) in enumerate(self.pary):
            a, u = self.cidla[i], self.cidla[j] - self.cidla[i]
            t = [0.0, 1.0]                           # parametry průsečíků s čarami sítě
            for k in (0, 1):
                if abs(u[k]) > 1e-12:
                    tk = (hrany - a[k]) / u[k]
                    t.extend(tk[(tk > 0) & (tk < 1)])
            t = np.unique(t)
            delky = np.diff(t) * np.linalg.norm(u)
            stred = a + np.outer((t[:-1] + t[1:]) / 2, u)   # středy úseků
            ix = np.clip(np.searchsorted(hrany, stred[:, 0]) - 1, 0, n - 1)
            iy = np.clip(np.searchsorted(hrany, stred[:, 1]) - 1, 0, n - 1)
            np.add.at(A[r], ix * n + iy, delky)
        return A

    def _matice_tlustych_paprsku(self, pomer=0.12):
        """Paprsek „vidí“ i buňky ve svém okolí, váha klesá se vzdáleností."""
        sirka = pomer * self.L.max()
        A = np.zeros((len(self.pary), len(self.stredy)))
        for r, (i, j) in enumerate(self.pary):
            a, u = self.cidla[i], self.cidla[j] - self.cidla[i]
            s = np.clip((self.stredy - a) @ u / (u @ u), 0, 1)
            d = np.linalg.norm(self.stredy - (a + np.outer(s, u)), axis=1)
            w = np.where(d < 2.5 * sirka, np.exp(-(d / sirka) ** 2), 0.0)
            A[r] = self.L[r] * w / w.sum()           # součet řádku je délka paprsku
        return A

    def _laplace(self):
        """Matice D: (D x)_j = (počet sousedů) * x_j - součet sousedů."""
        n = self.n
        cislo = -np.ones(n * n, dtype=int)
        cislo[self.maska] = np.arange(self.maska.sum())
        D = np.zeros((self.maska.sum(),) * 2)
        for c in np.flatnonzero(self.maska):
            ix, iy = divmod(c, n)
            for jx, jy in ((ix - 1, iy), (ix + 1, iy), (ix, iy - 1), (ix, iy + 1)):
                if 0 <= jx < n and 0 <= jy < n and cislo[jx * n + jy] >= 0:
                    D[cislo[c], cislo[c]] += 1
                    D[cislo[c], cislo[jx * n + jy]] -= 1
        return D

    def pomalost(self, fantom):
        """Fantom převedený na síť: pomalost ve středech buněk."""
        return 1.0 / fantom(self.stredy[:, 0], self.stredy[:, 1])

    def casy(self, fantom, sum_=0.0, seed=1):
        """„Měření“: časy průchodu spočítané jemnou numerickou integrací."""
        t = (np.arange(4000) + 0.5) / 4000
        b = np.empty(len(self.pary))
        for r, (i, j) in enumerate(self.pary):
            body = self.cidla[i] + np.outer(t, self.cidla[j] - self.cidla[i])
            b[r] = self.L[r] * np.mean(1.0 / fantom(body[:, 0], body[:, 1]))
        if sum_ > 0:
            b = b * (1 + sum_ * np.random.default_rng(seed).standard_normal(len(b)))
        return b

    def meze(self, b):
        """Fyzikálně přípustné pomalosti: (1/v_max, 1/v_min)."""
        v = self.L / b
        return 1 / v.max(), 1 / max(340.0, 0.5 * v.min())


# ----------------------------------------------------------------------
# Rekonstrukční metody
# ----------------------------------------------------------------------

def zpetna_projekce(A, b, L):
    """Buňka dostane vážený průměr pomalostí paprsků, které jí procházejí."""
    soucet = A.sum(axis=0)
    x = np.full(A.shape[1], np.nan)
    x[soucet > 0] = (A.T @ (b / L))[soucet > 0] / soucet[soucet > 0]
    return x


def sirt(A, b, L, iterace=1000, omega=1.5, alpha=0.0, D=None, h=1.0, meze=None,
         x_prave=None, ulozit=()):
    """Metoda SIRT: x <- x + omega * C A^T R (b - A x).

    Pro alpha > 0 se k soustavě přidají rovnice alpha*h*D x = 0 (vyhlazení).
    Vrací řešení a slovník s historií (reziduum, chyba, uložené iterace).
    """
    if alpha > 0:
        M = np.vstack([A, alpha * h * D])
        p = np.concatenate([b, np.zeros(D.shape[0])])
    else:
        M, p = A, b
    radky = np.abs(M).sum(axis=1)
    sloupce = np.abs(M).sum(axis=0)
    R = np.where(radky > 0, 1 / np.where(radky > 0, radky, 1), 0)
    C = np.where(sloupce > 0, 1 / np.where(sloupce > 0, sloupce, 1), 0)
    x = np.full(M.shape[1], b.sum() / L.sum())       # homogenní počáteční odhad
    hist = {"rez": [], "chyba": [], "snimky": {}}
    for k in range(1, iterace + 1):
        x = x + omega * C * (M.T @ (R * (p - M @ x)))
        if meze is not None:
            x = np.clip(x, *meze)
        hist["rez"].append(np.linalg.norm(A @ x - b) / np.linalg.norm(b))
        if x_prave is not None:
            hist["chyba"].append(np.linalg.norm(x - x_prave) / np.linalg.norm(x_prave))
        if k in ulozit:
            hist["snimky"][k] = x.copy()
    return x, hist


def fbp(A, b, x0, tlumeni=1.0, vrat_y=False):
    """Filtrovaná zpětná projekce: x = x0 + A^T (A A^T + mu I)^(-1) (b - A x0)."""
    G = A @ A.T
    mu = tlumeni * np.trace(G) / len(b)
    y = np.linalg.solve(G + mu * np.eye(len(b)), b - A @ x0)
    x = x0 + A.T @ y
    return (x, y) if vrat_y else x


def chyba(x, x_prave):
    """Relativní chyba pomalosti v procentech."""
    return 100 * np.linalg.norm(x - x_prave) / np.linalg.norm(x_prave)


# ----------------------------------------------------------------------
# Kreslení
# ----------------------------------------------------------------------

def obraz(ax, u, x, titulek=None, rychlost=True, cidla=True, **kw):
    """Vykreslí hodnoty v buňkách (standardně jako rychlost 1/x)."""
    pole = np.full(u.n * u.n, np.nan)
    if rychlost:
        pole[u.maska] = 1 / np.clip(x, 1 / 5000, 1 / 100)
        kw = {"cmap": CMAP, "vmin": VMIN, "vmax": VMAX, **kw}
    else:
        pole[u.maska] = x
    im = ax.imshow(pole.reshape(u.n, u.n).T, origin="lower",
                   extent=[-u.H, u.H, -u.H, u.H], interpolation="nearest", **kw)
    if cidla:
        ax.plot(u.cidla[:, 0], u.cidla[:, 1], "ko", ms=2.5)
    ax.set_aspect("equal")
    ax.axis("off")
    if titulek:
        ax.set_title(titulek, fontsize=9)
    return im


def paprsky(ax, u, barvy=None, vyber=None, **kw):
    vyber = range(len(u.pary)) if vyber is None else vyber
    usecky = [[u.cidla[u.pary[r][0]], u.cidla[u.pary[r][1]]] for r in vyber]
    lc = LineCollection(usecky, **kw)
    if barvy is not None:
        lc.set_array(np.asarray(barvy))
    ax.add_collection(lc)
    return lc


def skala(fig, im, axs, popis="rychlost [m/s]"):
    fig.colorbar(im, ax=axs, shrink=0.8, label=popis, pad=0.02)


def uloz(fig, jmeno):
    fig.savefig(os.path.join(SLOZKA, jmeno))
    plt.close(fig)
    print("  uloženo", jmeno)


# ----------------------------------------------------------------------
# Jednotlivé obrázky
# ----------------------------------------------------------------------

def obr_geometrie(u):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    for ax in axs:
        paprsky(ax, u, colors="tab:blue", lw=0.6)
        ax.plot(u.cidla[:, 0], u.cidla[:, 1], "ko", ms=5)
        ax.add_patch(plt.Circle((0, 0), POLOMER, fill=False, color="saddlebrown", lw=1.5))
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_xlim(-0.34, 0.34); ax.set_ylim(-0.34, 0.34)
    for k, p in enumerate(u.cidla):
        axs[0].annotate(str(k + 1), 1.09 * p, ha="center", va="center")
    axs[0].set_title(f"{len(u.cidla)} čidel, {u.m} paprsků")
    obraz(axs[1], u, np.ones(u.pocet_bunek), rychlost=False, cidla=False,
          cmap="Greys", vmin=0, vmax=6)
    for hr in u.hrany:
        axs[1].plot([hr, hr], [-u.H, u.H], color="gray", lw=0.2)
        axs[1].plot([-u.H, u.H], [hr, hr], color="gray", lw=0.2)
    axs[1].set_title(f"síť {u.n}×{u.n}, {u.pocet_bunek} neznámých buněk")
    uloz(fig, "obr_geometrie.png")


def obr_paprsek(u):
    i, j = 0, 4
    r = u.pary.index((i, j))
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    radek = np.where(u.A[r] > 0, 100 * u.A[r], np.nan)
    im = obraz(ax, u, radek, rychlost=False, cidla=False, cmap="viridis")
    paprsky(ax, u, vyber=[r], colors="red", lw=1.2)
    for hr in u.hrany:
        ax.plot([hr, hr], [-u.H, u.H], color="gray", lw=0.2)
        ax.plot([-u.H, u.H], [hr, hr], color="gray", lw=0.2)
    for k in (i, j):                                 # jen obě koncová čidla paprsku
        ax.plot(*u.cidla[k], "ko", ms=4)
        ax.annotate(f"čidlo {k + 1}", u.cidla[k], xytext=(6, 0), textcoords="offset points",
                    va="center")
    konce = u.cidla[[i, j]]
    ax.set_xlim(konce[:, 0].min() - 0.03, konce[:, 0].max() + 0.09)
    ax.set_ylim(konce[:, 1].min() - 0.03, konce[:, 1].max() + 0.03)
    skala(fig, im, ax, "délka paprsku v buňce [cm]")
    uloz(fig, "obr_paprsek.png")
    print(f"  paprsek {i + 1}-{j + 1}: délka {u.L[r]:.4f} m, součet řádku {u.A[r].sum():.4f} m, "
          f"nenulových prvků {np.count_nonzero(u.A[r])}")


def obr_matice(u):
    fig, ax = plt.subplots(figsize=(8, 2.6))
    ax.imshow(u.A > 0, aspect="auto", cmap="Greys", interpolation="nearest")
    ax.set_xlabel("číslo buňky $j$"); ax.set_ylabel("číslo paprsku $i$")
    uloz(fig, "obr_matice.png")
    print(f"  A: {u.A.shape}, nenulových prvků {100 * np.mean(u.A > 0):.1f} %")


def obr_pokryti(u):
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.6))
    for ax, A, t in zip(axs, (u.A, u.Af), ("tenké paprsky", "tlusté paprsky")):
        s = 100 * A.sum(axis=0)
        im = obraz(ax, u, np.where(s > 0, s, np.nan), t, rychlost=False, cmap="magma_r", vmin=0)
        skala(fig, im, ax, "součet sloupce [cm]")
    uloz(fig, "obr_pokryti.png")
    print(f"  buněk bez paprsku (tenké): {np.sum(u.A.sum(axis=0) == 0)} z {u.pocet_bunek}")


def obr_fantom(u, b):
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.7))
    obraz(axs[0], u, u.pomalost(DUTINA), "fantom: skutečná rychlost")
    axs[1].plot(u.cidla[:, 0], u.cidla[:, 1], "ko", ms=3)
    lc = paprsky(axs[1], u, barvy=u.L / b, cmap=CMAP, lw=1.6)
    lc.set_clim(VMIN, VMAX)
    axs[1].set_aspect("equal"); axs[1].axis("off")
    axs[1].set_xlim(-u.H, u.H); axs[1].set_ylim(-u.H, u.H)
    axs[1].set_title("zdánlivá rychlost paprsků $L_i/b_i$")
    skala(fig, lc, axs)
    uloz(fig, "obr_fantom.png")
    v = u.L / b
    print(f"  časy {1e6 * b.min():.0f}–{1e6 * b.max():.0f} µs, "
          f"zdánlivé rychlosti {v.min():.0f}–{v.max():.0f} m/s")
    print(f"  kontrola A x - b (tenké, přesná pomalost): "
          f"{100 * np.linalg.norm(u.A @ u.pomalost(DUTINA) - b) / np.linalg.norm(b):.2f} %")


def obr_nejednoznacnost(u, b, b_sum):
    """Několik různých obrazů, které dávají přesně stejné časy."""
    s0 = b.sum() / u.L.sum()
    x, y = u.stredy.T
    starty = [np.full(u.pocet_bunek, s0),
              s0 * (1 + 0.4 * np.sign(np.sin(40 * x) * np.sin(40 * y))),
              s0 * (1 + 0.4 * np.sin(25 * y))]
    reseni = [x0 + u.A.T @ np.linalg.solve(u.A @ u.A.T, b - u.A @ x0) for x0 in starty]
    reseni.append(starty[0] + u.A.T @ np.linalg.solve(u.A @ u.A.T, b_sum - u.A @ starty[0]))
    fig, axs = plt.subplots(1, 4, figsize=(11, 3.1))
    for k, (ax, xr) in enumerate(zip(axs, reseni)):
        cil = b if k < 3 else b_sum
        rez = np.linalg.norm(u.A @ xr - cil) / np.linalg.norm(cil)
        t = f"řešení {k + 1}" if k < 3 else "data se šumem 2 %"
        im = obraz(ax, u, xr, f"{t}\nneshoda s časy {rez:.0e}")
    skala(fig, im, axs)
    uloz(fig, "obr_nejednoznacnost.png")
    print(f"  hodnost A (tenké) = {np.linalg.matrix_rank(u.A)}, "
          f"A (tlusté) = {np.linalg.matrix_rank(u.Af)}; m = {u.m}, n = {u.pocet_bunek}")


def obr_zpetna_projekce(u, b):
    od_cidla_1 = [r for r, p in enumerate(u.pary) if p[0] == 0]
    r1 = u.pary.index((0, 6))
    varianty = [("1 paprsek", u.A[[r1]], b[[r1]], u.L[[r1]]),
                ("11 paprsků z čidla 1", u.A[od_cidla_1], b[od_cidla_1], u.L[od_cidla_1]),
                ("všech 66, tenké paprsky", u.A, b, u.L),
                ("všech 66, tlusté paprsky", u.Af, b, u.L)]
    fig, axs = plt.subplots(1, 4, figsize=(11, 3))
    for ax, (t, A, bb, L) in zip(axs, varianty):
        im = obraz(ax, u, zpetna_projekce(A, bb, L), t)
    skala(fig, im, axs)
    uloz(fig, "obr_zpetna_projekce.png")


def obr_bodova_vada(u):
    b = u.casy(BODOVA_VADA)
    fig, axs = plt.subplots(1, 3, figsize=(9, 3.1))
    obraz(axs[0], u, u.pomalost(BODOVA_VADA), "fantom: malá vada")
    kw = dict(vmin=1300, vmax=1500)
    obraz(axs[1], u, zpetna_projekce(u.A, b, u.L), "zpětná projekce\ntenké paprsky", **kw)
    im = obraz(axs[2], u, zpetna_projekce(u.Af, b, u.L), "zpětná projekce\ntlusté paprsky", **kw)
    skala(fig, im, axs[1:])
    uloz(fig, "obr_bodova_vada.png")


def obr_kaczmarz():
    """Dvě rovnice o dvou neznámých: Kaczmarzova metoda a současná oprava."""
    A = np.array([[1.0, 2.0], [3.0, 1.0]])
    b = np.array([8.0, 9.0])
    presne = np.linalg.solve(A, b)
    x = np.array([0.5, 0.5])
    kacz = [x.copy()]
    for k in range(8):
        i = k % 2
        x = x + (b[i] - A[i] @ x) / (A[i] @ A[i]) * A[i]
        kacz.append(x.copy())
    R, C = 1 / A.sum(axis=1), 1 / A.sum(axis=0)
    x = np.array([0.5, 0.5])
    sou = [x.copy()]
    for k in range(30):
        x = x + C * (A.T @ (R * (b - A @ x)))
        sou.append(x.copy())
    kacz, sou = np.array(kacz), np.array(sou)
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.8))
    t = np.linspace(0, 5, 2)
    for ax, cesta, tit in zip(axs, (kacz, sou),
                              ("postupně po rovnicích (Kaczmarz)", "všechny rovnice současně (SIRT)")):
        ax.plot(t, (8 - t) / 2, "tab:blue", label="$x_1+2x_2=8$")
        ax.plot(t, 9 - 3 * t, "tab:green", label="$3x_1+x_2=9$")
        ax.plot(cesta[:, 0], cesta[:, 1], "o-", color="tab:red", ms=3, lw=1)
        ax.plot(*presne, "k*", ms=10)
        ax.set_xlim(0, 4); ax.set_ylim(0, 5); ax.set_aspect("equal")
        ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$"); ax.set_title(tit); ax.legend()
    uloz(fig, "obr_kaczmarz.png")
    print(f"  Kaczmarz po 8 krocích {kacz[-1].round(4)}, SIRT po 30 krocích "
          f"{sou[-1].round(4)}, přesně {presne}")


def obr_sirt_iterace(u, b, b_sum):
    xp = u.pomalost(DUTINA)
    N = 3000
    _, ht = sirt(u.A, b, u.L, iterace=N, x_prave=xp, ulozit=(1, 5, 1000))
    _, hf = sirt(u.Af, b, u.L, iterace=N, x_prave=xp, ulozit=(1, 10, 100, 1000))
    _, hs = sirt(u.Af, b_sum, u.L, iterace=N, x_prave=xp)
    fig, axs = plt.subplots(2, 4, figsize=(11, 5.8))
    obraz(axs[0, 0], u, xp, "fantom")
    for ax, k in zip(axs[0, 1:], (1, 5, 1000)):
        obraz(ax, u, ht["snimky"][k], f"tenké, {k}. iterace\n"
              f"neshoda {100 * ht['rez'][k - 1]:.2f} %, chyba {100 * ht['chyba'][k - 1]:.0f} %")
    for ax, k in zip(axs[1], (1, 10, 100, 1000)):
        im = obraz(ax, u, hf["snimky"][k], f"tlusté, {k}. iterace\n"
                   f"neshoda {100 * hf['rez'][k - 1]:.1f} %, chyba {100 * hf['chyba'][k - 1]:.0f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_sirt_iterace.png")

    fig, axs = plt.subplots(1, 2, figsize=(9, 3.4))
    it = np.arange(1, N + 1)
    for h, t in ((ht, "tenké paprsky"), (hf, "tlusté paprsky"), (hs, "tlusté paprsky, šum 2 %")):
        axs[0].loglog(it, 100 * np.array(h["rez"]), label=t)
        axs[1].semilogx(it, 100 * np.array(h["chyba"]), label=t)
        ch = 100 * np.array(h["chyba"])
        print(f"  SIRT {t}: nejmenší chyba {ch.min():.1f} % v iteraci {ch.argmin() + 1}; " +
              ", ".join(f"{k}: neshoda {100 * h['rez'][k - 1]:.3f} % chyba {ch[k - 1]:.1f} %"
                        for k in (1, 5, 10, 100, 1000, 3000)))
    axs[0].set_ylim(1e-3, 50)
    axs[0].set_ylabel("neshoda s naměřenými časy [%]")
    axs[1].set_ylabel("chyba vůči fantomu [%]")
    for ax in axs:
        ax.set_xlabel("iterace"); ax.legend(); ax.grid(alpha=0.3)
    uloz(fig, "obr_sirt_konvergence.png")


def obr_omega(u, b):
    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    for om in (0.5, 1.0, 1.5, 1.9, 2.5):
        _, hist = sirt(u.A, b, u.L, iterace=60, omega=om)
        ax.semilogy(np.arange(1, 61), 100 * np.array(hist["rez"]), label=f"$\\omega={om}$")
        print(f"  omega {om}: neshoda po 10/60 iteracích {100 * hist['rez'][9]:.3g} / "
              f"{100 * hist['rez'][-1]:.3g} %")
    ax.set_ylim(1e-8, 1e4)
    ax.set_xlabel("iterace"); ax.set_ylabel("neshoda s časy [%]"); ax.legend(); ax.grid(alpha=0.3)
    uloz(fig, "obr_omega.png")


def obr_stabilizace(u, b_sum):
    """Chyba obrazu během iterací pro čtyři varianty metody (tlusté paprsky, šum)."""
    xp = u.pomalost(DUTINA)
    N = 3000
    fig, ax = plt.subplots(figsize=(5.8, 3.6))
    for al, mz, t in ((0, None, "bez úprav"), (0, u.meze(b_sum), "ořez"),
                      (10, None, "vyhlazení"), (10, u.meze(b_sum), "ořez i vyhlazení")):
        _, h = sirt(u.Af, b_sum, u.L, iterace=N, alpha=al, D=u.D, h=u.h, meze=mz, x_prave=xp)
        ch = 100 * np.array(h["chyba"])
        ax.semilogx(np.arange(1, N + 1), ch, label=t)
        print(f"  {t}: nejmenší chyba {ch.min():.1f} % v iteraci {ch.argmin() + 1}, "
              f"na konci {ch[-1]:.1f} %, neshoda {100 * h['rez'][-1]:.1f} %")
    ax.set_ylim(0, 100)
    ax.set_xlabel("iterace"); ax.set_ylabel("chyba vůči fantomu [%]"); ax.legend(); ax.grid(alpha=0.3)
    uloz(fig, "obr_stabilizace.png")


def obr_vyhlazeni(u, b_sum):
    xp = u.pomalost(DUTINA)
    alfy = (0, 1, 10, 50)
    fig, axs = plt.subplots(2, 4, figsize=(11, 5.6))
    for radek, (A, jm) in enumerate(((u.A, "tenké"), (u.Af, "tlusté"))):
        for ax, al in zip(axs[radek], alfy):
            x, _ = sirt(A, b_sum, u.L, iterace=1000, alpha=al, D=u.D, h=u.h, meze=u.meze(b_sum))
            im = obraz(ax, u, x, f"{jm} paprsky, $\\alpha={al}$\nchyba {chyba(x, xp):.1f} %")
            print(f"  {jm}, alpha {al}: chyba {chyba(x, xp):.1f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_vyhlazeni.png")


def obr_orez(u, b_sum):
    xp = u.pomalost(DUTINA)
    kw = dict(iterace=1000, alpha=10, D=u.D, h=u.h)
    x1, _ = sirt(u.Af, b_sum, u.L, **kw)
    x2, _ = sirt(u.Af, b_sum, u.L, meze=u.meze(b_sum), **kw)
    fig, axs = plt.subplots(1, 3, figsize=(11, 3.1), layout="constrained",
                            gridspec_kw={"width_ratios": [1, 1, 1.5]})
    obraz(axs[0], u, x1, f"bez ořezu, chyba {chyba(x1, xp):.1f} %")
    im = obraz(axs[1], u, x2, f"s ořezem, chyba {chyba(x2, xp):.1f} %")
    # řez obrazem: řada buněk nejblíže přímce y = 0,03 m
    yr = u.stredy[np.argmin(np.abs(u.stredy[:, 1] - 0.03)), 1]
    rada = np.isclose(u.stredy[:, 1], yr)
    xs = 100 * u.stredy[rada, 0]
    axs[2].plot(xs, 1 / xp[rada], "k--", label="fantom")
    axs[2].plot(xs, 1 / x1[rada], label="bez ořezu")
    axs[2].plot(xs, 1 / x2[rada], label="s ořezem")
    vmax, vmin = 1 / np.array(u.meze(b_sum))
    axs[2].axhline(vmax, color="gray", lw=0.6); axs[2].axhline(vmin, color="gray", lw=0.6)
    axs[2].set_xlabel("x [cm]"); axs[2].set_ylabel("rychlost [m/s]")
    axs[2].set_title("řez obrazem"); axs[2].legend(); axs[2].grid(alpha=0.3)
    fig.colorbar(im, ax=axs[:2], location="left", shrink=0.8, label="rychlost [m/s]")
    uloz(fig, "obr_orez.png")
    print(f"  meze rychlosti: {vmin:.0f}–{vmax:.0f} m/s; bez ořezu rychlosti "
          f"{(1 / x1).min():.0f}–{(1 / x1).max():.0f}")


def obr_aat(u, b):
    fig, axs = plt.subplots(1, 3, figsize=(11, 3.3), gridspec_kw={"width_ratios": [1, 1, 1.6]})
    for ax, A, t in zip(axs, (u.A, u.Af), ("tenké paprsky", "tlusté paprsky")):
        G = A @ A.T
        ax.imshow(G / G.max(), cmap="viridis")
        ax.set_title(f"$AA^T$, {t}"); ax.set_xlabel("paprsek"); ax.set_ylabel("paprsek")
        print(f"  {t}: číslo podmíněnosti AA^T = {np.linalg.cond(G):.3g}")
    s0 = b.sum() / u.L.sum()
    x, y = fbp(u.Af, b, np.full(u.pocet_bunek, s0), vrat_y=True)
    r = b - u.Af @ np.full(u.pocet_bunek, s0)
    i = np.arange(u.m)
    axs[2].bar(i - 0.2, r / np.abs(r).max(), 0.4, label="reziduum $\\vec r$")
    axs[2].bar(i + 0.2, y / np.abs(y).max(), 0.4, label="po filtraci $\\vec y$")
    axs[2].set_xlabel("paprsek"); axs[2].set_title("data před filtrací a po ní (normováno)")
    axs[2].legend()
    uloz(fig, "obr_aat.png")


def obr_fbp_kroky(u, b):
    s0 = b.sum() / u.L.sum()
    x0 = np.full(u.pocet_bunek, s0)
    r = b - u.Af @ x0
    x, y = fbp(u.Af, b, x0, vrat_y=True)
    fig, axs = plt.subplots(1, 4, figsize=(12, 3.1))
    axs[0].plot(u.cidla[:, 0], u.cidla[:, 1], "ko", ms=3)
    lc = paprsky(axs[0], u, barvy=1e6 * r, cmap="coolwarm", lw=1.6)
    m = 1e6 * np.abs(r).max(); lc.set_clim(-m, m)
    axs[0].set_aspect("equal"); axs[0].axis("off")
    axs[0].set_xlim(-u.H, u.H); axs[0].set_ylim(-u.H, u.H)
    axs[0].set_title("1. reziduum $\\vec r$ [µs]")
    fig.colorbar(lc, ax=axs[0], shrink=0.7, pad=0.02)
    bez = x0 + u.Af.T @ r / (u.Af.sum(axis=0) * u.L.mean())
    obraz(axs[1], u, bez, "zpětná projekce $\\vec r$ bez filtru")
    obraz(axs[2], u, x, "2.+3. filtr a zpětná projekce")
    im = obraz(axs[3], u, u.pomalost(DUTINA), "fantom")
    skala(fig, im, axs[1:])
    uloz(fig, "obr_fbp_kroky.png")
    print(f"  s0 = {1e6 * s0:.1f} µs/m, tj. {1 / s0:.0f} m/s; FBP neshoda "
          f"{100 * np.linalg.norm(u.Af @ x - b) / np.linalg.norm(b):.2f} %, "
          f"chyba {chyba(x, u.pomalost(DUTINA)):.1f} %")


def obr_tlumeni(u, b_sum):
    xp = u.pomalost(DUTINA)
    x0 = np.full(u.pocet_bunek, b_sum.sum() / u.L.sum())
    hodnoty = (1e-4, 1e-2, 0.1, 1, 10, 100)
    fig, axs = plt.subplots(2, 3, figsize=(9, 6))
    for ax, la in zip(axs.ravel(), hodnoty):
        x = fbp(u.Af, b_sum, x0, la)
        rez = 100 * np.linalg.norm(u.Af @ x - b_sum) / np.linalg.norm(b_sum)
        im = obraz(ax, u, x, f"tlumení {la:g}\nneshoda {rez:.1f} %, chyba {chyba(x, xp):.1f} %")
        print(f"  tlumení {la:g}: neshoda {rez:.2f} %, chyba {chyba(x, xp):.1f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_tlumeni.png")


def obr_odezva(u):
    b = u.casy(BODOVA_VADA)
    xp = u.pomalost(BODOVA_VADA)
    x0 = np.full(u.pocet_bunek, b.sum() / u.L.sum())
    xs, _ = sirt(u.Af, b, u.L, alpha=10, D=u.D, h=u.h, meze=u.meze(b))
    obrazy = [("fantom", xp), ("zpětná projekce", zpetna_projekce(u.Af, b, u.L)),
              ("SIRT", xs), ("FBP", fbp(u.Af, b, x0))]
    fig, axs = plt.subplots(1, 4, figsize=(11, 3))
    for ax, (t, x) in zip(axs, obrazy):
        im = obraz(ax, u, x, f"{t}\nnejnižší rychlost {1 / x.max():.0f} m/s", vmin=1100, vmax=1550)
    skala(fig, im, axs)
    uloz(fig, "obr_odezva.png")


def obr_srovnani(u):
    fig, axs = plt.subplots(4, 4, figsize=(10, 10))
    for radek, (jmeno, fantom) in zip(axs, FANTOMY.items()):
        b = u.casy(fantom, sum_=0.02)
        xp = u.pomalost(fantom)
        x0 = np.full(u.pocet_bunek, b.sum() / u.L.sum())
        xs, _ = sirt(u.Af, b, u.L, alpha=10, D=u.D, h=u.h, meze=u.meze(b))
        xf = np.clip(fbp(u.Af, b, x0), *u.meze(b))
        xb = zpetna_projekce(u.Af, b, u.L)
        obraz(radek[0], u, xp, f"fantom\n{jmeno}")
        obraz(radek[1], u, xb, f"zpětná projekce\nchyba {chyba(xb, xp):.0f} %")
        obraz(radek[2], u, xs, f"SIRT\nchyba {chyba(xs, xp):.0f} %")
        im = obraz(radek[3], u, xf, f"FBP\nchyba {chyba(xf, xp):.0f} %")
        print(f"  {jmeno}: BP {chyba(xb, xp):.1f} %, SIRT {chyba(xs, xp):.1f} %, "
              f"FBP {chyba(xf, xp):.1f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_srovnani.png")


def obr_pocet_cidel():
    pocty = (8, 12, 16, 24)
    fig, axs = plt.subplots(2, 4, figsize=(11, 5.6))
    for k, N in enumerate(pocty):
        u = Uloha(N)
        b = u.casy(DUTINA, sum_=0.02)
        xp = u.pomalost(DUTINA)
        x0 = np.full(u.pocet_bunek, b.sum() / u.L.sum())
        xs, _ = sirt(u.Af, b, u.L, alpha=10, D=u.D, h=u.h, meze=u.meze(b))
        xf = np.clip(fbp(u.Af, b, x0), *u.meze(b))
        obraz(axs[0, k], u, xs, f"SIRT, {N} čidel ({u.m} paprsků)\nchyba {chyba(xs, xp):.1f} %")
        im = obraz(axs[1, k], u, xf, f"FBP, {N} čidel\nchyba {chyba(xf, xp):.1f} %")
        print(f"  {N} čidel, {u.m} paprsků: SIRT {chyba(xs, xp):.1f} %, FBP {chyba(xf, xp):.1f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_pocet_cidel.png")


# ----------------------------------------------------------------------
# Skutečné stromy: měření z lipové aleje v Jičíně (data z knihovny tomotree)
# ----------------------------------------------------------------------

def nacti_strom(cislo):
    """Načte polohy čidel [m] a tabulku časů [s]; vrátí úlohu a vektor časů b."""
    cidla = np.loadtxt(os.path.join(SLOZKA, "data", f"nodes-{cislo}.csv"), delimiter=",")
    T = np.loadtxt(os.path.join(SLOZKA, "data", f"times-{cislo}.csv"), delimiter=",")
    u = Uloha(cidla=cidla)
    # každý paprsek byl změřen v obou směrech, bereme průměr
    b = np.array([(T[i, j] + T[j, i]) / 2 for i, j in u.pary])
    return u, b


def rekonstrukce_stromu(u, b):
    x0 = np.full(u.pocet_bunek, b.sum() / u.L.sum())
    xs, _ = sirt(u.Af, b, u.L, iterace=2000, alpha=10, D=u.D, h=u.h, meze=u.meze(b))
    xf = np.clip(fbp(u.Af, b, x0), *u.meze(b))
    return zpetna_projekce(u.Af, b, u.L), xs, xf


def kresli_paprsky(ax, u, b, titulek):
    ax.plot(u.cidla[:, 0], u.cidla[:, 1], "ko", ms=3)
    lc = paprsky(ax, u, barvy=u.L / b, cmap=CMAP, lw=1.6)
    lc.set_clim(VMIN, VMAX)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-u.H, u.H); ax.set_ylim(-u.H, u.H)
    ax.set_title(titulek, fontsize=9)


FOTO_OKRAJ = 1.25   # fotografie pokrývá čtverec o čtvrtinu větší než síť


def stejne_meritko(axs, u):
    """Všechny panely ve stejném výřezu jako fotografie."""
    for ax in np.ravel(axs):
        ax.set_xlim(-FOTO_OKRAJ * u.H, FOTO_OKRAJ * u.H)
        ax.set_ylim(-FOTO_OKRAJ * u.H, FOTO_OKRAJ * u.H)


def kresli_foto(ax, u, cislo, titulek):
    """Fotografie řezu; je otočena a oříznuta na čtverec o FOTO_OKRAJ větší, než je síť."""
    K = FOTO_OKRAJ * u.H
    ax.imshow(plt.imread(os.path.join(SLOZKA, f"foto_strom_{cislo}.jpg")), extent=[-K, K, -K, K])
    ax.plot(u.cidla[:, 0], u.cidla[:, 1], "o", color="red", ms=2.5)
    ax.annotate("1", u.cidla[0], xytext=(0, 4), textcoords="offset points",
                ha="center", color="red", fontsize=8)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title(titulek, fontsize=9)


def obr_stromy():
    stromy = {c: nacti_strom(c) for c in ("14", "08")}
    vysledky = {c: rekonstrukce_stromu(u, b) for c, (u, b) in stromy.items()}

    # úvodní obrázek: fotografie řezu a tomogram
    fig, axs = plt.subplots(1, 4, figsize=(11, 3.1))
    for k, c in enumerate(stromy):
        u, b = stromy[c]
        kresli_foto(axs[2 * k], u, c, f"strom {int(c)}: řez kmenem")
        im = obraz(axs[2 * k + 1], u, vysledky[c][1], f"strom {int(c)}: tomogram")
        stejne_meritko(axs[2 * k:2 * k + 2], u)
    skala(fig, im, axs)
    uloz(fig, "obr_stromy_uvod.png")

    # závěrečný obrázek: všechny kroky na skutečných datech
    fig, axs = plt.subplots(2, 5, figsize=(13, 5.6))
    for radek, c in zip(axs, stromy):
        u, b = stromy[c]
        xb, xs, xf = vysledky[c]
        kresli_foto(radek[0], u, c, f"strom {int(c)}: řez kmenem")
        kresli_paprsky(radek[1], u, b, "zdánlivá rychlost paprsků")
        obraz(radek[2], u, xb, "zpětná projekce")
        obraz(radek[3], u, xs, "SIRT")
        im = obraz(radek[4], u, xf, "FBP")
        stejne_meritko(radek, u)
        v = u.L / b
        nesh = lambda x: 100 * np.linalg.norm(u.Af @ x - b) / np.linalg.norm(b)
        print(f"  strom {c}: {u.m} paprsků, {u.pocet_bunek} buněk, obvod "
              f"{np.linalg.norm(u.cidla - np.roll(u.cidla, -1, axis=0), axis=1).sum():.2f} m, "
              f"časy {1e6 * b.min():.0f}–{1e6 * b.max():.0f} µs, zdánlivé rychlosti "
              f"{v.min():.0f}–{v.max():.0f} m/s, s0 -> {u.L.sum() / b.sum():.0f} m/s")
        print(f"    neshoda s daty: BP {nesh(xb):.1f} %, SIRT {nesh(xs):.1f} %, FBP {nesh(xf):.1f} %; "
              f"nejnižší rychlost SIRT {1 / xs.max():.0f}, FBP {1 / xf.max():.0f} m/s; "
              f"podíl plochy pod 1000 m/s: SIRT {100 * np.mean(1 / xs < 1000):.0f} %, "
              f"FBP {100 * np.mean(1 / xf < 1000):.0f} %")
    skala(fig, im, axs)
    uloz(fig, "obr_stromy.png")


def kontrola_identity(u, b):
    """Numerické ověření: A^T (A A^T + mu I)^-1 = (A^T A + mu I)^-1 A^T."""
    A = u.Af
    mu = np.trace(A @ A.T) / u.m
    x0 = np.full(u.pocet_bunek, b.sum() / u.L.sum())
    r = b - A @ x0
    x1 = A.T @ np.linalg.solve(A @ A.T + mu * np.eye(u.m), r)
    x2 = np.linalg.solve(A.T @ A + mu * np.eye(u.pocet_bunek), A.T @ r)
    print(f"  identita FBP = tlumené nejmenší čtverce: rozdíl "
          f"{np.linalg.norm(x1 - x2) / np.linalg.norm(x1):.1e}")


if __name__ == "__main__":
    if "stromy" in sys.argv:                 # jen obrázky skutečných stromů
        obr_stromy()
        sys.exit()
    u = Uloha(12)
    b = u.casy(DUTINA)
    b_sum = u.casy(DUTINA, sum_=0.02)
    print(f"čidel {len(u.cidla)}, paprsků {u.m}, buněk {u.pocet_bunek}, velikost buňky "
          f"{100 * u.h:.2f} cm")
    obr_geometrie(u)
    obr_paprsek(u)
    obr_matice(u)
    obr_pokryti(u)
    obr_fantom(u, b)
    obr_nejednoznacnost(u, b, b_sum)
    obr_zpetna_projekce(u, b)
    obr_bodova_vada(u)
    obr_kaczmarz()
    obr_sirt_iterace(u, b, b_sum)
    obr_omega(u, b)
    obr_stabilizace(u, b_sum)
    obr_vyhlazeni(u, b_sum)
    obr_orez(u, b_sum)
    obr_aat(u, b)
    obr_fbp_kroky(u, b)
    obr_tlumeni(u, b_sum)
    obr_odezva(u)
    obr_srovnani(u)
    obr_pocet_cidel()
    obr_stromy()
    kontrola_identity(u, b)
