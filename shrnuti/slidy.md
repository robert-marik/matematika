# Shrnutí za předmět Matematika

(Tato kapitola není k dispozici v PDF formátu.)

\iffalse

Stránka obsahuje dva způsoby shrnutí. Jednak z hlediska aplikací a jednak z hlediska matematického aparátu.

<style>
h2 {clear:both;}
</style>

## Matematika a dřevo/půda/příroda/materiál

### Hookův zákon v 1D nebo pro izotropní materiál

<div class='obtekat'>

```{figure} beam.png
Tříbodový ohyb dřevěného nosníku. Barevně je znáronběno napětí podél nosníku, tj. v podélném směru dřeva. Jdou vidět části s tlakovým a tahovým namáháním v tomto směru. Výstup z programu ANSYS, autor modelu J. Milch, LDF MENDELU.
```

</div>

Hookův zákon umožňuje vyhodnotit, jaká __tvarové změny jsou vyvolány působením vnější síly__ na těleso z materiálu podléhajícího deformaci. Naopak umožňuje také určit, jaké __vnitřní napětí nastává u materiálu vystaveného deformaci__.

Napětí $\sigma$ v materiálu při mechanickém namáhání relativní deformací $\varepsilon$ je dáno vztahem $$\sigma = E\varepsilon,$$ kde $E$ je Youngův modul pružnosti.

* Zákon vyjadřuje přímou úměrnost mezi deformací a napětím.
* Jedná se o lineární aproximaci obecného vztahu. Proto je problematické použití tohoto zákona pro velké deformace. Nicméně na naprostou majoritu aplikací je tato lineární aproximace dostatečná a kdybychom ji neučinili, nespočítáme ve statice skoro nic.
* Funkce $\sigma(\varepsilon)=E\varepsilon$ je lichá funkce proměnné $\varepsilon$, předpokládá __stejné chování v tahu a tlaku__. (Ve skutečnosti pro dřevo neplatí ani pro malé deformace, odtud je poté spousta problémů při přenesení ``strojařských'' výsledků na dřevo.)

### Darcyho zákon 

<div class='obtekat'>

```{figure} darcy.jpg
Hydraulická hladina v hornaté oblasti. Zdroj: http://geologylearn.blogspot.com/2015/12/groundwater-flow.html
```

</div>

Darcyho zákon je vztah mezi hydraulickým gradientem (hnací síla dávající do pohybu vodu v půdě) a filtračním tokem. Umožňuje modelovat, __jakým směrem a jakou rychlostí prosakuje voda porézní zeminou__. Umožňuje posuzovat hydraulické poměry v půdě, je důležitý pro hospodaření s vodou (kolik je vody v půdě a kterým směrem teče) i pro __ochranu vodních zdrojů__ (ve vnitrozemí ochrana před __znečištěním__, v přímořských státech i ochrana před __průnikem mořské vody do zdrojů vody pitné__). 

