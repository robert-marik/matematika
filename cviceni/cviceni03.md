# Výpočet derivací, lineární aproximace

> * Naučíme se derivovat součin a podíl funkcí. Jedná se o použití vzorců, nejsou nutné předchozí znalosti, je nutné mít pouze k dispozici vzorce.
> * Naučíme se používat vzorec pro lineární aproximaci funkce. Naučíme se nahrazovat komplikované funkční závislosti závislostmi jednoduššími.
> * Naučíme se další triky získané díky lineární a polynomiální aproximaci: numerické derivování a numerické řešení rovnic.

## Výpočet derivace součinu a podílu

Určete derivace následujících funkcí, kde $a,b,\mu\in\mathbb{R}$.

1. $f(x)=x\ln x$
1. $f(x)=x\sqrt{x^2+1}$
1. $f(x)=\frac {x}{ax+b}$
1. $f(t)=\frac{t}{t^2+6}$
1. $f(x)=\frac{ax^2}{x^2+1}$
1. $f(x)=\frac {2x^3}{x^2+1}$
1. $f(x)=\frac {ax}{(x-1)^2}$

```{prf:example} Řešení
:class: dropdown
:nonumber:

1. $f'(x)=1\cdot \ln x+x\frac 1x=1+\ln x$
1. $f'(x)=\sqrt{x^2+a}+x\frac{x}{\sqrt{x^2+1}}$
1. $f'(x)=\frac{1\cdot (ax+b)-x\cdot a}{(ax+b)^2}=\frac b{(ax+b)^2}$
1. $f'(t)=\frac{(t^2+6)-t2t}{(t^2+6)^2}=\frac{6-t^2}{(t^2+6)^2}$
1. $f'(x)=\frac {2ax(x^2+1)-ax^22x}{(x^2+1)^2}=\frac {2ax}{(x^2+1)^2}$
1. $f'(x)=\frac {6x^2(x^2+1)-2x^32x}{(x^2+1)^2}$
1. $f'(x)=\frac{a(x-1)^2-ax2(x-1)}{(x-1)^4}= \frac{a(x-1)-ax2}{(x-1)^3}=\cdots$

```

## Základní lineární aproximace

Najděte lineární aproximace funkcí $\sin x$, $\cos x$ a ${(1+x)^n}$ v okolí nuly. Tím dokážete platnost následujících přibližných vzorců platných pro $x$ blízko nuly.
$$
\begin{aligned}
\sin x&\approx  x\\
\cos x&\approx  1\\
(1+x)^n&\approx  1+nx
\end{aligned}
$$

_První dvě aproximace využijeme později pro odvození tvaru matice malých rotací, což je důležité při studiu deformace materiálů. Poslední můžeme využít například pro to, abychom z relativistického vzorce pro  celkovou energii extrahovali část závislou na rychlosti, tj. kinetickou energii (na přednášce)._

```{prf:example} Řešení
:class: dropdown
:nonumber:

$f(x)\approx f(x_0)+f'(x_0)(x-x_0)$

1. $f(x)=\sin x$, $x_0=0$, $f(0)=\sin 0=0$, $f'(x)=(\sin(x))'=\cos x$, $f'(0)=\cos (0)=1$
  $$\sin(x)\approx 0+1\cdot (x-0)=x$$
1. $f(x)=\cos x$, $x_0=0$, $f(0)=\cos 0=1$, $f'(x)=(\cos(x))'=-\sin x$, $f'(0)=-\sin (0)=0$
  $$\cos(x)\approx 1+0\cdot (x-0)=1$$
1. $f(x)=(1+x)^n$, $x_0=0$, $f(0)=(1+0)^n=1$, $f'(x)=((1+x)^n)'=n(1+x)^{n-1}$, $f'(0)=n(1+0)^{n-1}=n$
  $$(1+x)^n\approx 1+n\cdot (x-0)=1+nx$$

```

## Lineární aproximace

Veličina $y$ je funkce proměnné $x$. Najděte její lineární aproximaci v okolí zadaného bodu.

1. $y=xe^x$ v okolí bodu $x=0$
1. $y=rx\left(1-\frac xK\right)$ v okolí bodu $x=0$
1. $y=rx\left(1-\frac xK\right)$ v okolí bodu $x=K$
1. $y=\sqrt x$ v okolí bodu $x=1$
1. $y=\frac 1{\sqrt x}$ v okolí bodu $x=1$

