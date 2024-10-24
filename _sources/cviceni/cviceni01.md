# Výpočet derivací

>  * Derivaci budeme chápat jako zobrazení, které funkci přiřadí jinou funkci. Proč je tak nesmírně užitečná zjistíme v následujících týdnech.
>  * Naučíte se derivovat jednoduché funkce (mocninné funkce, další základní elementární funkce a složené funkce). Nejsou nutné žádné předchozí znalosti, budete potřebovat pouze vzorce pro derivování a spoustu cviku.
>  * Naučíte se interpretovat derivaci jako rychlost růstu v různých kontextech, kdy veličina závisí na čase, případně na jiné veličině.
>  * Naučíte se ze známého vzorce mezi dvěma veličinami odvodit vzorec dávající do souvislosti rychlosti změn těchto veličin.
>  * [Zde jsou numerické výpočty](https://gist.github.com/robert-marik/9807f45acd8e4c522472749d73bb5b46) k některým příkladům v jazyce Python.

## Základní vzorce.

1. $( c)'=\frac{\mathrm d}{\mathrm dx}( c)=0$
1. $( x^n)'=\frac{\mathrm d}{\mathrm dx}( x^n)=n x^{n-1}$
1. $( e^x)'=\frac{\mathrm d}{\mathrm dx}( e^x)=e^x$
1. $( \ln x)'=\frac{\mathrm d}{\mathrm dx}( \ln x)=\frac 1x$
1. $( \sin x)'=\frac{\mathrm d}{\mathrm dx}( \sin x)=\cos x$
1. $( \cos x)'=\frac{\mathrm d}{\mathrm dx}( \cos x)=-\sin x$
1. $( \mathop{\mathrm{arctg}} x)'=\frac{\mathrm d}{\mathrm dx}( \mathop{\mathrm{arctg}} x)=\frac 1{1+x^2}$

Zde $c\in\mathbb R$ je konstanta a zbytek jsou vzorce,
které platí vždy, když je výraz napravo definovaný.

## Triky, které se často hodí.

1. $\sqrt x=x^{\frac 12}$
1. $\sqrt[k] x=x^{\frac 1k}$
1. $\frac {1}{x^k}=x^{-k}$
1. $\frac {f(x)}c=\frac 1c f(x)$
1. $\frac {c}{f(x)}=c f^{-1}(x)$
1. $a^x=e^{x\ln a}$
1. $\log_ax=\frac{\ln x}{\ln a}$
1. $\sqrt x(x+1)=x^{\frac 32}+x^{\frac 12}$
1. $\frac  {x^3+4}{x^2}=x+4x^{-2}$

## Derivace matematických operací mezi funkcemi

Nechť $f$, $g$ jsou funkce a $c\in\mathbb R$ konstanta. Platí

1. ${\left[cf\right]}'=cf'$
1. ${\left[f\pm g\right]}'=f'\pm g'$
1. ${\left[fg\right]}'=f'g+fg'$
1. ${\left[\frac{f}{g}\right]}'=\frac{f'g-g'f}{g^2}$
1. $\left[f(g(x))\right]'=\frac{\mathrm df}{\mathrm dg}\frac{\mathrm dg}{\mathrm dx}=f'(g(x))g'(x)$

## Výpočet derivace

Určete derivace následujících funkcí, kde $a,b,\mu\in\mathbb{R}$.

1. $f(x)=x^6+\frac 1{x^6}.$
1. $f(x)=x^2+2x+6.$
1. $f(r)=r^3+2r^2-1$
1. $f(x)=3x\sqrt x+9x^5.$
1. $f(x)=1-e^{bx}.$
1. $f(x)=(x^2-1)^4.$
1. $f(x)=\frac{1}{\sqrt \pi}e^{ax^2}.$
1. $f(x)=\frac 1{(x+6)^2}.$
1.  $f(x)=\frac{a}{(\mu x+b)^2}.$

```{prf:example} Řešení
:class: dropdown
:nonumber:

1. $f'(x)=6x^5-\frac{6}{x^7}$
1. $f'(x)=2x+2$
1. $f'(r)=3r^2+4r$
1. $f'(x)=(3x^{3/2}+9x^5)'=\frac 92\sqrt x+45x^4$
1. $f'(x)=-be^{bx}$
1. $f'(x)=4(x^2-1)^32x=8x(x^2-1)^3$
1. $f'(x)=\frac 1{\sqrt \pi} e^{ax^2}2ax$
1. $f'(x)=\frac{-2}{(x+6)^3}$
1. $f'(x)=\frac{-2a\mu}{(\mu x+b)^3}$

```

## Růst ryby

\iffalse 

```{figure} ryba.png
wikimedia.org
```

\fi

Biologové navrhli funkci
$$
    l=0.03937 t^3 - 0.945 t^2 + 10.033 t + 3.073
  $$
  jako model délky jistého druhu ryby, kde $l$ je délka ryby v centimetrech a $t$ je věk v letech.  Vypočtěte derivaci
  $\frac{\mathrm{d}l}{\mathrm {d}t}$. Určete jednotku této derivace a
  slovní interpretaci hodnoty derivace v bodě $t=12$.

_Upraveno podle Stewart, Day: Biocalculus. Calculus for the life siences. V tomto příkladě se setkáváme s klasickou interpretací derivace jako rychlosti změny, tj. hodnoty o kterou se změní závislá veličina, když se nezávislá veličina změní o jednotku._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Jednotka derivace délky podle věku je stejná, jako bychom délku dělili věkem. Tedy $\left[\frac{\mathrm dl}{\mathrm dt}\right]=\mathrm{cm}/\mathrm{rok}$, tj. centimetr za rok. 

Derivace je rychlost změny. Pokud derivujeme délku ryby podle času, je derivace rychlost s jakou se mění délka ryby v čase. Převedeno do srozumitelnějšího jazyka to je možné elegantněji vyjádřit tak, že derivace udává (v centimetrech za rok) okamžitou rychlost růstu ryby, přičemž velikost ryby vyjadřujeme její délkou (a ne například hmotností).

Zadaná funkce vyjadřující závislost délky na čase je polynom. Použitím pravidel pro derivování je snadné ukázat, že pro derivaci délky podle času platí $$\frac{\mathrm dl}{\mathrm dt} =3\cdot 0.03937 t^2 - 2\cdot 0.945 t + 10.033 =  0.11811 t^2 -1.89 t + 10.033$$   a pro $t=12\,\mathrm{let}$ dostáváme  $$    \frac{\mathrm dl}{\mathrm dt}\Bigr\vert_{t=12} =4.4\, \mathrm{cm}/\mathrm{rok}.   $$   Dvanáctiletá ryba roste rychlostí přibližně $4.4$ centimetrů za rok, tj. mezi dvanáctým a třináctým rokem vyroste přibližně o $4.4$ centimetru. (Slovo přibližně je použito proto, že derivace je okamžitá rychlost růstu a není zaručeno, že tato rychlost se udrží po celou jednotku času, tj. po celý rok.) 

* <a href="https://sagecell.sagemath.org/?z=eJx1jM0KgkAUhfeC73ChhX81jE0hLtz1AC1aB5MzojjNjZnRsKdPUyGCzupw-M7nip6bMHBBBGs2cDZ4l1pzcFsoufU9FbqooISynGWxu7IdJfnhOLZ9kk4zi13CCM3YeD5J1XIww23wPVvjM5zO3_ZLY1t4GIQWtTOoOt8T0jQ9L2WhiGiqKozgI5rHRbMys23RiD9Muh-hHwYsCLT8JTV2UKPQ6LB7AzQ9S-8=&lang=sage&interacts=eJyLjgUAARUAuQ==">Sage výpočet</a>
* <a href="https://sagecell.sagemath.org/?z=eJyFUs1uozAQviPxDhN6MQmhJuyqalVuvfXQS29VN3LAERY_RsZpS96pT9EXq8fghG2r3TnYZr4fz4zRNEs2vlcTHWY0pul1erXUf9I1ja9__TanzSrBdLrUqzSmVylcwB2vKwZq2A2-15fylaA4hP_EBTyKvoJOSahkq5WsD75XKVkNkMFTQqMkonESgbltXN122mfxQ2rMP_ueGvKylr0W6Gu-89JUOp1LWbQy563DCq7EC8u5-azjQuz3JCQ60zQE2-cI-t5eKsBSQbR2H25mbd0jgG0xs7yJhuUCZMWao9AczsV0spEGmSXUoeGqNfboU-BQt53cHhve2nqIpiu8LPyLoHhhKfIwcdYzDgLM5L-Yrb-LR74rxkhG6SWQzXJmeKo2Zl3H24K4xITjbPFCtuvJaZZr-IE1OAcrmQCxnxxu7bPfjFmM00M5WfBwH0wqXvf8n9TFYuG4GL6n2e6A_6yZmOg1OYoOiH3H6NxhNJYZnf3C0CprTia9wTgzbW6VfM2eAnQIokAWJSvAdR9EENie8OCsPt6D5_ATIrP-Bw==&lang=sage&interacts=eJyLjgUAARUAuQ==">Sage numerický odhad</a> s ilustrací toho, že výsledek se dá odhadnout u použitím základních aritmetických operací, ale že délka kroku nemůže být ani moc krátká ani moc dlouhá. </a>

```

## Bazální metabolismus

\iffalse

```{figure} kolibrik.jpg
pixabay.com
```

\fi

Bazální metabolismus $M$ (ve wattech) souvisí s hmotností $W$ vztahem
$$M=AW^n,$$ kde $n$ je pro mnoho živočišných druhů blízké číslu $0.75$ a
$A$ je konstanta, která je specifická pro daný druh a v rámci daného
druhu klesá s věkem. Určete derivaci $$\frac{\mathrm d M}{\mathrm dW}$$
a určete i fyzikální jednotku a slovní interpretaci této derivace.

_Zpracováno podle Monteith, Unsworth: Principles of Environmental Physics. Tady je opět klasická interpretace derivace jako rychlosti změny. Rychlost změny ale nemusí být jenom klasické chápání rychlosti jako závislosti na čase. Derivace vyjadřuje, jak závislá veličina reaguje na změny nezávislé veličiny. Pro pochopení, co derivace vyjadřuje, hraje velkou roli i jednotka této derivace. Označení je ponecháno z původní literatury, mimo jiné $M$ není hmotnost a $W$ není watt. Vztah je v literatuře znám jako Kleiberův zákon. Vysvětluje se pomocí něj rozdílná délka života různých živočišných druhů._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Pro výpočet si stačí uvědomit, že funkce je konstantním násobkem mocninné funkce a umíme ji tedy zderivovat podle pravidla pro derivaci konstantního násobku a pravidla pro derivaci mocninné funkce. Derivace je $$\frac {\mathrm dM}{\mathrm dW}=\frac {\mathrm d}{\mathrm dW}(AW^n)=nAW^{n-1}$$ podle pravidla pro derivaci konstantního násobku a pro derivaci mocniny. Jednotka derivace je stejná, jako bychom místo derivování dělili, tj. watt na kilogram, $$\left[\frac {\mathrm dM}{\mathrm dW}\right]=\frac{\mathrm W}{\mathrm {kg}}.$$ Derivace udává rychlost, s jakou se projeví změna hmotnosti na bazálním metabolismu. Je to nárůst bazálního metabolismu způsobený nárůstem hmotnosti a přepočtený na jednotkovou změnu hmotnosti. Přibližně také změna bazálního metabolismu ve wattech při změně hmotnosti o kilogram u velkých živočichů nebo v miliwatech při změně hmotnosti o gram u drobných živočichů. Například u malých ptáčků nemá smysl uvažovat nárůst hmotnosti o kilogram a pro interpretaci raději přejdeme k jednotkám tisíckrát menším.
```

## Mezní náklady (marginal cost)

\iffalse 


```{figure} airbus.jpg
wikimedia.org
```

\fi

Náklady na produkci $x$ letadel za rok jsou (v milionech
Euro) dány funkcí
$$C(x) = 6 + \sqrt{4x + 4},\qquad  0 \leq x \leq 30.$$
Platí $C'(15)=0.25$. Určete, jakou tato derivace má slovní
interpretaci a určete i jednotku této derivace.

_Toto je jedna z nejrozšířenější aplikací derivací mimo přírodní vědy. Zajímáme se o to, jak rychle rostou ekonomické veličiny, protože ekonomika je za vším. Veličiny, které v ekonomii získáváme derivováním, obsahují zpravidla slovo "mezní", nebo též "marginální". Podle Wikipedie nastupující technická revoluce nazývaná Průmysl 4.0 přinese výrobu s velmi malými mezními náklady. Tedy derivace nákladů na výrobu podle množství vyrobeného zboží bude malá. To odpovídá představě výroby v robotizovaných halách, kde hlavním nákladem je vybudování výrobního zařízení._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Jednotka derivace $C'(x)$ je $\mathrm{milion\ Euro}/\mathrm{kus}$, resp. 
$\mathrm{milion\ Euro}/\mathrm{letadlo}$, resp. milion Euro, podle toho, jak nazveme jednotky v nichž měříme počet letadel.

Derivace $C'(15)$ vyjadřuje rychlost, s jakou rostou náklady při produkci $15$ letadel. Je to cena vztažená na jednotkový přírůstek, tj. jedná se vlastně o cenu výroby šestnáctého letadla. Šestnácté letadlo má výrobní náklady 0.25 milionů euro.

*Poznámka 1:* Jinou cestou jak určit cenu šestáctého letadla je použít rozdíl $$C(16)-C(15)\approx 0.246.$$ Toto je cesta, která se zdá výhodnější, protože není nutné derivovat. Ale tato cesta zpravidla vede ke složitějším postupuům, jakmile tento výpočet vstupuje jako jedna z komponent do složitějšího modelu. Odhad ceny dalšího letadla při produkci $x$ letadel je bez derivace roven
$$C(x+1)-C(x)=\sqrt{4(x+1)+4}-\sqrt{4x+4}$$ a s derivací
$$C'(x)=\frac{2}{\sqrt{4x+4}}.$$ Ve druhém případě máme zlomek s konstantním čitatelem (vlastně se jedná o mocninnou funkci s exponentem $-\frac 12$), v prvním případě máme rozdíl dvou odmocnin. Druhá metoda tedy vede k jednodušší funkci a tato jednoduchost může být kriticky důležitá, pokud námi odvozená cena dalšího letadla vstupuje do dalšího výpočtu. 

*Poznámka 2:* Možná jste si vzpomněli na příklady z nižších škol týkající se přímé úměrnosti. Jsou to příklady typu "Za výrobu patnácti jachet ruský oligarcha zaplatí částku $C$. Kolik zaplatí za šestnáct jachet?" Takové příklady jsou založeny na předpokladu, že výroba každé jachty stojí stejně a cena je nezávislá na počtu. V takovém případě je možné řešit úlohu trojčlenkou, pomocí přímé úměrnosti. V takové situaci by závislost ceny na množství byla lineární. V praxi tomu tak ale často není, závislost je nelineární. Proto není možné použít úměrnost a proto mají v ekonomii místo i veličiny jako [mezní náklady](https://cs.wikipedia.org/wiki/Mezn%C3%AD_n%C3%A1klady), které jsme vypočítali v tomto příkladě pomocí derivace. Slovo "mezní" je odvozeno od skutečnosti, že tato veličina pomáhá určit mez množství výroby, kdy se zvýší cena za jednotku

```

## Vzdálenost k horizontu

\iffalse 

```{figure} horizont.jpg
pixabay.com
```

\fi 

Vzdálenost k horizontu pro pozorovatele ve výšce $h$ nad Zemí je dána funkcí $H=\sqrt {2Rh},$ kde $R=6.371\times 10^6\,\mathrm m$ je poloměr Země ([viz zde](https://aty.sdsu.edu/explain/atmos_refr/horizon.html)). Po dosazení a vydělení faktorem 1000, aby $H$ vycházelo v kilometrech, dostáváme vzorec $$H=3.57\sqrt{h},$$ kde $h$ je v metrech a $H$ v kilometrech. Určete hodnotu této derivace $\frac{\mathrm d H}{\mathrm dh}$ pro $h=5\,\mathrm{m}$ (včetně jednotky) a slovní interpretaci této derivace.

_Tento příklad opět udává derivaci jako rychlost změny, ale nezávislá proměnná není čas. Sledujeme vzájemnou relaci dvou délek - vzdálenosti k horizontu a výšky pozorovatele. V případech jako je tento je rozměr veličiny derivované stejný, jako rozměr veličiny, podle které se derivuje. Potom je derivace vlastně bez rozměru. Někdy je však vhodné pro srozumitelnější interpretaci jednotky nevykrátit, obzvlášť v případě jako zde, kdy se obě délky udávají v řádově jiných jednotkách (metry versus kilometry)._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Pro $H=3.57\sqrt h$ platí $$\frac{\mathrm dH}{\mathrm dh}=\frac 12 \times 3.57 \times \frac {1}{\sqrt h}$$ a numericky
$$\frac{\mathrm dH}{\mathrm dh}(5)=\frac{3.57}{2\sqrt 5}\approx 0.7983 \frac {\mathrm{km}}{\mathrm m}\approx 0.8 \frac {\mathrm{km}}{\mathrm m}.$$ Vzdálenost k horizontu pro pozorovatele ve výšce $5$ metrů roste rychlostí 0.8 kilometru na každý metr výšky navíc. Toto je interpretace pro praktické využití. Kromě toho se jednotky dají upravit a ve skutečnosti derivace žádný fyzikální rozměr nemá
$$\frac{\mathrm dH}{\mathrm dh}(5)=0.7983 \times \frac {1000\, \mathrm{m}}{\mathrm m}=798$$ a každá změna výšky pozorovatele se na vzdálenosti k horizontu projeví svým $800$-násobkem.

<a href="https://sagecell.sagemath.org/?z=eJwtzEEKwjAQheG94B0GXDSRko0UV9256DViMmGGtBNNmkA9vUFcPv6PR3OzWQ00aLjAA-Nqs3UIr5w2FMHzaVGk55uZ7tfyznsf8IOBhbsLVaLrynMIahlJm1KfRdE8aSPqbzO3_jmCT8V-UBgoeUn7ARakbj27iNAOx2Xt9Qvbki8M&lang=sage&interacts=eJyLjgUAARUAuQ==">Sage výpočet</a>

```

## Rychlost s jakou roste obsah kruhu

\iffalse 

```{figure} vate_pisky.jpg
J. Kameníček, brnensky.denik.cz
```

\fi

Váté písky je bezlesý
pruh podél železniční trati nedaleko Bzence, kde je extrémní sucho
(Moravská Sahara). V dřívějších dobách byly v pruhu podél železnice velmi časté
požáry kvůli provozu parních vlaků. Předpokládejme, že požár se v této
vysušené oblasti šíří ve tvaru kruhu. V určitém okamžiku je poloměr $50$
metrů a roste rychlostí $1.5$ metrů za minutu. Zapište zadání pomocí
derivací a určete jak rychle roste plocha zasažená ohněm.

_V tomto příkladě se učíme, že ze znalosti vztahů mezi veličinami můžeme odvodit vztah, mezi rychlostmi změn, tj. do statických vzorců můžeme dodat dynamiku vývoje. V praxi někdy jde příklad tohoto typu obejít úvahou: teď je poloměr 50 metrů, tomu odpovídá jakási plocha, za minutu  bude poloměr 51.5 metru, tomu odpovídá opět jakási plocha a porovnáním s plochou původní snadno zjistím přírůstek. To pro nás může být kontrola, že aparát funguje. Pro nás je teď důležité naučit se tento aparát na malých věcech, abyste mohli později dělat věci velké._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Je zadán vztah mezi dvěma veličinami a pro jednu z těchto veličin známe její hodnotu derivaci podle času. Máme za úkol určit derivaci podle času druhé z veličin.

Ze zadání známe poloměr $r=50\,\mathrm{m}$ a rychlost růstu poloměru $\frac {\mathrm dr}{\mathrm dt}=1.5\,\text{m}\,\text{min}^{-1}$. Zajímá nás rychlost růstu obsahu $\frac{\mathrm dS}{\mathrm dt}$.

Derivováním vztahu $$S=\pi r^2$$ podle $r$ získáváme $$\frac {\mathrm dS}{\mathrm dr}=2\pi r.$$ Derivováním podle $t$ dostaneme
$$\frac{\mathrm dS}{\mathrm dt} = \frac{\mathrm dS}{\mathrm dr}
\frac{\mathrm dr}{\mathrm dt}= 2\pi r \frac{\mathrm dr}{\mathrm dt}$$
a numericky
$$\frac{\mathrm dS}{\mathrm dt} = 2\pi \times 50 \times 1.5 \approx 471 \,\mathrm{m}^2\,\text{min}^{-1}.$$

<a href="https://sagecell.sagemath.org/?z=eJx1UjtPwzAQ3iPlP5zoQIKiCpAYvbGDhFhAIF1tl7hJfJUfgeTXc2niFhXIFPk-f6_zCp5bqhGc9gZiQ20FjRpg5ynCiArtAHtqqdMOGhfrCAwdZN2SD-CiDxEC1RQooeIa8mwFz8ykO9hpiE6acH6HNh7rmGd5FkSPrrgMlyWcfSt4dMxoLUKoQKLPMye20cpgyBYX7qKy6D68uCln8OLSwQ4bAgY2UrMBZTXsZyKdZ09FKMXewBUUjn_L99uT3MNkakn5kyMlq45NjNgbroudsS1m9TV9FhP1HyFeaONwNN3BBTRkg6P22G0_ktPyMKKT_FTMKdGvxpMh6HBnZiYNNSlLYcgzRR5HbY14nRIKcXddKbPdHvJW08HN-u5t8Zyw5ax4r53pkSPP-2Eh1eopI2f_Z4NquSIOGk-zRmJfZomdxdRUhCJIo1_uk4xIiLWPG39u9MWkUvtxTzJoy8_16BDZeJh2z-3YyE0Z2fAcuWX5ZTqUhvW9DsbaoQNpPD_VxXLiSBHs6aT8BnG_DrA=&lang=sage&interacts=eJyLjgUAARUAuQ==">Sage výpočet</a> (v tomto jednoduchém případě spíše jako ukázka zápisu, než jako nástroj pro urychlení výpočtu)

```

## Sůl nad zlato

\iffalse 

```{figure} kopec_soli.jpg
Že je u koule objem úměrný třetí mocnině poloměru vidíme přímo ze vzorce. Nejinak to je u těles, které si zachovávají proporce, tj. vzniknou zvětšením či zmenšením z jediného vzoru. Typickým příkladem je kromě koule i kužel s pevně zadaným vrcholovým úhlem. Tento tvar zachovávají volně sypané materiály. Obrázek: pixabay.com
```

\fi 

V pohádce _Sůl nad zlato_ sype Maruška z bezedné slánky sůl na hromadu soli ve tvaru kužele, který roste tak, že objem je v každém okamžiku svázán s výškou vzorcem $$V=\frac 14h^3.$$ Výška je $0.5$ metru a vydatnost solničky $10$ litrů (tj. $0.01$ krychlových metrů) soli za minutu. Určete, jak rychle roste hromada soli do výšky.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Je zadán vztah mezi dvěma veličinami a pro jednu z těchto veličin známe její hodnotu derivaci podle času. Máme za úkol určit derivaci podle času druhé z veličin.

Podle zadání je $\frac{\mathrm dV}{\mathrm dt}=0.01$ krychlových metrů za minutu, $h=0.5$ metru a chceme znát $\frac{\mathrm dh}{\mathrm dt}$. Derivováním dostáváme
$$\frac{\mathrm dV}{\mathrm dt} = \frac{\mathrm dV}{\mathrm dh} \frac{\mathrm dh}{\mathrm dt} = \frac 34 h^2 \frac{\mathrm dh}{\mathrm dt}.$$
Odsud
$$\frac{\mathrm dh}{\mathrm dt} = \frac 43 \frac{\mathrm dV}{\mathrm dt} \frac 1{h^2}$$
a po dosazení
$$\frac{\mathrm dh}{\mathrm dt} = \frac 43 \times 0.01 \times \frac 1{0.5^2} \,\mathrm{m}\,\mathrm{min}^{-1}=0.053 \,\mathrm{m}\,\mathrm{min}^{-1}.$$
Hromada roste do výšky rychlostí 5.3 centimetru za minutu.

<a href="https://sagecell.sagemath.org/?z=eJx9kk2P0zAQhu-R8h9Gu4dNUFRaAUff9sANxKEHqoLceLp2k9iV7RjFvx7HH0u3AnLKfD3zzowtcVQ3T_aphbvvEb5qNaGUFGwHPTV1xcl5lr0VSjYP_KGTVL8Ysmtj8n4xA4ULHRSEpKFHuCCTCNcEwbra31Tv76q_nC44_bdaKydFj2Tf2JaQ3fuP8A4aHoz2x4ci-FvKgQm9ABWRFFwQpuZb9iTWcea6Mlz9albgX4b_rk6aejFFDTAoabUaZ_CUUbmA80pjH0Nrm7qqq0f4rJhUdolepgz1KEX4gSy9roqTHHicYrv5tO2YOJ-jiC65trtjVlbS24R_Ri0cDeNlHlwVGzGPwnKQRFzOCMSCyuGM2i8azaquoJznI7KwrwFyqgD-pkEqIEaNDl9x3SG240n98R_0DrJ9mhmCQS_p1IFHGCxq5Aqm2ayLDpfCEQerHLWwgq6aunA6YzWVc7DcjWJfSHMXOUt4MbnPlIdOVhDF-E9mSTIP2-NGc9O8bmaNlQ2HhbNVSThaGTFdHIGn44ZFLD0flbEkVm7MfDL3l_rzdpy3lKf3WOomUeRlR_sb5Qknag==&lang=sage&interacts=eJyLjgUAARUAuQ==">Sage výpočet</a> (v tomto jednoduchém případě spíše jako ukázka zápisu, než jako nástroj pro urychlení výpočtu)

```
	
## Rychlost s jakou roste obsah kruhu II

\iffalse 

```{figure} kyjov.jpg
http://mp.mestokyjov.cz/
```

\fi

Město má přibližně tvar kruhu o poloměru $10\,\mathrm{km}$ a žije v něm $300\,000$ obyvatel. Jak rychle musí růst poloměr kruhu (velikost
města), pokud počet obyvatel roste rychlostí $10\,000$ obyvatel za rok
a chceme udržet stejnou hustotu osídlení?

_Toto je mírná modifikace příkladu s požárem. Protože město má konstantní hustotu osídlení, jsou počet obyvatel i rozloha přímo úměrné a je to podobné, jako bychom jednu veličinu vyjadřovali ve dvou různých jednotkách._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Ze zadání: $r=10\,\mathrm{km}$, $N=300\,000$, $\sigma=\frac{N}{\pi r^2}$ je hustota osídlení a ta je konstantní, $\frac {\mathrm dN}{\mathrm dt}=10\,000 \,\text{rok}^{-1}$. Zajímá nás $\frac{\mathrm dr}{\mathrm dt}$.

Výpočet: Pro počet obyvatel platí $N=\sigma \pi r^2$ a derivováním $$\frac{\mathrm dN}{\mathrm dt} = \frac{\mathrm dN}{\mathrm dr}\frac{\mathrm dr}{\mathrm dt}=\sigma \pi 2r\frac{\mathrm dr}{\mathrm dt}.$$ Odsud
$$
\frac{\mathrm dr}{\mathrm dt}=\frac 1{2\pi r\sigma}\frac{\mathrm dN}{\mathrm dt}
$$
a protože $\pi r\sigma=\frac Nr$, máme
$$
\frac{\mathrm dr}{\mathrm dt}=\frac {r}{2N}\frac{\mathrm dN}{\mathrm dt}=\frac {10}{2\times 300\,000}\times 10\,000=0.166 \,\mathrm{km}\,\mathrm{rok}^{-1}\approx 170\,\mathrm m\,\mathrm{rok}^{-1}
$$

Existuje ještě poněkud přímočařejší, ale na provedení mírně náročnější postup, protože je nutné derivovat podíl funkcí. Zderivujeme přímo definiční vztah pro hustotu osídlení $\sigma=\frac{N}{\pi r^2}$ podle času. Vlevo je derivace konstanty, tj. nula, vpravo derivace podílu. Proto
$$0=\frac{\frac{\mathrm dN}{\mathrm dt} \pi r^2 - N2\pi r\frac{\mathrm dr}{\mathrm dt}}{(\pi r^2)^2}$$
a odsud
$$\frac{\mathrm dN}{\mathrm dt} \pi r^2 - N2\pi r\frac{\mathrm dr}{\mathrm dt}=0.$$
Nyní osamostatníme derivaci poloměru a dostaneme
$$
\begin{aligned}
\frac{\mathrm dN}{\mathrm dt} \pi r^2 &= N2\pi r\frac{\mathrm dr}{\mathrm dt}\\
\frac{\mathrm dr}{\mathrm dt} &= \frac{\mathrm dN}{\mathrm dt} \frac r{2N} 
\end{aligned}
$$
a výsledek je stejný jako v předchozím postupu.

```