Jako všechny materiálové vztahy, je analogický Hookovu zákonu. Často se vyjadřuje pomocí podílu, [například na Wikipedii](https://cs.wikipedia.org/wiki/Darcyho_z%C3%A1kon). To je nejjednodušší formulace. Pokud hydraulický gradient není konstantní, není možné použít tuto jednoduchou formulaci a je nutné použít formulací pomocí [gradientu](https://en.wikipedia.org/wiki/Darcy%27s_law). V jednorozměrném případě se jako obvykle gradient redukuje na derivaci podle prostorové proměnné.

### Fourierův zákon v 1D nebo pro izotropní materiál 

<div class='obtekat'>

```{figure} panel.jpg
Ukázka sendvičové konstrukce, Tepelný odpor se počítá stejně jako v elektrotechnice elekrický odpor. Vidíme analogii sériového (materiály 1, 6, ...) i paralelního (materiál 2 nebo 4 a k nim  paralelně dřevo nad a pod) zapojení. Zdroj: https://www.rdrymarov.cz/
```

</div>

Fourierův zákon umožňuje __přepočet rozdílu teplot na teplotní tok nebo tepelné ztráty__. Jedná se o vztah mezi teplotním gradientem (hnací síla dávající do pohybu energii v materiálu) a tokem tepla. Analogický Hookovu a Darcyho zákonu, jako ostatně všechny materiálové vztahy aproximované lineární funkcí.
Fourierův zákon se často vyjadřuje pomocí podílu, [například na Wikipedii](https://cs.wikipedia.org/wiki/Tepeln%C3%A1_vodivost#V%C3%BDpo%C4%8Det_tepla_p%C5%99edan%C3%A9ho_veden%C3%ADm). To je nejjednodušší formulace. Pokud teplotní gradient není konstantní (tok není homogenní), není možné použít tuto jednoduchou formulaci a je nutné použít formulací pomocí [gradientu](https://cs.wikipedia.org/wiki/Fourier%C5%AFv_z%C3%A1kon). V jednorozměrném případě se jako obvykle gradient redukuje na derivaci podle prostorové proměnné.

V případě __sendvičových materiálů__ se využívá analogie mezi různými materiálovými vztahy, nejčastěji podobnost s Ohmovým zákonem. Tepelný odpor různých částí stěny se chová stejně jako paralelně či sériově zapojené rezistory. Protože teorie elektrických obovodů je dobře prozkoumána, přenáší se vzorce, označení a někdy i terminologie z elektrotechniky do stavební fyziky. Matematické zdůvodnění této analogie mezi různými materiálovými vztahy je, že se vždy jedná o __lineární aproximaci reálné reakce materiálu__ na vnější podněty. 

### Rovnice vedení tepla v 1D

Rovnice vedení tepla je model zahrnující efekt nerovnoměrného rozdělení teploty (dává do pohybu teplo podle Fourierova zákona) a změny v intenzitě toku tepla (například zeslabení toku tepla znamená, že energie se ukládá do materiálu a to se projeví se změnou teploty v daném místě). V jednodimenzionálním povedení umožňuje modelovat __prostup tepla stěnou__, například __postupné ohřívání stěny__ a její vyrovnávání se s okolními podmínkami.

Rovnice vedení tepla dokáže modelovat nestacionární děj. Proto je možné ji použít například k výpočtu vlivu __akumulační příčky__ na tepelnou pohodu ve dřevostavbě, což může ovlivnit jednu z nevýhod dřevostaveb (velmi malá akumulace), případně zlepšit pohodu v permanentně přehřátých podkrovních bytech. 

### Rovnice vedení tepla ve 2D nebo 3D

Rozšíření rovnice vedení tepla pro vícerozměrný případ. Umožňuje zmapovat tok tepla a teplotu při proudění energie v krajině, ve městě, v konstrukčním prvku dřevostavby. Tím je možné analyzovat například vliv __tepelných ostrovů v krajině__, nebo vliv __zeleně na teplotní komfort ve městech__.

### Hookův zákon pro ortotropní a anizotropní materiál

<div class='obtekat'>

```{figure} wood_growth.jpg
Anatomické směry dřeva výrazně determinují vlastnosti v jednotlivých směrech. V podélném směru je podstatně vyšší pevnost (modul pružnosti), ale i součinitel tepelné vodivosti a difuzní koeficient. V příčných směrech je vyšší například koeficient bobtnání. Zdroj: https://en.wikipedia.org/wiki/File:Wood_growth_ill.jpg
```

</div>

* Napjatost a deformaci a v jednotlivých směrech vyjadřujeme tenzorem napětí a tenzorem deformace. Tenzory jsou z matematického hlediska matice, na které jsou naloženy jisté další podmínky (transformují se tak, aby dávalo smysl ve fyzice).
* Na rozdíl od 1D nebo izotropního případu má materiál více parametrů: moduly pružnosti v tahu/tlaku/smyku pro jednotlivé směry a způsoby namáhání, což jsou ve 3D tři směry a tři roviny pro smykové namáhání. Dále Poissonova čísla dávající do relace namáhání v jednom směru a odezvu v jiném směru.
* Využíváme maticový součin a matici rotace. Díky nim umíme transformovat napětí do otočených souřadnic: posouzení namáhání lepených šikmých spojů, namáhání trhlin. Transformace se provádí nasobení maticí rotace z jedné strany a inverzní maticí z druhé strany. Všimněte si, že u komutativní operace by takový postup neměl vůbec smysl: odpovídalo by to například násobení pěti a jednou pětinou - operace by se vyrušily. Díky komutativitě však k vyrušení nedojde a máme k ruce nástroj na transformaci tenzorů, například působících napětí.
* Podobně je možno formulovat tenzorově i další materiálové vztahy: Fourierův zákon, Darcyho zákon.
* Matice vyjadřující materiálové vlastnosti jsou diagonální, pokud jsou souřadné osy zvoleny ve vlastních směrech. U ortotropních materiálů jsou tyto vlastní směry určeny rovinami symetrie. U dřeva se jedná o anatomické směry dřeva (podélný, radiální, tangenciální). 

### Rovnice exponenciálního růstu/poklesu

<div class='obtekat'>

```{figure} kava.jpg
Příklad konvergence ke stacionárnímu stavu rychlostí úměrnou vzdálenosti od tohoto stacionárního stavu. Právě zalité kafe se ochladí o prvních pět stupňů rychle, protože je velký rozdíl mezi teplotou nápoje a okolí. Tepelná výměna je proto intenzivní. Jak se teploty slibžují, rychlost klesá.
```

</div>

Mnoho dějů spějících k rovnováze probíhá rychlostí úměrnou vzdálenosti od rovnovážného stavu. Příkladem je [Newtonův zákon ochlazování](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling) nebo [von Bertalanffyho model růstu](https://cs.wikipedia.org/wiki/Ludwig_von_Bertalanffy). To vede k tomu, že měnící se veličina se k rovnovážnému stavu přibližuje. Tím klesá vzdálenost od rovnovážného stavu a rychlost růstu se zpomaluje. Přesná analýza (vyřešení příslušné diferenciální rovnice) ukazuje, že veličina se blíží asymptoticky k rovnovážné poloze a vydálenost od rovnovážné polohy klesá jako klesající exponenciální funkce (exponenciální funkce $y=e^{-kx}$ kde $k>0$). 

Naopak růst úměrný množství je, na rozdíl od předešlého, prudký a stále se zrychluje. Tento růst je exponenciální ($y=e^{kx}$, kde $k>0$), pro malé hodnoty roste pomalu, ale později je velmi prudký. Exponenciální funkce roste nejrychleji ze všech základních elementárních funkcí. Například ani mocnina se sebevětším exponentem neroste tak rychle. Nepříliš známým ale nám blízkým zařízením ilustrujícím rychlost růstu exponenciální funkce je třecí brzda níže.

#### Capstan equation -- třecí pásová brzda, spouštěcí buben

<div class='obtekat'>

```{figure} buben.jpg
Třecí brzda jako spouštěcí buben. Dostatečné obtočení lana okolo tyče způsobí, že s malou námahou udržíme obrovskou sílu.  Zdroj: https://www.skyman.cz/nabidka/arboristika/spousteni-bremen/bubny-a-kotvy/spousteci-buben-tu100-2-popruhy-2958.html
```

</div>

Lano se omotává okolo válce a třením se brzdí. Efekt je velmi silný protože [růst tahu je úměrný tomuto tahu](https://user.mendelu.cz/marik/am/slidy/cviceni/cviceni09.md.html#p%C3%A1sov%C3%A1-brzda). 

* Omotáním lana o čtvrtotočku na dřevěném kůlu dosáhneme silného brzdícího účinku.
* Omotáním lana o půlotočku dosáhneme ještě násobně většího brzdícího účinku ve srovnání se čtvrtotočkou, vyzkoušejte si. 
* Omotáním okolo dřevěného kůlu dvakrát ubrzdíme prakticky cokoliv, co nevyvrátí tento kůl nebo nepřetrhne lano. 

Při použití hladkého válce je potřeba více otáček -- například capstanová brzda v jachtingu nebo [spouštěcí buben v arboristice](https://www.worksafety.cz/2545-stein-stein-spousteci-buben-rc2001/). Efekt funguje stejně, jenom exponenciální funkce roste s nižším koeficientem v exponentu.

### Rovnice ohybové čáry nosníku, kvadratický moment průřezu

Bude doplněno.

### Thiemova rovnice

Bude doplněno.

### Vedení tepla v mezikruží

Bude doplněno.

### Rovnice podzemní vody

Rovnice podzemní vody je obecná difuzní rovnice specifikovaná pro podzemní vodu. Je v ní započtena dynamika v čase a Darcyho zákon (viz výše). Díky tomu dokáže modelovat časový vývoj hladiny podzmení vody a proudění při různých scénářích čerpání, zasakování, budování vodních děl. Ve velkém měřítku je použitelná pro pochopení funkce vody v krajině. V malém měřítku pro posouzení vlastností studny nebo pro ochranu budov a výkopů před spodní vodou. 

### Difuzní rovnice

Bude doplněno.

### Buckinghamův pí teorém

<div class='obtekat'>

```{figure} hala.jpeg
Model Janáčkova kulturního centra v měřítku 1:10. Zdroj: https://ct24.ceskatelevize.cz/regiony/
```

</div>

Fyzikální zákony jsou invariantní vůči změně jednotek. Fyzikálním procesům je jedno, jestli je měříme v metrech nebo v milimetrech. Z tohoto principu vychází rozměrová analýza a její zdokonalení - Buckinghamův pí teorém. Tato technika umožňuje například předpovědět, jak se budou systémy chovat při změně měřítka. Jako aktuální praktické využití uveďme, že [v létě 2021 jsme v Brně hostili](https://ct24.ceskatelevize.cz/regiony/3304995-brno-ma-model-koncertniho-salu-za-dva-miliony-mesto-na-nem-overi-akustiku-budouci) na výstavišti model koncertní haly v měřítku 1:10 k ověření akustických vlastností budoucí stavby. Změna měřítka má vliv na parametry, přesně podle Buckinghamova teorému. To bylo nutno zohlednit při měření. Konkrétně, bylo nutno desektrát urychlit čas, tj. v praxi použít desetinásobek frekvence zvuku. To si vynutilo další opatření: při vysokých frekvencích by se negativně projevovaly vodní páry a proto bylo nutno je z modelu vytěsnit, což se udělalo natlakováním dusíkem. Další metoda jak se vyrovnat s menšími rozměry bez změny frekvence by mohla spočívat v naplnění médiem, ve kterém se zvuk šíří desetkrát pomaleji než ve vzduchu. Toto je pro použití problematičtější, ale i to by byla cesta. Tato cesta je chybně zmíněna v odkazované reportáži.

### Okrajová podmínka v rovnici vedení tepla

Bude doplněno.

### Numerické řešení rovnic vedení tepla, difuze, strukturální analýza

Rovnice vedení tepla, difuzní rovnice nebo rovnice popisující reakci na mechanické namáhání pěkně zachycují fyzikální princip děje, ale není praktické je řešit analyticky. Analytické řešení je známo pro jednoduché množiny, typu kruh, obdélník, krychle. Stačí mít netriviální oblast a je nemožné či nepraktické rovnici řešit. Používá se __numerické řešení__ kombinace několika technik.

* Převod derivací pomocí konečných diferencí na algebraické výrazy používající čtyři základní aritmetické operace.
* Použití konečných diferencí vede k aproximaci úlohy lineárním systémem a řešení tohoto systému dává dobrý odhad řešení původní úlohy. Řádově desítky tisíc rovnic.
* Pokud materiálové vztahy nejsou lineární, je výsledný systém nelineární. Řeší se například vícerozměrnou modifikací Newtonovy iterační metody.
* Zpravidla je celý proces řešení plně automatizovaný a uživatel nakreslí nebo naimportuje geoemtrii úlohy, 

### Integrální střední hodnota

<div class='obtekat'>

```{figure} beh.jpg
Optimální pohyb běžce je takový, aby nedocházelo k výkyvům v poloze těžiště. Těžište hledáme tak, že zprůměrujeme souřadnice všech bodů. Protože však tělo má spojitě rozloženou hmotnost a bodů je nekonečně mnoho, musíme tento průměr chápat ve smyslu integrální střední hodnoty. Zdroj: pixabay.com, autor RoonZ-nl
```

</div>

Vypočítat aritmetický průměr, hodnotu ležící z určitého úhlu pohledu uprostřed mezi zadanými hodnotami umíme už ze základní školy a používáme v běžném životě (průměrná známka na vysvědčení, průměrný měsíční plat atd.). Někdy však potřebujeme vypočítat průměr spojitě rozložených hodnot. Například těžiště trojúhelníka nebo soustavy hmotných bodů [vypočítáme právě aritmetickým průměrem](https://en.wikipedia.org/wiki/Centroid#Of_a_finite_set_of_points). Co ale s případem, kdy je průměrovaná veličina rozložena spojitě na úsečce, na dvojrozměrné množině v rovině, nebo v tělese v prostoru? V takových případech je nutno počítat průměr pomocí integrálu a takový průměr se nazývá integrální střední hodnota. 

* Střední hodnotu funkcí rozložených spojitě na přímce ukazují například měřící přístroje u rychle se měnících veličin. Uvažujme napětí v zásuvce na 230V jako funkci času. Toto napětí se při frekvenci střídavého proudu 50Hz mění padestkrát za sekundu a voltmetr nemá šanci na tyto změny reagovat. Ukazuje zprůměrovanou hodnotu ve smyslu integrální střední hodnoty. (V tomto případě se uvažují výkonové účinky a proto se ve skutečnosti průměruje druhá mocnina napětí a ta se poté zpět odmocní, ale to je v tuto chvíli technický detail.) Pokud chceme okamžitý průběh napětí, musíme použít úplně jiný přístroj - osciloskop. Na něm uvidíme, že napětí se mění cca padesátkrát za sekundu a v některých okamžicích je nad hodnotou 230V, v jiných zase pod ní. To nás ale většinou nezajímá, my potřebujeme průměr, tj. střední hodnotu, což je v Evropě 230V.
* Střední hodnota na dvourozměrné množině definuje těžiště této množiny. To je důleřité z technického hlediska. Například znalost těžiště obrazce, který je průřezem nosníku, umožní po zatížení nosníku identifikovat části nosníku namáhané tahem a části namáhané tlakem. Neutrální osa totiž prochází těžištěm. To je u symetrických obrazců uprostřed. Proto také neutrální osa prizmětického nosníku s průřezem ve tvaru obdélníka je uprostřed. Podobně to platí pro válcové nosníky, například šatní tyče. U složitějších nosníků však situace není na první pohled tak jasná a je nutné stanovit polohu těžiště. V případě těžiště dvourozměnrné množiny dvojným integrálem.
* Tělesa se v mnoha případech pohybují tak, jako by byla jejich hmotnost soustředěna v těžišti. Nejhladší pohyb je přímočarý a proto je například pro běžce nejvýhodnější zvolit takový styl běhu, při kterém se těžiště příliš nevychyluje nahoru/dolů nebo do stran.

### Hydrostatická síla na stěnu 

Hydrostatická síla na rovinnou stěnu je součinem tlaku a obsahu. Toto však je možné použít jenom v případě, že tlak je ve všech místech stěny stejný. Takový předpoklad nebývá splněn u ploch položenýc napříč různými hloubkami. V takovém případě je nutno celkovou sílu na stěnu vypočítat dvojným integrálem, který v podstatě nejprve rozdělí nekonečně jemně celou plochu tak, aby se vliv různých tlaků v různých místech zohlednil a poté všechny příspěvky posčítá do celkové síly. 

Protože je úloha prakticky zajímavá a často se věnujeme jenom jejím speciálním případům, vznikla řada pouček, jak se vyrovnat s vlivem nestejné hloubky i bez dvojného integrálu. Například [metoda zatěžovacího obrazce](http://www.prehrady.cz/vizp/vizp_vi_9_2.pdf) nebo využití těžiště. Tyto metody však mají své limity a jsou speciálním případem obecného postupu založeného na dvojném integrálu. Přístup využívající dvojný integrál také přirozeně zahrnuje i méně časté situace, kdy je stěna šíkmo nebo kdy je celá stěna ponořena do určité hloubky (například výpusť pod hladinou). V takovém případě není nutné se učit speciální poučky jak tyto efekty započíst do inženýrských metod typu metoda zatěžovacího obrazce, ale tyto požadavky se stávají integrální součástí výpočtu.

## Čísla a funkce

* K měření množství čehokoliv potřebujeme *čísla*.
* K vyjadřování vztahů mezi dvěma nebo více veličinami potřebujeme *funkce*.
    * Rostou obě veličiny současně? *rostoucí funkce*
    * Je růst jedné veličiny spojený s poklesem druhé?  *klesající funkce*
    * Lze z výstupu funkce zrekonstruovat vstupní data? Jak? *prostá funkce*, *inverzní funkce*

## Derivace

<div class='obtekat'>

```{figure} blok.png
Vzájemné souvislosti derivace a dvou integrálů.
```

</div>

K měření rychlosti změn potřebujeme *derivace*.

* Derivace veličiny podle času udává rychlost změny veličiny v čase.
* Derivace veličiny podle prostorové souřadnice (jednorozměrný gradient) udává rychlost změny veličiny ve směru příslušné prostorové osy.
* Vektor z derivací veličiny podle prostorových souřadnic (vícerozměrný gradient) udává směr a rychlost změny veličiny.

První dvě operace jsou vlastně totéž, jenom pro jinou nezávislou proměnnou a umíme je i obrátit. Pro tyto potřeby jsme zavedli pojem integrál. Třetí operaci (kdy je zadaný gradient a máme najít původní funkci) se naučíme obrátit pomocí křivkového integrálu druhého druhu, pokud se spolu setkáme v předmětu Aplikovaná matematika v navazujícím studiu.

Symbolicky zapsáno, platí
$\int_a^b f(t)\mathrm dt=F(b)-F(a)$, kde $\int f(t)\,\mathrm dt=F(t)$ tj. $F'(t)=\frac{\mathrm dF}{\mathrm dt}=f(t)$.

## Lineární aproximace

*Vstup:* $y=f(x)$, $x=x_0$ *Výstup:* Aproximace funkce $f(x)$  v okolí bodu $x_0$ přímkou.

$$f(x)\approx f(x_0)+f'(x_0)(x-x_0)$$

* Výraz $f'(x_0)$ je změna funkce $f$ vyvolaná jednotkovou změnou proměnné $x$
* Výraz $x-x_0$ je změna ve vstupních datech, pokud hodnotu $x_0$ změníme na $x$
* Výraz $f'(x_0)(x-x_0)$ je odhad změny funkce $f$, pokud hodnotu $x_0$ změníme na $x$

Využití:

a) **Konstitutivní zákony** v 1D, kdy bereme $x_0=0$ a $f(x_0)=0$.
$$f(x)\approx 0+f'(0)(x-0)=kx$$
b) **Newtonova metoda** používá aproximaci pro $x_0=x_n$, $x=x_{n+1}$ a $f(x_{n+1})=0$, tj. 
$$0=f(x_n)+f'(x_n)(x_{n+1}-x_n)$$ a odsud
$$x_{n+1}=x_n-\frac {f(x_n)}{f'(x_n)}.$$
c) **Konstitutivní zákony ve 2D a 3D,** kdy rozšiřujeme zákon z 1D do vícerozměrného vztahu mezi vektory $$\vec j=A\vec q,$$
kde $\vec j$ je tok, $A$ symetrická matice a $\vec q$ podnět vyvolávající tok $\vec j$. V tomto případě nás zajímají vlastní směry jako neulové vektory splňující $$A\vec u=\lambda \vec u$$ pro vhodné reálné číslo $\lambda$. Pokud jsou  vlastní směry v souřadnicových osách, je matice $A$ diagonální a v diagonále jsou její vlastní čísla.

## Diferenciální rovnice

Pokud neznám časový průběh veličiny ani její rychlost, ale vím, jak spolu hodnoty veličiny s rychlostí souvisí, příslušným matematickým modelem je diferenciální rovnice.

* Obecná diferecnciální rovnice prvního řádu je $$\frac{\mathrm dy}{\mathrm dt}=f(y,t),$$
my jsme se naučili řešit dvojí integrací rovnice se separovanými proměnnými ve tvaru $$\frac{\mathrm dy}{\mathrm dt}=f(y)g(t).$$
* Diferenciální rovnice tvaru $$\frac{\mathrm dy}{\mathrm dt}=f(y)$$ má monotonii řešení dánu znaménkem pravé strany a odsud mohu posoudit i stabilitu konstantních řešení.
* Diferenciální rovnice tvaru $$\frac{\mathrm dy}{\mathrm dt}=f(y)-g(y)$$ je stejného typu jako předchozí rovnice a monotonie řešení stabilita vyplyne ze vzájemného srovnání obou funkcí na pravé straně.

## Transportní děje

Tento přístup používáme v situacích, kdy rychlost změny veličiny souvisí se změnami v toku, který tuto veličinu přenáší.

Celkovou bilanci je možno vyjářit vztahem dávajícím do relace rychlost akumulace stavové veličiny a součet přírůstku ze zdrojů s přírůstkem díky toku.
$$\frac{\partial u}{\partial t}=\sigma -\nabla\cdot\vec j$$

* Výraz $\vec j$ vyjařuje tok (přesněji hustotu toku).
* Výraz $\nabla\cdot\vec j$ vyjadřuje nárůst hustoty toku, tj. jeho zesílení v daném místě.
* Výraz $-\nabla\cdot\vec j$ vyjadřuje pokles hustoty toku, tj. jeho zeslabení toku v daném místě.

Celková bilance se nazývá rovnice kontinuity.

## Od gradientu k toku

Gradient vyjadřuje směr a intenzitu růstu skalární veličiny. Tok je iniciován záporně vzatým gradientem (směr a intenzita poklesu).

Od záporně vzatého gradientu k toku nás odvedou konstitutivní zákony. Tyto umíme formulovat v jedné i více dimenzích a zpravidla je formulujeme v lineární aproximaci.

Tok je vyvolán nerovnoměrnostmi v prostorovém rozložení veličiny, tj. *gradientem*.

### Jedna dimenze

V 1D je nárůst vyjádřen prostorovou derivací $\frac{\partial u}{\partial x}$ (jednorozměrný gradient) a pokles výrazem $-\frac{\partial u}{\partial x}$ (záporně vzatý jednorozměrný gradient). Tok je $$\vec j=- k \frac{\partial u}{\partial x},$$ kde $k$ je reálná konstanta.

### Více dimenzí

* Ve 2D a 3D je nárůst vyjádřen gradientem $\nabla u=\begin{pmatrix}\frac{\partial u}{\partial x}\\\vdots\end{pmatrix}$ a pokles záporně vzatým gradientem $-\nabla u$. Tok je $$\vec j=- D \nabla u,$$ kde $D$ je $2\times 2$ nebo $3\times 3$ matice.

## Difuzní rovnice

Difuzní rovnice vznikne spojením rovnice kontinuity $$\frac{\partial u}{\partial t}=\sigma -\nabla\cdot\vec j$$
a konstitutivního zákona $$\vec j=- D \nabla u,$$ do jedné rovnice
$$\frac{\partial u}{\partial t}=\sigma -\nabla\cdot\left(- D \nabla u\right)$$
tj. 
$$\frac{\partial u}{\partial t}=\sigma +\nabla\cdot\left( D \nabla u\right)$$

a) Transport vázané vody ve dřevě, kdy hustotou stavové veličiny je koncentrace vody a rovnice je bezzdrojová, tj. $$\frac{\partial u}{\partial t}=\nabla\cdot\left( D \nabla u\right)$$
b) Transport energie vedením tepla, kdy hustotou stavové veličiny je hustota energie (entalpie), platí $$\frac{\partial E}{\partial t}=\rho c \frac{\partial T}{\partial t}, \quad \sigma=0$$
$$\vec j=-k\nabla T$$
$$\rho c\frac{\partial T}{\partial t}=\nabla\cdot\left(k\nabla T\right).$$

## Numerická aproximace

1. Rovnice, viz Newtonova metoda.
2. Derivace aproximujeme pomocí dvou nebo tří po sobě jdoucích hodnot. $$\begin{aligned}\frac{\mathrm df}{\mathrm dx}&=\frac{f(x+h)-f(x)}{h}+O(h)\\\frac{\mathrm df}{\mathrm dx}&=\frac{f(x+h)-f(x-h)}{2h}+O(h^2)\\ \frac{\mathrm d^2f}{\mathrm dx^2}&=\frac{f(x+h)-2f(x)+f(x-h)}{h^2}+O(h^2)\end{aligned}$$ Při použití v rovnici vedení tepla nebo v difuzní rovnici vede na soustavu lineárních rovnic $AX=B$. Tato soustava může být velká (stovky rovnic a proměnných)  a je velmi řídká (v každé rovnici několik málo neznámých). Proto řešíme numerickými metodami odvozenými pro tyto typy soustav.
3. Integrál můžeme aproximovat lichoběžníkovou metodou jako obsah pod lomenou čarou.
4. Diferenciální rovnici $$\frac{\mathrm dy}{\mathrm dt}=f(y,t)$$ můžeme aproximovat podobně jako ve druhém případě, ale s výhodou, že rovnice se dají řešit postupně od počáteční podmínky dopředu nebo dozadu.
$$\begin{aligned}y_{n+1}&=y_n+f(y_n,t_n)h \\ t_{n+1}&=t_n+h\end{aligned}$$

<!--
## Co tu najdete

* Definice jsou neformální, vyjádřeny slovně a proto někdy bohužel poněkud vágně.
* Hlavní je uvědomit si při druhém čtení souvislosti mezi pojmy a aplikační potenciál jednotlivých pojmů.

## Vlastnosti funkcí

#### Prostá funkce

* Definice:  Prostá funkce nabývá každou funkční hodnotu jenom jednou.
* Lze u ní zrekonstruovat vstupní data, tj. definovat inverzní funkci.
* Pokud v rovnici vystupují prosté funkce, dá se tato rovnice řešit
  (pomocí inverzních funkcí).

#### Rostoucí funkce

* Definice: Rostoucí funkce  zachovává uspořádání vzorů i pro funkční hodnoty.
* Rostoucí funkční můžeme detekovat pomocí znaménka derivace.
* Podobně je definována klesající funkce. U spojitých funkcí změna
  růstu na klesání nebo naopak signalizuje lokální extrém.
* Monotonie umožní modifikovat úlohu na lokální extrémy. Například úloha s nosníkem maximální tuhosti: úloha $x^3\sqrt{1-x^2}\to\max$ je na intervalu $x\in (0,\infty)$
  ekvivalentní mnohem jednodušší úloze pro druhou mocninu funkce,
  tj. $x^6(1-x^2)\to\max$.

#### Spojitá funkce

* Definice: Spojitá funkce má v každém bodě stejnou limitu a funkční hodnotu.
* Nespojité funkce jsou nepředvídatelné a jejich chování je
  neintuitivní.  Například změna monotonie si bez spojitostí nemusí
  vynutit existenci lokálního extrému. Spojité jsou v určitém smyslu
  pěkné. Spojitost je vyžadována například pro Bolzanovu větu a ta je základním nástrojem pro vyšetřování průběhu funkce (umožní najít intervaly kde je fuknce kladná a záporná, kde je funkce rostoucí a klesající, kde je funkce konvexní a konkávní).
* Spojitost je automaticky zaručena, jakmile existuje derivace.
* Elementární funkce jsou spojité na svém definičním oboru.

## Derivace

#### Obyčejná derivace 

* Definice: $\frac{\mathrm df}{\mathrm dx}=\lim_{h\to 0} \frac{f(x+h)-f(x)}h$
* Okamžitá rychlost změny $f$, tj. změna veličiny $f$ vztažená na
  jednotku veličiny $x$.
* Jednotka je stejná, jako bychom veličiny $f$ a $x$ dělili.   
* Derivace umožní detekovat monotonii.
* Derivace umožní kvantitativně pracovat s rychlostí změny a tím umožní lineární
  aproximaci. Ta se uplatní při přibližných výpočtech (odvození
  Newtonovy věty, u parciálních derivací odvození tenzoru malých
  deformací a odvození vzorce pro divergenci vektorového pole).
* Derivace umožní formulovat modely založené na rychlostech, kdy
  rychlost měnící se veličiny souvisí s velikostí této nebo jiné 
  veličiny. Většina fyzikálních zákonů je v tomto
  tvaru. (Např. Newtonův zákon ochlazování, rychlost s jakou se mění
  teplota tělesa při tepelné výměně je úměrná rozdílu teplot.)
* Vzorec pro derivaci složené funkce se používá i v případě, že jsou
  dvě veličiny svázány vzorcem, jedna veličina se mění zadanou
  rychlostí a snažíme se identifikovat, jakou rychlostí se mění
  veličina související. (related rates problems) 
* Vzorce pro derivaci konstantního násobku, derivaci složené funkce a derivaci součtu se (kromě přímého využití při derivování) používají často při eliminaci konstant z diferenciální rovnice. Zde vhodnou záměnou za jiné veličiny (často bezrozměrné -- nondimenzionalizace) dosáhneme toho, že úloha má menší počet parametrů a je možné ji snáze řešit, zejména pokud musíme použít numerické metody.

#### Gradient

* Definice: Gradient funkce (většinou více proměnných) je vektor sestavený z parciálních derivací funkce.
* Je důležitý při studiu materiálové odezvy, protože podnětem pro reakci
materiálu bývá gradient stavové veličiny, viz například Fickův zákon,
Fourierův zákon, Darcyho zákon.
* Gradient (přesněji vektor z parciálních derivací podle prostorových proměnných) umožní formulovat fyzikální zákony charakterizující proudění stavové veličiny způsobené nerovnoměrným prostorovým rozložením této veličiny. (Například teplota se mění dodáním nebo odebráním tepla a teplo proudí ve směru daném Fourierovým zákonem. V izotropním protředí tedy ve směru gradientu teploty vynásobeného faktorem $-1$, tj. ve směru maximálního poklesu teploty.)

#### Obyčejná derivace versus parciální

* Obyčejná derivace udává, jak reaguje veličina závisející na jedné
  proměnné na změnu vstupních dat. Parciální derivace udává, jak
  reaguje veličina závisející na více proměnných na změnu vstupních
  dat, pokud se mění jenom jedna z proměnných. Ostatní bereme jako
  parametry a proto se dá používat stejná pravidla pro výpočet jako u
  obyčejné derivace.
* Parciální derivace však mají smysl zejména proto, že je seskupujeme
  do operátorů jako jsou například divergence nebo gradient a tyto
  operátory jsou přirozeným jazykem pro formulaci přírodních zákonů.
* Parciální derivace umožňují studovat změny funkcí více proměnných a
  použili jsme je například pro tenzor malých deformací ve
  dvourozměrném nebo trojrozměrném případě.

## Divergence, tok a zákony zachování

* Definice: Divergence vektorového pole je celková bilance toku z
  daného místa přes hranici myšlené (nekonečně malé) množiny, dělená
  mírou (objemem ve 3D nebo plochou ve 2D) této množiny.
* V 1D je divergence parciální derivace jednorozměrného toku podle prostorové proměnné. Odpovídá to tomu, že při proudění jedním směrem (představme si nataženou hadici) nemusí v jiném průřezu být stejný průtok. 
* Rovnice kontinuity je vyjádření říkající, že rychlost změny stavové
  veličiny v daném místě je dána vydatností zdrojů v tomto místě
  zmenšené o tok z daného místa.
* K rovnici kontinuity často přidáváme konstituční zákon. Většinou má
  roli vztahu vyjadřujícího, že intenzita toku je záporně vzatý
  gradient stavové veličiny vynásobený materiálovou konstantou
  (difuzní rovnice, obecně tenzorového charakteru, tj. matice).
* Někdy nás zajímá stacionární případ, kdy je nastolena
  rovnováha. Potom $\frac{\partial u}{\partial t}=0.$
* Někdy nás zajímá případ, kdy nejsou přítomny zdroje. Potom
  $\sigma=0.$ Často toto je u rovnice vedení tepla (uvnitř dřeva
  nejsou tepelné zdroje) a vlhkosti (uvnitř dřeva se nijak
  nesyntetizuje voda).
* Výraz popisující tok, tj. $\mathrm{div}(D\nabla u)$, může mít v
  různých prostředí různou míru zjednodušení.

    * Nejjednodušší tvar je pro homogenní izotropní prostředí. Potom se jedná o rovnici typu (např. ve dvou rozměrech) $$\frac{\partial u}{\partial t}=\sigma + D\frac{\partial ^2 u}{\partial x^2}+ D\frac{\partial ^2 u}{\partial y^2}.$$
    * Pro ortotropní materiál (např dřevo) je možné identifikovat vlastní směry, ale v každém vlastním směru je jiná materiálová chrakteristika, tj. místo společného $D$ u obou členů s derivacemi podle souřadnic bude mít každý člen svoji konstantu. $$\frac{\partial u}{\partial t}=\sigma + D_x\frac{\partial ^2 u}{\partial x^2}+ D_y\frac{\partial ^2 u}{\partial y^2}$$
    * Pro ortotropní nehomogení materiál není možné pro členy v difuzní rovnici využít pravidlo pro derivaci konstanty a maximální míra zjednodušení je $$\frac{\partial u}{\partial t}=\sigma + \frac{\partial}{\partial x}\left(D_x\frac{\partial  u}{\partial x}\right) + \frac{\partial}{\partial y}\left(D_y\frac{\partial  u}{\partial y}\right).$$

## Integrály

#### Neurčitý integrál

Neurčitý integrál má na vstupu funkci a na výstupu funkci. Je-li na vstupu rychlost, s jakou se mění veličina $F$ v čase, na výstupu je funkce popisující časový průběh veličiny $F$ v čase a ta je dána až na aditivní konstantu.

#### Newtonův integrál

Newtonův integrál má na vstupu funkci a interval a na výstupu číselnou
hodnotu. Je-li na vstupu rychlost, s jakou se mění veličina $F$ v čase
a časový interval, na výstupu je změna veličiny $F$ za daný
interval. Ta se počítá pomocí neurčitého integrálu jako rozdíl hodnot
funkce $F$ za uvažovaný časový interval. Na aditivní konstantě u
funkce $F$ nezáleží díky tomu, že pracujeme se změnou a ne s
absolutními čísly. V případě konstantní rychlosti (integrál z
konstantní funkce) se redukuje na násobení funkce a délky
intervalu. Má tedy smysl pro procesy probíhající nekonstantní
rychlostí.

#### Riemannův integrál

Na vstupu je interval a funkce, na výstupu číselná hodnota. Je odvozen
pro aditivní veličinu, kterou v případě konstantních parametrů
počítáme pomocí součinu. Pokud parametry nejsou konstantní, přechází
součin na integrál. Například práce konstantní síly je součin
velikosti síly a posunutí, ale pro proměnnou sílu musíme práci počítat
jako určitý integrál síly.

Pro spojité funkce vychází stejně jako Newtonův integrál a takto se
většinou i počítá, ale je možné jej i aproximovat numericky
(lichoběžníkové pravidlo).

#### Dvojný integrál

Jako Riemannův, ale studovaná funkce je definovaná nad dvourozměrnou
množinou.

## Maticový součin

* Slouží k efektivnímu zápisu lineárních vztahů mezi vícerozměrnými
  veličinami, kdy se jednotlivé příspěvky sčítají. Například Hookův
  zákon: každá složka tenzoru napětí (definovaný působící silou) se
  může s lineární odezvou projevit deformací v kterémkoliv směru a pro
  každý směr se příspěvky od jednotlivých složek tenzoru napětí
  sčítají.
* Umožňuje definovat fyzikální zákony mezi vektory, které nemusí mít
  stejný směr (konstituční zákony jako Fickův apod).
* Umožňuje modelovat vývoj systémů se skokovou změnou v čase (Leslieho
  matice, Markovovy řetězce).
* Umožňuje efektivně zapsat soustavu lineárních rovnic.
* Umožňuje přecházet k jiným souřadnicovým systémům, např. umožňuje
  pootočení soustavy souřadnic. To se dělá zejména v případě, že v jiné soustavě je formulace problému jednodušší, například je systém charakterizován diagonální maticí, namísto symetrické matice. O jednoduchosti diagonálních matic viz níže.

## Vlastní číslo a vlastní vektor matice

* Definice: Vektor $\vec u$ je vlastní vektor matice $A$ příslušný vlastní
  hodnotě $\lambda$, pokud $A\vec u=\lambda \vec u$.
* Vlastní vektor k matici $A$ se působením matice $A$ neodchýlí od
  původního směru. V řeči materiálů tedy materiálová odezva má stejný
  směr jako podnět, pokud je podnět ve vlastním směru. Například pokud
  tlak klesá směrem, ve kterém pórovité prostředí vede nejochotněji
  tekutinu, tak tato tekutina proudí přesně ve směru maximálního poklesu tlaku. Pokud tlak klesá jiným směrem, tok tekutiny se stáčí
  do směru, ve kterém materiál vede tekutinu "ochotněji".
* Vlastní vektory a čísla odpovídají směrům, ve kterých má reakce
  materiálu na vnější podnět maximum nebo minimum.

## Transponovaná matice

* Definice: Matica transponovaná je matice, ve které jsou řádky zaměněny za sloupce.
* Slouží například při vyjádření tenzoru deformace k odfiltrování
  pootočení z matice popisující změnu polohy bodů v tělese,
  tj. (matematicky vyjádřeno) k rozkladu matice na součet symetrické a
  antisymetrické matice.
* Pro speciální matice (ortogonální) je transponovaná matice současně
  maticí inverzní. Takové matice přirozeně vychází například při
  transformaci matice do souřadnic mířících vlastními směry matice.

## Inverzní matice

* Definice: $A A^{-1}=A^{-1}A=I$
* Existuje pouze pokud je determinant matice $A$ nenulový.
* Inverzní matice se používá při studiu soustav lineárních rovnic. Teoreticky je řešením soustavy lineárních rovnic $AX=B$ vektor $X=A^{-1}B$. V praxi je výpočet inverzní matice nestabilní a používáme inverzi jenom k jednodušším maticím (Jacobiho metoda používá inverzi k diagonální matici, Gaussova-Seidelova inverzi k trojúhelníkové matici, ale obě metody jsou iterační)
* Maticový součin se používá pro vyjádření transformace souřadnic, inverzní matice je potom nástroj pro cestu zpět k původním souřadnicím. Je-li přechod mezi souřadnicemi $X$ a $X'$ dán vztahem $X=AX'$, v opačném směru platí $X'=A^{-1}X$.
* Inverzní matice se používá pro vyjádření fyzikálních zákonů v soustavách souřadnic, které vzniknou pootočením původních souřadnic. Je-li fyzikální zákon (Hookův, Fickův, ...) mezi vektory ve tvaru $Y=AX$ a přechod do čárkovaných souřadnic je umožněn rovnicemi $Y=PY'$, $X=PX'$, je $Y'=P^{-1}AP X'$ a $P^{-1}AP$ je vyjádření tenzoru $A$ v čárkovaných souřadnicích. Používá se zejména při otočení souřadnic.

## Determinant

* Charakterizuje svou nulovostí nebo nenulovostí neexistenci nebo existenci inverzní matice.
* Úloha na hledání vlastních čísel (maximální a minimální materiálová odezva na podnět) vede na výpočet jistého determinantu.

## Soustava lineárních rovnic

* Úloha na hledání vlastních směrů (směr ve kterém je extrém
  materiálové odezvy na podnět) vede na řešení jisté soustavy
  lineárních rovnic.
* Přibližné řešení difuzní rovnice nebo rovnice vedení tepla je možné
  realizovat převodem na soustavu lineárních rovnic. Například v
  metodě konečných diferencí hraje při aproximaci roli Taylorův
  polynom.
* Univerzální metodou řešení je Gaussova eliminace, numericky
  výhodnější pro soustavy s jedním řešením a pro diagonálně dominantní matice jsou iterační metody, například Jacobiho a Gaussova-Seidelova.
* Ve vektorové podobě jde o vyjádření zadaného vektoru jako lineární
  kombinace jiných zadaných vektorů. Tedy například rozklad vektoru do
  daných směrů.

## Diagonální matice

* Součin matice $A$ s diagonální maticí $D$ je snadné, protože v součinem $AD$ je matice, která má sloupce tvořené násobky sloupců matice $A$.
* Determinant diagonální matice je součin prvků v diagonále. 
* Vlastní čísla diagonální matice jsou právě čísla v diagonále. Příslušné vlastní vektory jsou jednotkové vektory se směru jednotlivých os.
* Po transformaci symetrické matice do soustavy souřadnic ve které osy míří do vlastních směrů je výsledná matice diagonální a proto má všechny pěkné vlastnosti uvedené v předchozích bodech.
* Soustava lineárních rovnic s diagonální maticí je triviální. Stejně tak nalezení inverzní matice je triviální záležistost. Toho můžeme využít i v případě, že soustava nemá diagonální matici, ale matici, která je k diagonální matici jenom v jistém smyslu blízká. Tovo využívají základní iterační metody pro řešení soustav, zejména Jacobiho metoda.

## Věty z diferenciálního počtu

V tomto seznamu **není** znění vět uvedených v semestru, ale je zde
naznačen jejich význam. Plné znění vět je v přednáškách (v prezentacích
žlutě).

#### Věta o spojitosti elementárních funkcí

Udává, že běžné funkce jsou spojité v každém bodě, kde jsou definovány.

#### Věta o souvislosti derivace a monotonie

*Má-li funkce kladnou derivaci, je rostoucí. Má-li funkce zápornou derivaci, je klesající. *

Představuje efektivní nástroj pro detekci množin, na kterých je funkce
rostoucí nebo klesající.

#### Věta o lineární aproximaci

Jedno z nejdůležitějších využití derivace - lineární aproximace
funkce. Využívá se například v odvození tenzoru malých
deformací. Vztahy získané linearizací přesných zákonů se 
používají v "běžné" fyzice ($E=mgh$ nebo $E=\frac 12 mv^2$). Přes
jednoduchost může být překvapivě silná, např. u Newtonovy metody
řešení rovnic se každým krokem přibližně zdvojnásobí počet desetinných
míst, která jsou správně.

#### Taylorova věta

Vyjadřuje skutečnost, že pokud se snažíme aproximovat funkci
polynomem, je při zadaném stupni polynomu optimální aproximací
Taylorův polynom. Tento polynom můžeme použít například pro aproximaci
potenciálu v okolí lokálního extrému (první derivace tam je nulová a
nijak by nepomohla) nebo pro aproximaci druhé derivace v metodě
konečných diferencí (při řešení rovnice vedení tepla přibližnými
metodami).

#### Fermatova věta o lokálním extrému

Fermatova věta umožňuje soustředit se při hledání extrémů na relativně
málo bodů - na body, kde je derivace rovna nule nebo není definovaná
vůbec.

#### Věta o souvislosti monotonie s lokálními extrémy

*V bodě lokálního extrému derivace buď neexistuje nebo je nulová.*

Efektivní nástroj, jak u spojitých funkcí detekovat lokální extrémy
pomocí první derivace (ta souvisí s monotonií).

#### Bolzanova věta

*Funkce která je na uzavřeném intervalu spojitá a mění zde znaménko má mezi znaménkovými změnami nulový bod.*

Prostředek na nalezení intervalů, kde je zadaný výraz kladný nebo
záporný. Na této větě je založeno například hledání lokálních extrémů
pomocí derivace, protože potřebujeme intervaly, kde je derivace funkce
kladná a kde je záporná.

#### Výpočet divergence

Divergence je důležitá veličina používaná pro obecnou formulaci zákonů
zachování v rovnici kontinuity. V kartézských souřadnicích je možné ji
vyjádřit pomocí parciálních derivací.

## Věty z integrálního počtu

#### Věta o jednoznačnosti primitivní funkce (až na aditivní konstantu)

Udává, že pokud známe rychlost s jakou se mění funkce, je tato funkce dána jednoznačně, až na aditivní konstantu související s počáteční hodnotou.

#### Věta o monotonii integrálu vzhledem k funkci

Zobecňuje názornou myšlenku, že pokud se zvýší rychlost, s jakou se mění nějaká veličina, je za stejný čas změna výraznější.

#### Lichoběžníkové pravidlo

Umožňuje aproximovat určitý integrál vhodnou lineárních kombinací funkčních hodnot. Jedná se o nástroj, jak odhadnout určitý integrál bez znalosti primitivní funkce.

#### Metoda per-partés

Převádí integrál z jednoho součinu na integrál z jiného
součinu. Má smysl pro případ, kdy nový integrál je jednodušší. Jedná se
o jakousi částečnou náhradu za neexistující vzorec pro integrál ze
součinu funkcí.

#### Substituční metoda

Převádí integrál z jedné proměnné do jiné proměnné. Má smysl
pro případ, kdy nový integrál je jednodušší. Jedná se o jakousi
částečnou náhradu za neexistující vzorec pro integrál složené funkce.

#### Integrál jako funkce horní meze

Většinou určitý integrál počítáme pomocí integrálu neurčitého. Někdy to ale nejde, protože neumíme najít primitivní funkci. V takovém případě můžeme díky této větě napsat primitivní funkci ve tvaru určitého integrálu a počítat hodnoty numericky, například lichoběžníkovým pravidlem. Tato věta otevírá cestu do světa funkcí, které nejsou elementární.

#### Postačující podmínka pro existenci primitivní funkce

Udává, že prakticky zajímavé funkce (spojité) jsou vždy
integrovatelné, tj. mohou být rychlostmi změn veličin.

## Věty o diferenciálních rovnicích 

#### Věta o jednoznačnosti řešení počáteční úlohy

Uváděli jsme si celkem dvě věty, které zajistí jednoznačnost
řešení. Jednu speciální pro diferenciální rovnici se separovanými
proměnnými, kdy stačí kontrolovat nenulovost pravé strany a druhou pro
obecnou diferenciální rovnici, kdy stačí kontrolovat ohraničenost
parciální derivace pravé strany podle $y$.

#### Věta o stabilitě řešení rovnice $y'=f(y)$

Umožní posoudit, která řešení jsou prakticky zajímavá, bez řešení
diferenciální rovnice.

## Věty z lineární algebry

#### Věta o hodnosti matice ve schodovitém tvaru

Spolu a větou identifikující operace zachovávající hodnost je to efektivní nástroj pro zjištění hodnosti matice nebo pro ověření lineární nezávislosti vektorů.

#### Frobeniova věta

*Soustava lineárních rovnic má řešení právě tehdy, když hodnosti matice soustavy a rozšířené matice soustavy jsou stejné.*

Nutná a postačující podmínka řešitelnosti soustavy lineárních rovnic pomocí pojmů hodnost matice a hodnost rozšířené matice soustavy. 

#### Věta o vlastních číslech symetrické matice

*Reálná symetrická matice řádu $n$ má $n$ reálných vlastních čísel (počítáno i s násobností).*

Vyjadřuje, že ve fyzikálně relevantních případech (matice je
symetrický tenzor) existují vlastní čísla a vlastní směry. To je
výhodné, protože těchto směrech je formulace fyzikálních zákonů
formálně jednodušší než ve směrech zcela obecných.

#### Věta o diagonalizaci čtvercové matice

Udává přímo návod, jaká transformace převede fyzikální zákon vyjádřený
pomocí maticového násobení do co nejjednoduššího tvaru.
-->

\fi
