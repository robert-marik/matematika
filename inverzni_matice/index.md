# Inverzní matice, determinanty

> **Motivace**.
>
> * Chování libovolného systému nezávisí na souřadné soustavě, ve které tento systém popisujeme. Opravdu, dřevo neví, jak jsme si zvolili osy  soustavy souřadnic. Ani, zda používáme pravoúhlou soustavu či jinou. Už vůbec dřevo nepozná, zda úlohu řešíme v pravotočivé či levotočivé soustavě souřadnic. Vhodná volba souřadné soustavy přirozeně neovlivní chování systému. Může ale značně usnadnit výpočty. Proto například při studiu obdélníkového objektu volíme osy ve směru hran. Proto například při studiu dřeva volíme souřadné osy v anatomických směrech dřeva. Tyto dva požadavky jsou částečně proti sobě v případě, že studujeme obdélníkový materiál s hranami jdoucími jiným směrem, než jsou anatomické směry dřeva. Naučíme se s tímto probléme vypořádat. Naučíme se používat matice k přechodu mezi souřadnými soustavami. Naučíme se transformovat fyzikální vlastnosti popsané maticemi z jedné soustavy do druhé. 
> * Ukázali jsme si, že soustavu lineárních rovnic je možné zapsat pomocí maticového násobení ve tvaru $AX=B$. Pokud by veličiny v této rovnici byla reálná čísla, řešitelnost je značně ovlivněna nulovostí či nenulovostí veličiny $A$. Ukážeme si zobecnění této vlastnosti i pro matice a soustavy rovnic. K tomu si představíme nový pojem - determinant matice.

## Inverzní matice

https://youtu.be/udDtFU4pxkY

<!-- YTB odf4e4fJHAU -->

U reálných čísel máme doplňkové operace ke sčítání a násobení. Jsou to
odečítání a dělení. Odečítání matic můžeme implementovat jako sčítání
matice s maticí vynásobenou minus jedničkou: $A-B=A+(-B)$. Oproti tomu
operace dělení matic vůbec není implementována. U reálných čísel lze
dělení nahradit násobením převrácenou hodnotou: $\frac
{a}{b}=ab^{-1}$. Tuto proceduru částečně rozšíříme pro
matice. Připomeňme ještě, že roli neutrálního prvku při násobení matic
hraje jednotková matice. Například pro matice $3\times 3$ je
jednotková matice   $$I= \begin{pmatrix}    1&0&0\\    0&1&0\\    0&0&1 \end{pmatrix}.$$

```{prf:definition} Inverzní matice
:nonumber:

Buď $A\in\mathbb R^{n\times n}$ čtvercová matice řádu $n$. Jestliže
existuje čtvercová matice $A^{-1}$ řádu $n$, splňující vztahy
$$A^{-1}A=I=A A^{-1},$$
nazýváme matici $A^{-1}$ *inverzní maticí k matici $A$*.
```


**Poznámka.** Předchozí definice nezaručuje existenci inverzní
matice. K některým čtvercovým maticím inverzní matice existuje, k některým ne. Později uvidíme, že existuje jednoduchá charakterizace
matic, ke kterým inverzní matice existuje, pomocí determinantu matice.

```{prf:theorem} Inverze maticového součinu
:nonumber:

Inverzní matice k součinu dvou matic je součinem jednotlivých inverzních matic, ale v opačném pořadí, tj. $$(AB)^{-1}=B^{-1}A^{-1}.$$
```


\iffalse

<div class='obtekat'>

```{figure} rubik.jpg
Klasickým permutačním hlavolamem je Rubikova kostka. Na něm si můžeme vyzkoušet některé vlastnosti maticového součinu jako nekomutativita nebo nutnost změny pořadí při invertování maticového součinu. Zdroj: congerdesign, pixabay.com.
```

</div>