_Ve druhém a třetím příkladě aproximujeme funkci modelující růst
populace v prostředí s nosnou kapacitou $K$. Aproximace v okolí bodu
$x=0$ odpovídá velmi malé populaci. Proto se konstanta úměrnosti ze
získané lineární aproximace nazývá *invazní parametr*._

```{prf:example} Řešení
:class: dropdown
:nonumber:

1. $f(x)=xe^x$, $x_0=0$, $f(0)=0e^0=0$, $f'(x)=(xe^x)'=e^x+x e^x$, $f'(0)=e^0+0e^0=e^0=1$
  $$xe^x\approx 0+1\cdot (x-0)=x$$
1. $f(x)=rx
\left(1-\frac xK\right)$,
$x_0=0$, $f(0)=r0
\left(1-\frac 0K\right)=0$,
$f'(x)= \left(rx-r\frac 1K x^2\right)' = r-\frac{2r}K x$, $f'(0)=r-\frac{2r}{K} \cdot 0=r$
  $$rx\left(1-\frac xK\right)\approx 0+r(x-0)=rx$$
1. $f(x)=rx\left(1-\frac xK\right)$, $x_0=K$, $f(K)=rK\left(1-\frac KK\right)=rK(1-1)=0$, $f'(x)=\left(rx-r\frac 1K x^2\right)'=r-\frac{2r}K x$, $f'(K)=r-\frac{2r}{K} \cdot K=r-2r=-r$
  $$rx\left(1-\frac xK\right)\approx 0-r(x-K)=-r(x-K)=r(K-x)$$
  Poslední aproximaci je možno přepsat do tvaru
  $$rx\left(1-\frac xK\right)\approx  rK\left(1-\frac xK\right)$$
1. $f(x)=\sqrt x$, $x_0=1$, $f(1)=\sqrt 1=1$, $f'(x)=\left(x^{\frac 12}\right)'=\frac 12 x^{-\frac 12}$, $f'(1)=\frac 12$
  $$\sqrt x \approx 1+\frac 12 (x-1)$$
1. $f(x)=\frac 1{\sqrt x}$, $x_0=1$, $f(1)=\frac 1{\sqrt 1}=1$, $f'(x)=\left(x^{-\frac 12}\right)'=-\frac 12 x^{-\frac 32}$, $f'(1)=-\frac 12$
  $$\frac 1{\sqrt x} \approx 1-\frac 12 (x-1)$$

```

## Kinetika chemických reakcí pro malé koncentrace

Rychlost mnoha chemických reakcí je dána vzorcem
$$
  f(x)=\frac {ax}{b+x},
$$
kde $x$ je koncentrace substrátu a $a$, $b$ jsou parametry (konstanty). Tento vzorec se nazývá kinetika  Michaelise a Mentenové. Ukažte, že platí
$$
  \frac{\mathrm df}{\mathrm dx}=\frac{ab}{(b+x)^2}.
$$
Použijte tento výpočet k lineární aproximaci funkce 
$$
  f(x)=\frac {ax}{b+x},
$$
pro malá $x$.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Přímým dosazením dostáváme $f(0)=\frac {a0}{b+0}=0$, $f'(0)=\frac{ab}{(b+0)^2}=\frac {ab}{b^2}=\frac ab$ a odsud
$$\frac {ax}{b+x}\approx 0+\frac ab (x-0)=\frac ab x.$$

```

## Lineární aproximace kvalifikovaným odhadem

<div class="shorten" data-text="Často zběhlejší počtáři lineární aproximaci prostě poznají hned ze zápisu funkce. Jedna z technik je popsána v tomto příkladě.">

Pokud je v součinu výraz, který je blízký nule, ovlivní tento výraz výsledný součin více, než zbylé součinitele. Postavíme toto pozorování na solidnější základy.

Ukažte, že pokud platí $f(x)=g(x)h(x)$ a $g(x_0)=0\neq h(x_0)$, má lineární aproximace funkce $g$ tvar
$$g(x)\approx g'(x_0)(x-x_0)$$ a lineární aproximace funkce $f$ tvar
$$f(x)\approx \Bigl[g'(x_0) (x-x_0)\Bigr]h(x_0),$$
kde v hranaté závorce je lineární aproximace funkce $g$ a tato aproximace je vynásobena hodnotou funkce $h$ v bodě $x_0$.

Situace je jednoduchá zejména v případě, kdy funkce $g$ je lineární a
je sama svojí lineární aproximací. Ukažte, že s uvedenou výbavou je možno
napsat lineární aproximace prvních funkcí $y=xe^x$ v okolí bodu $x=0$
a $y=rx\left(1-\frac xK\right)$ v okolí bodů $x=0$ a $x=K$ (jeden z předchozích příkladů)
  přímo a bez výpočtu. Ukažte, že výpočet není nutný a výsledek se dá kvalifikovaně odhadnout i v
předchozím příkladě s kinetikou Michaelise a Mentenové. Pro tyto účely použijte triviální identitu
$$
  \frac {ax}{b+x}=x\cdot\frac {a}{b+x}.
$$

```{prf:example} Řešení
:class: dropdown
:nonumber:

