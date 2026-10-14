# Report oprav učebního textu (14. 10. 2026)

Opravy z bodů 1 a 7 jsou hotové, tabulka symbolů je napsaná a odkazy na ChatGPT jsou pryč. Nic není commitnuté. Knihu jsem nesestavil, protože nejsou nainstalované Sphinx ani myst_nb. Před commitem tedy doporučuji spustit `scripts/build.sh`. Rovnice jsem ověřil skriptem, který porovná obsah všech `$…$` a `$$…$$` před úpravami a po nich. Změnily se jen věcné chyby uvedené níže, značení zůstalo beze změny.

## Věcné chyby (bod 1)

- **Rovnice:**
  - $f'(x_0)$ v definici tečny
  - interval $(0,1)$ u nosníku z kulatiny
  - prohozené $m$ a $n$ u Π-teorému
  - chybějící $\Delta x_i$ v linearizaci
  - $\partial x^2$ a počáteční podmínka v čase 0 v numerice
  - $T_\infty$ a odkaz na `NZ-I` v ODR
  - $I_{xT}$ ve vzorci pro působiště tlakové síly
  - jednotky °C/min a m s⁻²
  - $n\neq-1$ u vzorce pro $\int x^n\,\mathrm dx$
  - $b_i$ v soustavách
  - $R$ místo $r$ v `cviceni07`
  - $\mathrm dS/\mathrm dh$ v řešení 10. úlohy v `cviceni02` (tuto chybu našla až korektura)
- **Text:**
  - „nekomutativitě“ ve shrnutí
  - „nestabilnímu“ místo „nestacionárnímu“
  - receptor PXY
  - spojitost φ ve větě o existenci řešení
  - $(AB)^T$ platí pro všechny matice, které lze vynásobit, ne jen čtvercové
  - absolutní hodnoty v diagonální dominanci
  - kolmé vlastní vektory u symetrické matice
  - siločáry nezřídlového pole
  - Saint-Venantovy rovnice
  - věta o asymptotě v tabulce s interpretací derivace
  - přestup tepla prouděním a „součinitel přestupu“
  - podíl ΔA/Δh u koryta řeky
- **Dutý kmen** (`dvojny_integral`): větu, že pevnost klesne víc než tuhost, jsem nahradil tvrzením, že obě klesnou ve stejném poměru (podle průřezového modulu). **Prosím, zkontrolujte to:** pokud jste původně myslel jiný mechanismus porušení, vraťte to.

## Korektura (bod 7)

- Opraveno je několik stovek překlepů, chyb ve shodě, zdvojených a slepených slov.
- Zbytky ze slajdů jsou pryč („na předchozím slidu“ → „výše“, nadpisy „Aplikace 1/3“ → „I/II/III“).
- „Konstituční“ jsem všude změnil na „konstitutivní“.
- Odstraněno je zbloudilé `</a>` v `cviceni01` a `>` v `matice`, opraveno `\"Uber` → „Über“ a odstraněno `\\` v `cviceni04`.
- Ve cvičeních korektor navíc doplnil povinné čárky před vedlejšími větami.

## Odkazy na AI z roku 2023

- Smazal jsem všechny sdílené konverzace ChatGPT a poznámky k nim v `cviceni02`, `cviceni05`, `cviceni10` a `derivace_III` i odrážku o AI v úvodu `cviceni02`.
- Odkaz na gist se simulací v `cviceni02` zůstal.

## Tabulka symbolů

- Je v nové stránce `symboly.md`, zařazené v `_toc.yml` za `cviceni00`.
- Tabulky jsou rozdělené podle oblastí a výslovně uvádějí dvojí významy: $T_0$ (okolí nebo počáteční teplota), $T$ (teplota nebo transmisivita), $\vec j$ (jednotkový vektor nebo tok), $\lambda$, $c$, $D$, $h$ a $Q$.

## Úmyslně jsem nechal

- Několik odkazů na předchozí přednášku, které míří správně.
- „Winer Timber Design Award“ v `integraly`: nevím, zda má být „Winner“, nebo „Wiener“.
- V recenzi navržená oprava voltmetru ve shrnutí a jednotek v `cviceni03`: po kontrole jsou tam správně.
- Překlepy a zmínky o slajdech uvnitř HTML komentářů.
- Překlepy v `cheatsheet.tex`.
- Odkazy, které obsahují „slidy“ jen v adrese (`mat-slidy`).