**Příklad.** Pomocí matic a jejich součinu je možné zapsat libovolnou permutaci konečněprvkové množiny. Známým permutačním hlavolamem je Rubikova kostka. Na ní snadno vidíme, že pokud kostku zamícháme ze složeného stavu tahem v horní stěně a poté v pravé stěně, pro opětovné složení musíme vracet tahy v opačném pořadí, tj. nejdřív vrátit tah v pravé stěně a poté ve stěně horní. Pěkně to jde vidět na [následující animaci](https://alg.cubing.net/?alg=R_U_%0A%2F%2F_dva_tahy,_ka%C5%BEd%C3%BD_je_mo%C5%BEn%C3%A9_reprezentovat_matic%C3%AD_permutace_%0AU-_R-_%0A%2F%2F_vr%C3%A1cen%C3%AD_tah%C5%AF_v_opa%C4%8Dn%C3%A9m_po%C5%99ad%C3%AD_slo%C5%BE%C3%AD_kostku_zp%C4%9Bt), kterou můžete spustit nebo přehrávat po jednotlivých krocích. Na druhou stranu, tato vlastnost se dá využít k vyřešení Rubikovy kostky naprosto bez algoritmů, protože při vhodně zvolených tazích ovlivníme jenom málo kostiček, například [jenom tři](https://alg.cubing.net/?alg=R-_D-_R___%2F%2F_TAH1:_roh_z_horn%C3%AD_steny_presuneme_dolu%0AU___%2F%2F_TAH_2:_pootoceni_horni_steny%0AR-_D_R__%2F%2F_vratime_TAH1%0AU-_%2F%2F_vratime_TAH2). 

\fi

### Inverzní matice k matici popisující rotaci v rovině

Pro matici rotace $$R_\theta=\begin{pmatrix}  \cos\theta & -\sin \theta\\  \sin\theta & \cos\theta\end{pmatrix}$$ z minulé přednášky platí
\dm $$(R_\theta)^{-1}=R_{-\theta} =  \begin{pmatrix}   \cos(-\theta) & -\sin (-\theta)\\   \sin(-\theta) & \cos(-\theta) \end{pmatrix} =\begin{pmatrix}   \cos\theta & \sin \theta\\   -\sin\theta & \cos\theta \end{pmatrix}$$
což je přirozené pokud si uvědomíme, že inverzní operací k pootočení
roviny o úhel $\theta$ je pootočení roviny o úhel opačný.

Odsud mimo jiné vidíme, že platí
\dm$$(R_\theta)^{-1}=\begin{pmatrix}   \cos\theta & -\sin \theta\\   \sin\theta & \cos\theta \end{pmatrix}^{-1}=\begin{pmatrix}   \cos\theta & \sin \theta\\   -\sin\theta & \cos\theta \end{pmatrix} =\begin{pmatrix}   \cos\theta & -\sin \theta\\   \sin\theta & \cos\theta \end{pmatrix}^T=(R_\theta)^T,$$
tj. že inverzní a transponovaná matice jsou v případě matice rotace stejné. To je velká náhoda, ale přesto matice s touto vlastností hrají tak důležitou roli, že si vysloužily vlastní název představený v následujícím odstavci. 

### Ortogonální matice

```{prf:definition} Ortogonální matice
:nonumber:
 *Ortogonální matice* je matice, jejíž transponovaná matice je současně maticí inverzní.
```


Řádky ortogonální matice jsou tvořeny navzájem kolmými vektory
jednotkové délky. Má-li například symetrická čtvercová matice $A$ řádu
$n$ celkem $n$ lineárně nezávislých jednotkových vlastních vektorů,
potom matice vytvořená tak, že sloupce nebo řádky matice jsou tyto
vektory, je ortogonální.

## Matice přechodu 

https://youtu.be/uOmV6DGMPbw

<!-- YTB AdbMMzTfR00 -->

\iffalse

manimp:MatrixMultiplication|Pomocí maticového násobení můžeme snadno přecházet od jedné soustavy souřadnic k jiné. (Poslední část prezentace).

<div class='obtekat'>

```{figure} souradnice.png
Matice rotace a maticové násobení umožňuje vyjáření souřadnic v různých vzájemně pootočených souřadných soustavách.
```

</div>

\fi

Ukážeme si, že pomocí matic je možné přepočítávat souřadnice mezi jednotlivými souřadnými soustavami. Praktické využití je studium ortotropních materiálů v situace, kdy pro matematický popis jsou výhodné směry os, ale roviny symetrie neodpovídají souřadným rovinám. Například dřevěný kvádr je vhodné studovat tak, že hrany kvádru jsou rovnoběžné se souřadnými osami. Materiálové vlastnosti jsou známy v anatomických směrech dřeva. Pokud tyto směry nejsou nejsou rovnoběžné s osami (kvádr je nařezaný našikmo), je potřeba mezi souřadnými soustavami přecházet. To se dá elegantně udělat pomocí maticového násobení a inverzní matice. 

Předpokládejme, že v rovině jsou dány dvě kartézské soustavy souřadnic $\mathcal B$ a $\mathcal B'$, které jsou vzájemně pootočené o úhel $\theta$. V těchto soustavách budou souřadnice $(x,y)^T$ a $(x',y')^T$. Je-li soustava $\mathcal B'$ otočená oproti soustavě $\mathcal B$ o úhel $\theta$ proti směru hodinových ručiček, má (viz obrázek) jednotkový vektor ve směru osy $x'$ v bázi $\mathcal B$ souřadnice $(\cos(\theta),\sin(\theta))^T$ a jednotkový vektor ve směru osy $y'$ má v bázi $\mathcal B$ souřadnice $(-\sin(\theta),\cos(\theta))^T$. Proto je vztah mezi souřadnicemi dán maticovým součinem $$\begin{pmatrix}x\\y\end{pmatrix}_{\mathcal B}=\begin{pmatrix}  \cos\theta & -\sin \theta\\  \sin\theta & \cos\theta\end{pmatrix}\begin{pmatrix}x'\\y'\end{pmatrix}_{\mathcal B'}.$$
Matice $$R=\begin{pmatrix}  \cos\theta & -\sin \theta\\  \sin\theta & \cos\theta\end{pmatrix}$$ je matice, kterou jsme poznali jako matici rotace. Je to matice, která svým působením pootočí vektor který ji násobí zprava o úhel $\theta$ proti směru hodinových ručiček.
Ve výše uvedením kontextu se tato matice nazývá maticí přechodu mezi oběma uvažovanými souřadnými systémy. Matice přechodu umožňuje najít souřadnice
vektoru v jedné souřadné soustavě pomocí souřadnic vektoru v souřadné soustavě vzniklé pootočením díky vztahu $$\begin{pmatrix}x\\y\end{pmatrix}_{\mathcal B}=R\begin{pmatrix}x'\\y'\end{pmatrix}_{\mathcal B'}.$$
Tato matice má inverní matici a proto evidentně můžeme mezi souřadnicemi přecházet i v opačném směru vztahem $$R^{-1}\begin{pmatrix}x\\y\end{pmatrix}_{\mathcal B} = \begin{pmatrix}x'\\y'\end{pmatrix}_{\mathcal B'}.$$

V inženýrských problémech je častou aplikací lineární algebry
transformace úlohy do vhodných souřadnic, ve kterých je popis
jednodušší. Zpravidla se jedná o prosté otočení. Toto se používá při
studiu dřeva, které má anatomicky význačné směry, při studiu
vrstvených materiálů, při studiu chování vodorovně uložených
geologických vrstev. Nemusí však vždy jít jenom o materiál s
charakteristickými směry. Transformace mezi souřadnicemi se používá
například v letectví, kdy je jedna souřadná soustava spojena s trupem
a další dvě jsou pootočené ve směru křídel šípovitě připojených k
trupu.

Matici transformace popisující otočení souřadnic budeme zkráceně označovat $R$, pokud budeme potřebovat zdůraznit velikost úhlu, použijeme $R(\theta)$ a pokud budeme potřebovat matici rozepsat ve složkách, budeme zkracovat výrazy $\cos\theta$ a $\sin\theta$ na $C$ a $S$ a psát
$$R= \begin{pmatrix}  C & -S \\ S & C\end{pmatrix}.$$
Potom například platí
$$R^{-1}=\begin{pmatrix}  C & S \\ -S & C\end{pmatrix}.$$

## Zobrazení v různých soustavách souřadnic

Ukážeme si důležité využití matice přechodu. Předpokládejme, že máme
zobrazení $f\colon X\to Y$, které je možno charakterizovat maticemi.  Na
vstupu i výstupu je tedy vektor.
Může se jednat třeba o zobrazení, které působícím silám přiřadí
deformaci tělesa, což uvidíme v Hookově zákoně později. Může
se jednat také o zobrazení, které vektoru charakterizujícímu změnu tlaku v
podzemní vodě nebo změnu koncentrace vody ve dřevě přiřadí směr proudění. (Směr podnětu a výsledného proudění si nemusí odpovídat,
protože voda je poháněna rozdílem tlaků ve směru největšího poklesu
tlaku nebo rozdílem koncentrací ve směru největšího poklesu koncentrace, ale současně si v anizotropním prostředí hledá cestu nejmenšího
odporu).

Nechť je naše zobrazení vyjádřeno v nějaké souřadné soustavě $\mathcal
B$ maticí $A$, tj. $$Y=AX,$$ kde $X$ a $Y$ jsou souřadnice vzoru a
obrazu v souřadné soustavě $\mathcal B$. Budeme chtít toto zobrazení
vyjádřit v jiné soustavě. Například v soustavě $\mathcal B'$ takové,
že platí $X=PX'$ a $Y=PY'$, kde čárkovaná písmena jsou souřadnice v
čárkované souřadné soustavě $\mathcal B'$. Dosazením získáme $$PY'=APX'$$ a po
vynásobení inverzní maticí $$P^{-1}(PY')=P^{-1}(APX'),$$ tj
$$Y'=(P^{-1}AP)X'.$$ V pootočených souřadnicích $\mathcal B'$ je tedy zobrazení charakterizováno
maticí $P^{-1}AP$. Pro vhodně zvolenou matici $P$ může být matice v
nové bázi podstatně jednodušší než matice v bázi původní.

<!-- 
V následujícím příkladě si ukážeme, že vhodně zvolenou maticí $P$
můžeme dosáhnout toho, že $P^{-1}AP$ je diagonální matice. Na dalším
slidu již rovnou zvolíme vhodnou bázi a matice, která bude sice
impozantních rozměrů $6\times 6$, bude plná nul a proto relativně pěkná. 

**Příklad.**
Pro matice $A= \begin{pmatrix}
  1 & 0 \\ 1 &2
\end{pmatrix}$
a $P= \begin{pmatrix}
  0& -1 \\ 1 &1
\end{pmatrix}$
platí (po chvilce počítání)
$$  P^{-1}AP= \begin{pmatrix}
  2& 0 \\ 0 & 1
\end{pmatrix}.
$$
Odsud vidíme, že v souřadnicích ke kterým bychom přešli pomocí matice
$P$ je vyjádření zobrazení matice $A$ mnohem jednodušší, protože matice
$P^{-1}AP$ je diagonální.

-->

Častým úkolem je zapsat vztahy mezi veličinami tak, aby byly co
nejjednodušší a proto jeden z častých úkolů v lineární algebře bývá
takovou šikovnou bázi nalézt. Nastíníme neoptimističtější variantu
postupu, případné detaily a řešení zádrhelů je možné najít v odborné
literatuře. Zpravidla vyjadřujeme zobrazení v bázi tvořené
ortonormálními vlastními vektory matice $A$. Sloupce matice $P$ jsou
vlastní vektory matice $A$. Pokud je matice $A$ symetrická, je matice
$P$ navíc ortogonální, její inverze je tedy matice
transponovaná. Tomuto procesu se říká diagonalizace matice, protože
$P^{-1}AP$ vychází diagonální a v diagonále vychází právě vlastní
čísla matice.

Stejným způsobem se transformují i fyzikální veličiny veličiny popisované maticemi, nazývané tenzory.

\iffalse

* [Ukázka Sage](https://sagecell.sagemath.org/?z=eJytkU1v2zAMhu8G_B8INEWkRM3ioOlNB5-GHQb4sJuRFYqtzmoV0ZNlr_Gw_z469ryP9lJgBkzT4ks9fMFUnlTw5pnl-V7sDiLfUTxwuAI6N4WOo-y3InnXfPWB7bm42f1Kh5b5eBbQFZvglWtqbDTjMN8HtddFhWULJUJjnrBzGo6q1xBHVxAUHWA7FSihioFGg1NtYU4aKqtLFaDGvtSPJo7iqKnwG7AqnCzzy0Uqr5uFgEU2fJfXzKqgn1nKxZhknB6apVelcqbr0Z8ly7diSy6SKSYUt5u9SDZ3Qzb-U43_y8o-f79JfqQTagSwbGNcp_1gmq_SVTbyJu8dOOwudi-jv5n_P1YRR3j0qj_LPFt1ugjomeHwgB4MGAeXmQ5x9OHje1mjcYGNcgEFWvRy6XW5FLSgXsvbLV_XaM9f0L2uUraulCQzfG2N06-J-Iiidz3iLgPMgFl7tK3-WzxyJ_mDsVZ-8q3-A_qid1gfo2bSNDVZv_e0FpQJ_wkl8e8J&lang=sage&interacts=eJyLjgUAARUAuQ==)
* [Ukázka Python](https://sagecell.sagemath.org/?z=eJyNUk2umzAQ3iNxhxFvAwhogpTuWHADFlU30WvlBCs4gMe1DS25Qw_SQ3TVHqxjQvJI36vUjTU_33zfNyM_gegVagutFA2OXIIcejUBg56pDm0nDr63QJaOAanutZ7ZBZapyUWurzrre08gmbGMKAUozY1EYwXxKkKzo6uOvObHloNESwUCCbDCtAM0WFPN96TKDLefqSEtKitQmpCojsJQWOwSMINy1Kb4oAceOc0SztyZEkR4wYNmF1LyvbIgLipr8S3c73dJ_pzsc3qf56FqNeT4SX-AGsGIFkfJ4UAs4ICWUQGHpUEBdQQYWoENR9FzaDpeM0s7Xmp-Jt3qQXf7zm30RdtwFyVpvsqcnXVzjSSTmdVMGoWGhxGQk_kiYVAWQVJG97SitJoX-ri2Lt46CdSCnVCyzl2HLqDHdoJe9EgrsHHVH-BsaFGlWUsMBJJDR__kRfRTmG6juIxn9Ti-ZeTD98YL6unhBJtkQ7tul3dL7ybbJdvsvYuuOfUeN_a92fVUlPFMeGfOoYDqVrti8hsodyj6iJn7lGFMHpjWbArnZpQEKQYJdOzAuyKosee_v_M2iN4cuTL_NTMX4TrZDv-YvDqhSUzT1ahFUpO_fsJ_Cb-en6VvLD8afGWj4ycu63DJTlrcY9Pg1zD6A0mFUhA=&lang=python&interacts=eJyLjgUAARUAuQ==)

\fi

## Praktická aplikace: transformace tenzoru

https://youtu.be/7Oi3ruVNUzI

\iffalse

<div class='obtekat'>

```{figure} pozgaj.jpg
Úloha na transformaci tenzoru napětí do anatomických směrů dřeva. Znázorněná krychlička je jenom reprezentující element většího tělesa. Zdroj: A. Požgaj a kol., Štruktúra a vlastnosti drevá. 
```

```{figure} kytara_leta.png
Stejná úloha jako výše (leta ve dřevě jdou pod úhlem 30 stupňů a transformujeme do tohoto směru) méně inženýrským přístupem.
```

```{figure} spoj_drevo_sikmy.jpg
U šikmého lepeného spoje se používá transformace do roviny spoje k posouzení únosnosti tohoto spoje. Lepidlo má definovanou pevnost spoje při normálovém a smykovém namáhání a transformace nám prozradí, jak se předpokládané namáhání projeví v těchto směrech a zda lepidlo spoj udrží.
```

</div>

\fi

V knize A. Požgaj a kol., Štruktúra a vlastnosti drevá, je následující
úloha (str. 322, vydání 1997, ISBN 80-07-00960-4). Dřevo v konfiguraci podle obrázku je namáháno pouze tahovou
silou svisle, tedy tenzor napětí má jenom jednu nenulovou
složku. Naším cílem je pootočit souřadnou soustavu tak, aby byl tenzor
napětí vyjádřen v anatomických směrech dřeva. Úloha je v knize vyřešena pomocí směrových kosinů. Ukážeme si alternativní způsob, který je výhodný v tom, že využívá pouze základní aparát lineární algebry. Původní souřadnice
$(x_1,x_2)$ označíme $(x,y)$, osa $x$ směřuje vodorovně vpravo (v obrázku $x_2$) a osa $y$ nahoru (v obrázku $x_1$). Tenzor napětí je $A=\begin{pmatrix}  0 & 0\\0& 10\end{pmatrix}$ (tah pouze ve směru osy $y$). Souřadnice je nutno pootočit o $30$ stupňů po směru hodinových ručiček, tj. v záporném směru. Nový tenzor napětí (viz [Sage](https://sagecell.sagemath.org/?z=eJx9ULtuwzAM3A34HwhkiCzIrVwXQRcPSZYODVB4NTIorhArsSVDD6PJH_U7-mOVH6mRoQUX8ng83HEBb0JypqUAVh_5QTMCrVJWldxDClIKxrpWOo-Cabh28JqHQcc0WtqKW7aMwiDPGma1-ERFUSqDBjwisRFy6vekmAcyc_Z7f72brymhnkpJQoeNq3idxSl9TF4obkUYtFpIC0gilD8Yd5hksrgnRhHe4Xt8hCOv1NcC3tX1yE59wEaVYoijuktZwVl5e47ASUh2hmunai6_v0CZSxho9pG1orcQBuv7oGlKsV-PiVZj7_3309PzvIJf4pBq84_I7WxSWf0psp1FktvXxqdJtMZbvIl-AGVpkmc=&lang=sage&interacts=eJyLjgUAARUAuQ==) nebo [Python](https://sagecell.sagemath.org/?z=eJxVjj0OwyAMhXck7sBoIoioulXKEbKwogyooQpScRA_Unv7koih8fQ--z3bPsQ9FYY1xC-zmWGkhJK6ufeEcUx29RYzyLviR391L6ahbK5Y_qCEtUqu1IQtNwZbkv-AMU0_99xtQjbMHjsuwlxYXMzLcp6Zp_91SqiWUuKm-jgmjwU0yONNPsyDhlPxHzCvP64=&lang=python&interacts=eJyLjgUAARUAuQ==)) je $$R(30^\circ)AR(-30^\circ)=\begin{pmatrix}   2.5 & -4.3\\-4.3&  7.5\end{pmatrix}.$$ V nových souřadnicích je směr $y'$ podélný a proto $\sigma_{RR}=2.5$
a $\sigma_{LL}=7.5$. Mimodiagonální složka udává komponentu $\sigma_{RL}=-4.3$, smykové napětí. Tento výsledek je stejný, jako výsledek získaný jiným postupem v knize, pomocí směrových kosinů. Použili jsme však jenom základní nástroje lineární algebry.

Výše uvedený výpočet se používá, když chceme najít deformaci vyvolanou působícím napětím. Protože konstanty udávající materiálovou odezvu máme změřeny v anatomických směrech dřeva, je nutno nejprve zjistit, jaké namáhání je v těchto směrech, pomocí materiálových konstant zjistíme, jaká je deformace v těchto směrech a poté zpětnou transformací přepočítáme tuto deformaci do původních souřadnic.

Stejný výpočet používáme, pokud se snažíme transformovat působící napětí při posouzení, jaké smykové a jaké normálové napětí působí na šikmý lepený spoj. Pokud je spoj pod úhlem $30$ stupňů a v ose $y$ působí tahové napětí $10\,\mathrm{MPa}$, potom  normálové napětí namáhající tento spoj je $7.5\,\mathrm{MPa}$ a smykové napětí $4.3\,\mathrm{MPa}$.


````{prf:algorithm} Obecné vzorce pro transformaci tenzoru
:class: dropdown

\iffalse

<div class='obtekat'>

```{figure} jatawood.jpg
Schopnost transformovat tenzory napětí nebo deformace  je důležitá u studia vrstvených materiálů. Ty umožní anizotropii potlačit (překližka) nebo zvýraznit (lyže, luk). Někdy vrstvíme jen tak, pro krásu. Na obrázku Jatawood, pro výrobu rukojetí nožů. Zdroj: jatagan.eu
```

</div>

\fi

Úloha na transformaci tenzoru, kterou jsme řešili v minulém odstavci je
v aplikacích velmi důležitá. Proto existuje řada grafických nebo
inženýrských metod na řešení tohoto úkolu. Tyto metody jsou důvtipné a názorné, například metoda Mohrovy kružnice, oproti lineární algebře však mají zásadní nevýhodu: uživatel se musí stále učit něco nového a dostává návod "jak", nikoliv "proč". Použitím aparátu lineární algebry, stejně jako dokážeme v pootočených souřadnicích vyjádřit libovolné zobrazení, dokážeme vyjádřit v pootočených souřadnicích i libovolný tenzor. Vzorce jsou stejné a navíc při otočení v rovině je matice rotace ortogonální, tj. inverzní matice je maticí transponovanou. Pro symetrický tenzor $A=\begin{pmatrix}  a_{11} & a_{12} \\ a_{12} & a_{22}\end{pmatrix}$
dostáváme v souřadnicích otočených o úhel $\theta$ proti směru hodinových ručiček
$$\begin{pmatrix}  a'_{11} & a'_{12} \\ a'_{12} & a'_{22}\end{pmatrix} = \begin{pmatrix}  C&S\\-S&C\end{pmatrix}\begin{pmatrix}  a_{11} & a_{12} \\ a_{12} & a_{22}\end{pmatrix}\begin{pmatrix}  C&-S\\S&C\end{pmatrix},$$
kde [po výpočtu](https://sagecell.sagemath.org/?z=eJyFUMGKgzAQvQv-Q_DSKImsHhc8FI8LPZi9qbukRWlAJxJTWfv1O7Fsa2WXDZkkvMl7M_MmaejOnhsriUwSjJTINCVHB-RE7ELf870i66U16ouWZc64qFkpWF7XmNs_Mkhnjo9ZPBmqLD98bzAKLKHBu5Ewttr0epIwE9vAVZvXCvivK0DuIaO0iK3jDXpsaBhG-6gI41H1Q6fa-bO9dB0N7yUOj2dQwZvuBw0N2HlTJFgxypca9xpIatybH8nzJBXcZ5EnUAQ9UKfmz1F4QHChwsJaefmRMoGRRiLKnan4dhj_AThezAWiHLNoqFO6N7LobWYGa3QniYKpMVfQo_2_vecmfe-mG4-X40hFxkUY3Qptff8GTrag5g==&lang=sage&interacts=eJyLjgUAARUAuQ==)
$$\begin{aligned}a'_{11}&=C^2a_{11}  + S^2a_{22} + 2CSa_{12},\\a'_{22}&=S^2a_{11}  + C^2a_{22} - 2CSa_{12},\\a'_{12}&=-CSa_{11} + CSa_{22} + (C^2 - S^2)a_{12}.\end{aligned}$$
Tento vztah je lineání vzhledem ke všem komponentám a je možné jej zapsat pomocí maticového násobení
$$\begin{pmatrix}  a'_{11}\\a'_{22}\\a'_{12}\end{pmatrix}=\begin{pmatrix}  C^2 & S^2 & 2CS\\  S^2 & C^2 & -2CS\\  -CS  & CS & C^2-S^2\end{pmatrix}\begin{pmatrix}  a_{11}\\a_{22}\\a_{12}\end{pmatrix}.$$
Tento vztah je uveden i v literatuře A. Požgaj a kol., Štruktúra a vlastnosti
drevá, a v e-opoře [Fyzikální a mechanické vlastnosti
dřeva](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9178). Zde
je také uvedena jedna z aplikací, transformace tenzoru deformací
naměřených při bobtnání dřeva. V této úloze je nutno tenzor deformací transformovat do anatomických směrů dřeva. To je
možné udělat po změření sklonu vláken a pootočení tenzoru o příslušný
úhel.

<!-- Získáme diagonální tenzor, který má v diagonále deformace v
anatomických osách dřeva. Jednodušší alternativou je určení vlastních hodnot
tenzoru deformace pomocí charakteristického polynomu, což je v tomto
případě polynom kvadratický. Která vlastní hodnota patří ke kterému
směru určíme ze znalosti uspořádání koeficientů bobtnání dřeva v
jednotlivých směrech podle velikosti. Při použití vlastních hodnot je
výhodou, že používáme standardní nástroje lineární algebry a metoda je
použitelná bez znalosti úhlu, který svírají vlákna dřeva s osami
soustavy, ve které určujeme tenzor deformace. -->

Inverzní operací je pootočení o úhel $-\theta$ a proto je snadné najít inverzní transformaci: vzhledem k sudosti funkce $\cos$ a lichosti funkce $\sin$ stačí změnit znaménko u členů s $S$, tj. 
$$\begin{pmatrix}  a_{11}\\a_{22}\\a_{12}\end{pmatrix}=\begin{pmatrix}  C^2 & S^2 & -2CS\\  S^2 & C^2 & 2CS\\  CS  & -CS & C^2-S^2\end{pmatrix}\begin{pmatrix}  a'_{11}\\a'_{22}\\a'_{12}\end{pmatrix}.$$

**Poznámka.** Pokud vypočteme derivaci členů $a'_{11}$ a $a'_{22}$ podle $\theta$, dostaneme použitím
$$\frac{\mathrm d}{\mathrm d\theta}C^2=\frac{\mathrm d}{\mathrm d\theta}\cos^2\theta=2\cos\theta(-\sin\theta)=-2CS,$$
a analogicky
$\frac{\mathrm d}{\mathrm d\theta}S^2=2SC$, $\frac{\mathrm d}{\mathrm d\theta}CS=-S^2+C^2$ derivace 
$$
\begin{aligned}
  \frac{\mathrm d a'_{11}}{\mathrm d\theta}&=   -2CSa_{11}+2SCa_{22}+2(C^2-S^2)a_{12}=2a'_{12},\\
  \frac{\mathrm d a'_{22}}{\mathrm d\theta}&=   2SCa_{11}-2CSa_{22}+2(S^2-C^2)a_{12}=-2a'_{12}.\\
\end{aligned}
$$
To znamená, že lokální extrémy diagonálních prvků nastávají v
okamžiku, kdy jsou prvky mimo diagonálu nulové. Toto pozorování
perfektně ladí s výsledky, které známe v lineární algebře i bez hledání
lokálních extrémů a bez derivací. Náznak tohoto konceptu si představíme na dalších
stránkách. Budeme potřebovat vlastní
vektory matice.

**Pozor.** V případě tenzoru deformace se někdy se namísto
mimodiagonální komponenty bere její dvojnásobek, protože ten má
názorný význam jako úhel smyku. Proto se někdy v literatuře uvádí
transformační vzorec pro deformace v upraveném tvaru, kdy u složek se
součinem $CS$ ve třetím sloupci není koeficient $2$ a u odpovídajících
složek ve třetím řádku tento koeficient naopak figuruje. Je proto
potřeba dávat pozor na to, s jakými komponentami je tenzor malých
deformací uvažován.

````

## Role vlastních vektorů při transformaci matic

https://youtu.be/yqjaeqQu0bE

<div class='obtekat'>

```{figure} eigenvectors.png
Eigenvectors (red) do not change direction when a linear transformation (e.g. scaling) is applied to them. Other vectors (yellow) do. Zdroj: http://www.visiondummy.com. 
```

</div>

Budeme zkoumat, kdy platí $$P^{-1}AP=D$$ pro čtvercové matice $P$, $A$
a diagonální čtvercovou matici $D$. Vynásobením maticí $P$ zleva
dostaneme
$$AP=PD.$$
Ve cvičení jsme násobili čtvercovou matici s maticí diagonální a není
těžké vidět obecný princip, že matice $PD$ má za sloupce násobky
sloupců matice $P$ s odpovídajícím číslem z hlavní diagonály matice
$D$. Například pro první sloupec matice $P$ a první číslo v hlavní
diagonále matice $D$, které označíme $\vec p_1$ a $\lambda_1$, dostáváme
$$A\vec p_1=\lambda_1 \vec p_1,$$
tj. (viz předchozí přednášky) $p_1$ je vlastní vektor matice $A$
příslušný vlastní hodnotě $\lambda_1$. Podobný princip platí pro
všechny sloupce. Je otázkou, jestli vlastních hodnot a vlastních
vektorů je tolik, kolik pro diagonalizaci "potřebujeme". Částečně
pozitivní odpověď na tuto otázku udávají věty na následujícím slidu.

## Transformace symetrické matice na diagonální tvar

```{prf:theorem} Vlastní čísla symetrické matice
:nonumber:

Symetrická čtvercová matice $A$  řádu $n$ má $n$ reálných vlastních čísel (počítáno i s případnou násobností).
```


```{prf:theorem} Diagonalizace symetrické matice
:nonumber:

Nechť má symetrická čtvercová matice $A$ řádu $n$ celkem $n$ reálných různých vlastních čísel $\lambda_i$. Označme odpovídající vlastní vektory jednotkové délky $\vec v_i$.

* Matice $P$ sestavená tak, že sloupce této matice jsou tvořeny vektory $\vec v_i$ je ortogonální.
* Matice $D$ definovaná vztahem $$D=P^TAP$$ je diagonální.
* Diagonální prvky matice $D$ jsou právě vlastní čísla $\lambda_i$ a jsou ve stejném pořadí jako odpovídající vlastní vektory v matici $P$.
```


```{prf:remark} Diagonální tvar materiálových vlastností dřeva
:nonumber:
 Typickým ortotropním materiálem je dřevo. Pokud transformujeme tenzor difuzní matice pro dřevo na diagonální tvar, jsou diagonální prvky v poměru přibližně $D_L:D_R:D_T=35:3:2$ (P. Horáček, Fyzikální a mechanické vlastnosti dřeva, 2008 , str. 65). Ortotropní charakter má však nejenom transport tekutin, ale i sesychání a bobtnání. V tomto případě však naopak v podélném směru dřevo bobtná nejméně a tenzor popisující bobtnání má po transformaci na diagonální tvar v diagonále prvky v poměru přibližně $\alpha_T:\alpha_R:\alpha_L=20:10:1$ (P. Horáček, Fyzikální a mechanické vlastnosti dřeva, 2008 , str. 38).
```


\iffalse 

<div class='obtekat'>

```{figure} rubik.svg
Pokud je tenzor spojený s materiálovou charakteristikou v diagonálním tvaru, redukuje se složitost problému. Podobná redukce složitosti je i při jiných příležitostech, například při skládání Rubikovy kostky pomocí metody [Human Thistlethwaite Algorithm](https://www.speedsolving.com/wiki/index.php/Human_Thistlethwaite_Algorithm). V této metodě se úloha nejprve redukuje na jednodušší úlohu, kdy každá barva je buď ve svojí straně nebo protilehlé. Tak je možné složit kostku buď bez nepříjemného učení se umělých algoritmů (člověk), nebo do 20 tahů (stroj a nejlepší lidé).
```

</div>

\fi

Matice transformace $P$ z předchozí věty je ortogonální (její
transponovaná matice je současně její inverzní matice) a její
determinant (veličina, se kterou se seznámíme vzápětí) je roven $1$
nebo $-1$. Pokud je determinant kladný,
reprezentuje matice pootočení soustavy souřadnic. Pokud je determinant
záporný, jedná se o pootočení spojené se zrcadlením jedné osy. Protože
tento případ většinou z fyzikálních důvodů nepreferujeme, sestavujeme
matici transformace tak, aby měla determinant kladný. V případě
záporného determinantu stačí prohodit dva vektory (sloupce matice
transformace) mezi sebou, nebo jeden vynásobit faktorem $-1$.

Pro kontrolu je zajímavé vědět, že determinant matice se pootočením
nemění a je tedy stejný pro původní i transformovanou matici. Totéž
platí pro součet prvků v hlavní diagonále (v lineární algebře se
nazývá stopa matice), pro charakteristický polynom a pro vlastní
hodnoty. Tenzor, jak jej uvažujeme v tomto textu, je matice, která má
navíc fyzikální význam a vzhledem ke své povaze pro ni platí speciální
transformační pravidla. Nicméně je to mimo jiné i matice a proto vše
výše uvedené platí i pro tenzory.

Transformace tenzorů je užitečná a důležitá činnosti. Bohužel však vzorce s touto transformací spojené nejsou natolik zapamatovatelné, aby bylo obvyklé s nimi pracovat. Možnosti jsou v zásadě tři.

* Mít vzorce v psané podobě po ruce a pouze do nich dosazovat.
* Mít k dispozici jednoduše zapamatovatelný postup, jak s transformacemi pracovat. Takový postup existuje, nazývá se [Mohrova kružnice](https://cs.wikipedia.org/wiki/Mohrova_kru%C5%BEnice) a po zapracování se jedná o efektivní grafickou metodu pro transforamci tenzorů. Zpravidla je v literatuře popsána pro tenzor napětí, funguje však obecně.
* Pracovat pouze s elementárními prostředky lineární algebry. Narozdíl od předchozích bodů máme přehled o tom, co a proč děláme (oproti vzorcům) a nemusíme se učit další metodu (oproti Mohrově kružnici).

## Determinant matice

https://youtu.be/XMyzmN3cq-Q

```{prf:definition} Ddeterminant
:nonumber:
   Buď $A\in\mathbb R^{n\times n}$ čtvercová matice řádu $n$.   *Determinant matice $A$* je reálné číslo ${\det A}$   přiřazené matici $A$ následujícím způsobem:

  * Je-li $A$ matice řádu $1$, tj. $A=(a_{11})$, je $\det A=a_{11}$.
  * Máme-li definován determinant z matice řádu $(n-1)$ označme
    symbolem $M_{ij}$ determinant matice řádu $(n-1)$, která vznikne
    z matice $A$ vynecháním $i$-tého řádku a $j$-tého sloupce.
    Definujme *algebraický doplněk* $A_{ij}$
    prvku $a_{ij}$ jako součin $A_{ij}=(-1)^{i+j}M_{ij}$.
  * Konečně, definujme determinant řádu $n$ následovně: zvolíme
    libovolný index $i\in\{1,2,\dots n\}$ a definujeme
    $$
     \det A= a_{i1}A_{i1}+ a_{i2}A_{i2}+\cdots+ a_{in}A_{in}.
    $$
```


Uff. Zacházejme vyjímečně s touto definicí stejně jako s definicí
limity: vezmeme na vědomí, že nějaká korektní definice existuje,
ale učit se ji nebudeme. Není to totiž tak úplně potřeba. bude nám
stačit naučit se několik málo speciálních případů.

Determinant matice $A$ označujeme též $|A|$. Je-li
$A=(a_{ij})$ píšeme zkráceně $|a_{ij}|$ místo $|(a_{ij})|$. K záměně
s absolutní hodnotou může dojít jedině v případě, že matice $A$ je
řádu jedna. V praxi se však obvykle s maticemi řádu jedna nepracuje.

```{prf:definition} Regulární a  singulární matice
:nonumber:
   Buď $A$ čtvercová matice. Je-li $\det A=0$, říkáme, že matice $A$ je *singulární*, v opačném případě říkáme, že je *regulární*.
```


## Determinant matice $2\times 2$ (křížové pravidlo)

$$
    \begin{vmatrix}
      a &b\\ c& d
    \end{vmatrix} =ad-bc
$$

Tento determinant je roven nule právě tehdy, když je jeden řádek
matice násobkem druhého a to bude právě tehdy když je jeden sloupec
matice násobkem druhého.

## Determinant matice $3\times 3$ (Sarusovo pravidlo)

$$    \begin{vmatrix}      a&b&c\\      i&j&k\\      x&y&z    \end{vmatrix} =ajz+bkx+ciy-(cjx+biz+aky)$$

*Mnemotechnická pomůcka:* opsat první dva řádky pod determinant,
vynásobit hlavní diagonálu a dvě diagonály pod tím, potom vynásobit
vedlejší diagonálu a dvě diagonály pod tím. Příspěvky od hlavní
diagonály a dvou šikmých řad pod ní se sčítají, příspěvky od vedlejší
diagonály a dvou šikmých řad pod ní se odečítají.

## Determinant matice ve schodovitém tvaru

```{prf:definition} Schodovitý tvar
:nonumber:
 
  Řekneme, že matice $A$ je ve *schodovitém tvaru*, jestliže
  případné nulové řádky jsou uspořádány na konci matice a nenulové
  jsou uspořádány tak, že každý následující řádek začíná větším počtem
  nul než řádek předchozí.
```


**Příklad.** Matice
$$\begin{pmatrix}  4& 7 &0\\  0 & -2 & 1\\  0& 0& 5\end{pmatrix}$$
je ve schodovitém tvaru.

```{prf:theorem} Determinant matice ve schodovitém tvaru
:nonumber:
 
   Determinant matice, která je ve  schodovitém tvaru je
   roven součinu prvků v hlavní diagonále.
```


Totéž platí zejména pro matice diagonální, které mají nenulové
prvky jenom v hlavní diagonále a tedy jsou ve schodovitém tvaru.

**Příklad.** Platí
$$\begin{vmatrix}  4& 7 &0\\  0 & -2 & 1\\  0& 0& 5\end{vmatrix}=4\cdot (-2)\cdot 5=-40.$$

## Souvislost některých pojmů

Pojmy lineární algebry spolu krásně souvisí. 

```{prf:theorem} Řešitelnost soustavy souvisí s determinantem a inverzní maticí 
:nonumber:
Buď $A$ čtvercová matice řádu $n$. Následující výroky jsou ekvivalentní:

1. K matici $A$ existuje matice inverzní $A^{-1}$.
1. Matice $A$ je  regulární, tj. $\det A\neq 0$.
1. Soustava lineárních rovnic $$AX=B$$ má pro libovolnou pravou stranu $B$ jediné řešení.
1. Homogenní soustava lineárních rovnic $$AX=0$$ má pouze nulové řešení.
1. Každý vektor z $\mathbb R^n$ lze vyjádřit jako lineární      kombinaci vektorů tvořených řádky (sloupci) matice      $A$, a to jednoznačně, až na pořadí.
```

Například je-li $\vec q$ vlastním vektorem matice $A$ příslušným vlastní hodnotě $\lambda$, platí
$$A\vec q=\lambda \vec q.$$
Odsud
$$\begin{aligned}A\vec q-\lambda \vec q&=0\\ A\vec q-(\lambda I )\vec q &=0\\ (A-\lambda I )\vec q &=0\end{aligned}.$$ 
Pokud chápeme poslední rovnost jako soustavu rovnic s koeficienty
$(A-\lambda I)$, nulovou pravou stranou a nenulovým řešením $\vec q$
(tj. bod 4 předchozí věty neplatí), musí být determinant matice
$A-\lambda I$ nulový (tj. bod 2 předchozí věty neplatí). Tím je
motivována následující definice a dokázána následující věta.

```{prf:definition} Charakteristická rovnice, charakteristický polynom
:nonumber:
 Rovnice
$$\det (A-\lambda I)=0$$ s neznámou $\lambda$ se nazývá
*charakteristická rovnice* matice $A$. Výraz na levé straně této rovnice je polynom proměnné $\lambda$ a nazývá se *charakteristický polynom* matice $A$.
```


```{prf:corollary} Vlastní čísla
:nonumber:
 Vlastní čísla matice $A$ jsou právě řešení charakteristické rovnice. Vlastní vektor $\vec u$ příslušný vlastnímu číslu $\lambda$ je nenulové řešení homogenní soustavy rovnic $$(A-\lambda I)\vec u=0.$$
```


<!--

## Transformace matice na diagonální tvar

Ukážeme si postup na jednoduchém příkladě. Pro srovnání je možno postup založený na dosazování do vzorců  shlédnout na [https://www.youtube.com/watch?v=xdxVpC856ms](https://www.youtube.com/watch?v=xdxVpC856ms). V průběhu počítání vyřešíme soustavu dvou rovnic o dvou neznámých. To je úloha známá ze střední školy. Jak opostupovat v komplikovanějších případech, kdy je rovnic více, si ukážeme v další přednášce. V té se budeme zabívat libovolně velkými soustavami rovnic.

**Příklad.**
Odvodíme diagonální tvar tenzoru napětí
$$A= \begin{pmatrix}
  20 & 30 \\ 30 & -10
\end{pmatrix}.
$$
Tím najdeme maximální hodnotu normálového napětí a směr, ve kterém působí.
Charakteristický polynom této matice je
\dm$$\det(A-\lambda I)= \begin{vmatrix}   20-\lambda & 30 \\ 30 & -10-\lambda \end{vmatrix}= (20-\lambda)(-10-\lambda)-30^2=\lambda^2-10\lambda-1100 $$
s kořeny $\lambda_1\approx 38.54$ a $\lambda_2\approx -28.54$. To
budou prvky v hlavní diagonále po transformaci tenzoru.

Pokud budeme chtít vědět, jak jsou nové osy orientovány vůči osám původním, musíme najít i vlastní vektory. Vlastní vektor příslušný hodnotě
$\lambda_1$ je řešením soustavy s maticí soustavy
$$
A-\lambda_1 I\approx
\begin{pmatrix}
  -18.54 & 30 \\
  30  & -48.54
\end{pmatrix}
$$
a nulami vpravo.
Přibližným řešením je vektor $\vec u_1= \begin{pmatrix}
  30 \\ 18.54
\end{pmatrix}$. (Toto plyne z první rovnice, druhá rovnice musí být splněna automaticky, protože jsme použili vlastní hodnotu a soustava musí mít nenulové řešení. Nicméně výpočet je zatížen zaokrouhlovací chybou.) Po vydělení normou vektoru dostáváme
$\begin{pmatrix}
  0.851 \\ 0.526
\end{pmatrix}$.
Druhý vlastní vektor je kolmý, tj. $\begin{pmatrix}
  -0.526 \\ 0.851 
\end{pmatrix}$.
Po transformaci maticí $P= \begin{pmatrix}
  0.851 & -0.526 \\ 0.526 & 0.851
\end{pmatrix}$ [dostáváme (na dvě desetiná místa)](https://sagecell.sagemath.org/?z=eJxtkF1rgzAUhu8F_0OgN4n4kVg2ykCG7A94tV6IjEyzmlkTSeLR_vtZXUthg8DJ4bzvcz52qHVusC9JMk1TfNGjGz9FXOs-mbir21fI5mZ-H94OT8-99b0867kzcsZlmdJwT6uw3NMwYrSqCEI7tFRlLXzvmOWxkCehQNROG_th5Kl1mPgesEzhY8mq66ObazCgJIIzt-4aRbdYViWwBFistOnxIlyVAnSDFEffolHadRr0iBpx7sbFkK5o-ohuzNhe_qLTLII0gfTO_hd9Jxf3tYGFkFYkdoYrO2grNvOafi0sXi9tblewrZ5wQX4_CnMrFY6KbUISsANNBkludYSLRywJ8qBA5Ac7KIR8&lang=sage&interacts=eJyLjgUAARUAuQ==)
$$P^{T}\begin{pmatrix}
  20 & 30 \\ 30 & -10
\end{pmatrix}
P=\begin{pmatrix}
  38.54 & 0 \\ 0 & -28.54
\end{pmatrix}.
$$
To vlastně ani nemusíme počítat, věta v úvodu tohoto slidu zaručuje,
že výsledná matice bude diagonální a bude obsahovat vlastní hodnoty.
Z matice $P$ vidíme sinus a kosinus úhlu pootočení a odsud určíme
snadno, o kolik se souřadná soustava otáčí a v jakém směru.

-->


````{prf:algorithm} Hookův zákon, matice tuhosti a poddajnosti
:class: dropdown

V minulé přednášce jsme odvodili tvar tenzoru malých deformací pro popis deformace tělesa ve tvaru
$$\begin{pmatrix}
        \frac{\partial u_{1}}{\partial x_{1}} & \frac 12\left(\frac{\partial u_{1}}{\partial x_{2}}+\frac{\partial u_{2}}{\partial x_{1}}\right)\\
        \frac 12\left(\frac{\partial u_{1}}{\partial x_{2}}+\frac{\partial u_{2}}{\partial x_{1}}\right)& \frac{\partial u_{2}}{\partial x_{2}}
      \end{pmatrix}$$


<div class='obtekat'>

```{figure} napeti.png
Složky tenzoru napětí charakterizují sílu způsobující deformaci. Zdroj: Wikiepdie.
```

```{figure} wood.jpg
Ortotropie dřeva. Zdroj: researchgate.net, Mathew Legg.
```

</div>

Toto můžeme zapsat symbolicky 

$$\varepsilon_{ij}=\frac 12\left(\frac{\partial u_{i}}{\partial x_{j}}+\frac{\partial u_{j}}{\partial x_{i}}\right).$$ (im*)

Pro deformaci v prostoru máme nikoliv dvě, ale tři souřadnice a tenzor deformací je tedy $3\times 3$ symetrická matice, tj. matice, která má šest nezávislých komponent. (Zbylé tři komponenty dostaneme ze symetrie.) Tyto komponenty dostaneme postupnou volbou indexů ve vzorci {eq}`im*` a můžeme je sestavit do sloupcového vektoru $$(\varepsilon_{11},\varepsilon_{22},\varepsilon_{33},\varepsilon_{23},\varepsilon_{13},\varepsilon_{12})^T$$ Podobně, působící sílu můžeme rozdělit podle působení v jednotlivých směrech a tím dostaneme tenzor napětí, šest veličin charakterizujících napětí. (Zbylé tři jsou dány podmínkou, že se deformované těleso nepohybuje.)
Pro další úvahy složky tenzoru napětí uspořádáme do sloupcového vektoru
$$(\sigma_{11},\sigma_{22},\sigma_{33},\sigma_{23},\sigma_{13},\sigma_{12})^T.$$

Následující poučka je fyzikálně ověřený fakt, že vztah mezi složkami
tenzoru napětí a tenzoru deformace je lineární. To nás nepřekvapí,
protože z přednášek o derivacích na začátku semestru víme, že
**jakákoliv** funkční závislost se dá linearizovat. Podstatné zde však
je, že interval, na kterém má linearizace smysl, není příliš malý,
tj. že tato linearizace platí pro prakticky významné případy.

> **Hookův zákon deformace (volná slovní formulace).** Do určité hranice zatížení je libovolná složka tenzoru deformace úměrná libovolné složce tenzoru napětí.

K tomu si přidejme, že příspěvky k deformaci, způsobené různými složkami tenzoru napětí, se přirozeně sčítají. Matematicky vyjádřeno proto platí
$$ \begin{pmatrix}\varepsilon_{11}\\\varepsilon_{22}\\\varepsilon_{33}\\\varepsilon_{23}\\\varepsilon_{13}\\\varepsilon_{12}\end{pmatrix}    =    S\begin{pmatrix}\sigma_{11}\\\sigma_{22}\\\sigma_{33}\\\sigma_{23}\\\sigma_{13}\\\sigma_{12}\end{pmatrix},$$ kde $S$ je čtvercová $6\times 6$ matice.


Fyzikální úvahy ukazují, že matice $S$ je určitě symetrická a obsahuje celkem ne 36, ale jenom 21 nezávislých
veličin. Nazývá se *matice poddajnosti*. V obecném případě tedy musíme
pro popis deformace mít celkem 21 materiálových konstant. Tento počet
se však výrazně redukuje, pokud je materiál například izotropní nebo
ortotropní. Například ortotropní materiál jakým je dřevo, můžeme
umístit do soustavy souřadnic tak, aby byl invariantní vůči symetrii
podle jednotlivých průměten. Poté je [možné
odvodit](https://en.wikipedia.org/wiki/Orthotropic_material#Stiffness_and_compliance_matrices_in_orthotropic_elasticity),
že nejobecnější možný tvar matice $S$ je
$$ S=    \begin{pmatrix}
  S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\
S_{12} & S_{22} & S_{23} & 0 & 0 & 0  \\
S_{13} & S_{23} & S_{33} & 0 & 0 & 0 \\
0 & 0 & 0  & S_{44} & 0 & 0 \\
0 & 0 & 0  & 0 & S_{55} & 0\\
0 & 0 & 0  & 0 & 0 & S_{66} \end{pmatrix},$$
tj. tvar, obsahující jenom devět materiálových konstant. Odsud vidíme,
že v takovém materiálu se smykové napětí projeví jenom na jedné
komponentě tenzoru deformace, protože poslední tři sloupce, které
udávají složky jednotlivých deformací způsobených napětími
$\sigma_{23}$, $\sigma_{13}$ a $\sigma_{12}$ mají jenom jednu
nenulovou složku.

Pokud bychom použili k popisu obecnou soustavu souřadnic, nebylo by
možné se na symetrii odvolávat. Matice $S$ by obsahovala všechny prvky
a bylo by nutné hledat bázi, v níž je její vyjádření nejjednodušší. U
dřeva je však snadné rozpoznat význačné směry. Když soustavu souřadnic
zvolíme tak, aby byla v souladu s těmito význačnými směry, docílíme
tohot, že obdržíme matici $S$ již přímo ve tvaru s co nejvíce nulami.

Někdy je vhodné umět určit napětí pomocí deformací. K tomu stačí
Hookův zákon vynásobit maticí $S^{-1}$ a obdržíme
$$ \begin{pmatrix}\sigma_{11}\\\sigma_{22}\\\sigma_{33}\\\sigma_{23}\\\sigma_{13}\\\sigma_{12}\end{pmatrix}= S^{-1} \begin{pmatrix}\varepsilon_{11}\\\varepsilon_{22}\\\varepsilon_{33}\\\varepsilon_{23}\\\varepsilon_{13}\\\varepsilon_{12}\end{pmatrix}. $$
Matice $S^{-1}$ se nazývá *matice tuhosti* a označuje $C$. 

Souvislostí vlastních vektorů matice tuhosti a matice poddajnosti
(nebo obecněji souvislostí vlastních vektorů matice a matice inverzní)
se budeme zabývat na následujícím slidu.

````

````{prf:algorithm} Vlastní vektory matice a matice inverzní
:class: dropdown

Fyzikální úvaha snadno vede k závěru, že matice a matice inverzní mají
stejné vlastní vektory. To proto, že pokud v některém směru je
materiálová odezva násobkem podnětu, je i opačně podnět násobkem
materiálové odezvy. To, že matice $A$ a $A^{-1}$ mají stejné vlastní
vektory plyne i z toho, že pokud definiční vztah pro vlastní vektor
matice $A$, tj. vztah 
$$A\vec u=\lambda\vec u,$$ 
vynásobíme zleva maticí $\frac 1\lambda A^{-1}$, dostaneme vzhledem k
identitě $\frac 1\lambda A^{-1}A \vec u=\frac 1\lambda I \vec u =\frac
1\lambda \vec u$ rovnici 
$$\frac 1\lambda \vec u=A^{-1}\vec u,$$ 
která vyjadřuje, že $\vec u$ je vlastním vektorem matice $A^{-1}$ s
vlastním číslem $\frac 1\lambda.$

````

## Shrnutí, hlavní myšlenky

\iffalse

<div class='obtekat'>

```{figure} ../message.jpg
A jaká je hlavní message? Zdroj: pixabay.com
```

</div>

\fi

* Přestože maticový součin nemá všechny vlastnosti na které jsme zvyklí u součinu čísel, jedna vlastnost zůstává: existence "převrácené hodnoty". V případě matic je zobecnění převrácené hodnoty reprezentováno inverzní maticí.
* Pomocí matic je možné transformovat souřadnice bodů, vektorů a tenzorů z jedné soustavy souřadnic do jiné. Inverzní matice poté představuje zpětnou transformaci. 
* Při transormaci tenzorů se snažíme o to, aby po transformaci byl tenzor co nejjednodušší. Pokud použijeme souřadnou soustavu s osami ve vlastních směrech (jsou kolmé a tedy je tato volba smysluplná), je tento tenzor je diagonální s vlastními čísly v diagonále.
* Pro identifikaci vlastních vektorů matice $A$ je nutné řešit soustavu rovnic $$(A-\lambda I)v=0,$$ ve které figuruje jistým i vlastní číslo $\lambda$. Toto umožňuje definovat podmínku na vlastní čísla: uvažovaná soustava musí mít nenulové řešení. 
* Existence nenulového řešení rovnice z předchozího bodu úzce souvisí s pojmem determinantu matice. Přesněji, aby soustava z předchozího bodu měla nenulové řešení, musí mít matice $A-\lambda I$ nulový determinant. 