Obecný vzorec je
$$f(x)\approx f(x_0)+f'(x_0)(x-x_0).$$

Vztah $$g(x)\approx g'(x_0)(x-x_0)$$ z něj plyne okamžitě použitím funkce $g$ a podmínky $g(x_0)=0$.

Pro funkci $f(x)=g(x)h(x)$ v našem případě máme
$$
\begin{aligned}
f(x_0)&=g(x_0)h(x_0)=0\cdot  h(x_0)=0\\
f'(x_0)&=g'(x_0)h(x_0)+g(x_0)h'(x_0)=g'(x_0)h(x_0)+0\cdot h'(x_0)=g'(x_0)h(x_0)\\
\end{aligned}
$$
a přímým dosazením
$$f(x)\approx 0+g'(x_0)h(x_0)(x-x_0)=\Bigl[g'(x_0)(x-x_0)\Bigr]h(x_0)$$

1. Funkce $f(x)=xe^x$ má v $x=0$ první součinitel nulový a druhý součinitel nenulový a platí $e^0=1$. V okolí $x=0$ je první součinitel
  lineární.  Proto v okolí
  $x=0$ platí
  $$xe^x\approx xe^0=x\cdot 1=x.$$
1.  Funkce $f(x)=rx\left(1-\frac xK\right)$ má v $x=0$ první
součinitel $rx$ nulový a  
druhý součinitel $\left(1-\frac xK\right)$ nenulový a platí
$\left(1-\frac 0K\right)=1$. V okolí $x=0$ je první součinitel lineární a v okolí $x=0$ platí
  $$rx\left(1-\frac xK\right)\approx rx\left(1-\frac 0K\right)=rx.$$
1. Funkce $f(x)=rx\left(1-\frac xK\right)$ má v bodě $x=K$ první součinitel $rx$ nenulový roven $rK$ a
   druhý součinitel $\left(1-\frac xK\right)$ nulový. Druhý součinitel je lineární. Proto v okolí
  $x=K$ platí
  $$rx\left(1-\frac xK\right)\approx rK\left(1-\frac xK\right)=r(K-x).$$
1. Funkce $f(x)=x\frac {a}{b+x}$ má v bodě $x=0$ první součinitel $x$ nulový  a
   druhý součinitel $\frac {a}{b+x}$ nenulový a roven $\frac ab$. První součinitel je lineární. Proto v okolí
  $x=0$ platí
  $$x\frac a{b+x}\approx x\frac ab.$$

```

</div>

## Numerické derivování a závislost tepelné vodivosti mědi na teplotě

\iffalse 

```{figure} medene_nadobi.jpg
pixabay.com
```

\fi

Tabulka udává závislost koeficientu tepelné vodivosti mědi na teplotě, $\lambda=\lambda(T)$. Odhadněte pomocí centrální diference derivaci funkce $\lambda$ pro $T=400K$ (cca $127^\circ \mathrm C$). Určete i fyzikální jednotku derivace $\frac{\mathrm d\lambda}{\mathrm dT}$ a slovní interpretaci vypočtené hodnoty.

_Poznámka: Teplota v Kelvinech (termodynamická teplota) je teplota ve stupních Celsia posunutá tak, aby teplota $-273{,}15^\circ\mathrm C$ odpovídala $0\,\mathrm K$. Dílky a tedy i změny teploty jsou na obou stupnicích identické._

|  $T/\mathrm K$ | $\lambda\Bigm/ \mathrm {W}/(\mathrm{m}\,\mathrm{K})$ |
|---------|----------|
|  200 | 413 |
|  400 | 393 |
|  600 | 379 |
|  800 | 366 |

Table: Zdroj: Cengel, Mass and heat transfer.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Teploty jsou v ekvidistantních krocích po $200$ kelvinech. Vezmeme od výchozí hodnoty $400$ kelvinů nejbližší nižší ($200\,\mathrm K$) a nejbližší vyšší ($600\,\mathrm K$) teplotu, najdeme v tabulce odpovídající koeficienty tepelné vodivosti, rozdílem určíme změnu v tomto koeficientu a podílem přepočteme změnu na jeden Kelvin.
$$\frac{\mathrm d\lambda}{\mathrm dT}(400) \approx \frac{(379 -413) \mathrm {W}/(\mathrm m\,\mathrm K)}{2\cdot 200\mathrm K}=-0.085\,\mathrm W \,\mathrm m^{-1}\,\mathrm K^{-2}$$
Při teplotě $T=400 K$ hodnota koeficientu tepelné vodivosti s rostoucí teplotou klesá. S každým stupněm Celsia (s každým Kelvinem) nad danou teplotu klesne koeficient tepelné vodivosti o $0.085\,\mathrm W \,\mathrm m^{-1}\,\mathrm K^{-1}$.

Pokusíme se trošku slovně ilustrovat, co nám vlastně vyšlo. Při teplotě $400\,\mathrm K$ a teplotním gradientu jeden stupeň Celsia na metr délky prochází mědí tepelný výkon $393$ wattů na metr čtvereční, tj. za sekundu se plochou metru čtverečního přenese $393$ joulů. S každým stupněm Celsia navíc tato hodnota malinko poklesne: o $0.085$ joulu. Odsud je patrné, že při změně teploty řádově o desítky stupňů se koeficent změní o malé jednotky procent a v těchto situacích nebude závislost na teplotě významná. 

```

## Iterační metoda

\iffalse 

```{figure} sun_house.jpg
pixabay.com
```

\fi

Úlohy s tepelnou bilancí (např. osluněná stěna) často vedou na rovnice obsahující čtvrtou mocninu  a první mocninu neznámé veličiny. Toto je dáno tím, že vyzařování tepla souvisí podle Stefanova-Bolzmannova zákona se čtvrtou mocninou teploty  a přenos tepla prouděním nebo vedením souvisí s první mocninou teploty.
Koeficient u první mocniny bývá větší než u čtvrté mocniny, protože konstanta ze Stefanova-Bolzmannova zákona je velmi malá. Typickým představitelem by mohla být rovnice $$x^4-8x+6=0.$$
Napište iterační vzorec pro řešení této rovnice Newtonovou metodou a proveďte několik iterací s počáteční aproximací $x_0=1$. Poté porovnejte s postupem, kdy v rovnici osamostatníte $x$ z lineární části a z takové rovnice sestavíte iterační vzorec.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Newtonova metoda: Využitím funkčního předpisu $f(x)=x^4-8x+6$ a derivace $f'(x)=4x^3-8$ dostáváme iterační vzorec $$x_{n+1}=x_n-\frac{x_n^4-8x_n+6}{4x_n^3-8},$$
který konverguje velmi rychle.

|Iterace|Hodnota|
|:----|:----|
$x_0$|$1.000000000000000$
$x_1$|$0.750000000000000$
$x_2$|$0.800123762376238$
$x_3$|$0.801613150991155$
$x_4$|$0.801614587354561$
$x_5$|$0.801614587355901$
$x_6$|$0.801614587355901$

[Python.](https://sagecell.sagemath.org/?z=eJyrsDXk5UrLL1LIVMjMUyhKzEtP1TA00LTi5VIAggrbCl2NCi0tE10LrQptM019DRMtINdY10IToqCgKDOvREGjQhMAkuMRdw==&lang=python&interacts=eJyLjgUAARUAuQ==)

Ad hoc iterace: Rovnici převedeme na tvar
$$x=\frac{x^4+6}{8}$$
a zkusíme iterace
$$x_{n+1}=\frac{x_n^4+6}{8}.$$
Konergenci pozorujeme, ale je pomalá.

|Iterace|Hodnota|
|:----|:----|
$x_0$|$1.000000000000000$
$x_1$|$0.875000000000000$
$x_2$|$0.823272705078125$
$x_3$|$0.807422868167514$
$x_4$|$0.803126865733812$
$x_5$|$0.802005182967586$
$x_6$|$0.801715260030858$

[Python.](https://sagecell.sagemath.org/?z=eJyrsDXk5UrLL1LIVMjMUyhKzEtP1TA00LTi5VIAggpbjQotLRNtM019DQtNiFhBUWZeiYJGhSYAu6IOQQ==&lang=python&interacts=eJyLjgUAARUAuQ==)

```


