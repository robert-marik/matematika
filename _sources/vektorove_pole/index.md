# Vektorová pole, tok, zákony zachování

> **Poznámky k samostudiu:**
> 
> * Příroda "nemá ráda"  nerovnoměrné rozložení celé řady veličin, jako je koncentrace látky nebo hustota vnitřní energie (teplota). Proto se snaží případnou nerovnost vyrovnávat transportními ději, jako je difuze nebo vedení tepla. V této přednášce je jednotný přístup ke všem transportním dějům.
> * Rovnice kontinuity je matematickým vyjádřením základní "selské úvahy", že navýšení transportované veličiny v daném místě je způsobeno produkcí veličiny v tomto místě a tím, co do tohoto místa přinese tok, tj. zeslabením toku.
> * Difuzní rovnice je rovnice kontinuity doplněná o konstituční zákon. Ten je matematickým vyjádřením pozorování, že větší nerovnosti se vyhlazují intenzivnějším tokem. Moderní formulace konstitučních zákonů vychází z tenzorového (maticového) tvaru, aby bylo možno modelovat i chování anizotropních látek.
> * Pro určení, pro jaký materiál a děj je napsána transportní rovnice typu
>   $$\frac{\partial u}{\partial t} =\sigma +
\frac{\partial }{\partial x}\left(D_x\frac{\partial u}{\partial x}\right)+
\frac{\partial }{\partial y}\left(D_y\frac{\partial u}{\partial y}\right)$$ 
>    je potřeba se dívat, zda je v rovnici derivace podle času (posoudíme stacionárnost a nestacionárnost), zda je tam člen bez derivací (posoudíme existenci zdrojů a spotřebičů), zda jsou difuzní konstanty pro jednotlivé směry odlišeny či nikoliv a zda prostorové souřadnice jsou ve výrazech s kvaziderivacemi, nebo se druhými derivacemi. To je snadné, jenom je potřeba vědět, na co se dívat.


https://youtu.be/DonzhFhcyQ4

## Připomenutí derivací

Derivace umožňují studovat a popisovat změny veličin, vyjadřovat kvantitativně jejich vzájemné souvislosti.

### (Obyčejná) derivace $\frac{\mathrm df}{\mathrm dt}$. 

* S touto derivací se pracuje u funkce jedné proměnné $f(t)$. Např. $f(t)=kt^2$, kde $k$ je parametr (reálné číslo).
* Derivace je okamžitá rychlost změny veličiny $f$ vzhledem k $t$, tj. nárůst veličiny $f$ vyvolaný jednotkovým nárůstem veličiny $t$. (Prakticky však veličinu $t$ změníme o malou hodnotu a nárůst přepočítáme na jednotkovou změnu.)
* Jednotka derivace je stejná, jako bychom veličiny $f$ a $t$ dělili.
* V modelech a při praktickém využití pracujeme s definicí derivace jako s rychlostí změny. Při výpočtu ale využíváme dostupné vzorce pro výpočet derivace. Například pro funkci z prvního bodu platí $\frac{\mathrm df}{\mathrm dt}=2kt.$

### Parciální derivace $\frac{\partial f}{\partial t}$, $\frac{\partial f}{\partial x}$, $\dots$. 

* S touto derivací se pracuje u funkce více proměnných, typicky $f(x,y,z,t)$. Např. $f(x,y,z,t)=xt^2$
* Jedná se o obyčejnou derivaci podle jedné proměnné, přičemž ostatní proměnné považujeme za parametry. Tj. v případě funkce z minulého bodu je $\frac{\partial f}{\partial t}=2xt$, $\frac{\partial f}{\partial x}=t^2$,  $\frac{\partial f}{\partial y}=\frac{\partial f}{\partial z}=0$.
* Pro jednotku a výpočet platí totéž co u obyčejné derivace. 
* Při aplikacích často pracujeme s gradientem, tj. s vektorem sestaveným z parciálních derivací podle jednotlivých prostorových proměnných. Pro funkci tří proměnných $x$, $y$ a $z$ a pro 
potřeby matematické formulace fyzikálních zákonů gradient uvažujeme jako sloupcový
vektor
$$\nabla f =\begin{pmatrix}\frac{\partial f}{\partial x}\\\mathstrut \frac{\partial f \mathstrut}{\partial y \mathstrut}\\\frac{\partial f}{\partial z}\end{pmatrix}.$$
Pro úsporu místa jej někdy píšeme v transponovaném tvaru
$$\nabla f =\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)^T.$$ Gradient je vektor, který má směr odpovídající směru nejrychlejšího růstu skalární veličiny a velikost odpovídá změně veličiny na jednotku délky.

## Transportní jevy

https://youtu.be/ULoUeHincbM

\iffalse 

<div class='obtekat'>

```{figure} 3d_pole.png
Pro popis proudění je vhodné vektorové pole. Zde je ve 3D a vykreslené v náhodných bodech v prostoru.
```

</div>

\fi

  Pochopení a modelování transportních dějů je
  důležité pro většinu technických oborů. Podstata těchto dějů je často
  odlišná, přesto mají navenek podobné chování a tím je umožněn
  jednotný přístup při matematickém modelování.

Příklady veličin podléhajících transportním dějům

* povrchová voda
* podzemní voda
* teplo
* voda ve dřevě

Obecná bilance veličiny, která má zdroje a spotřebiče a je přenášena tokem vypadá následovně.

* Existuje veličina, spojitě rozložená v prostoru, charakterizující stav systému. Tuto veličinu budeme nazývat
    *stavovou veličinou* a její hustotu označíme $u$.
* Stavová veličina se může v prostoru přemisťovat *tokem* $\vec
    \jmath$.
* Stavová veličina může vznikat a zanikat.
    *Zdroje* i *spotřebiče* budeme
    uvažovat společně a jejich vydatnost rozlišíme
    znaménkem: spotřebiče budou zdroje se zápornou vydatností. Celkovou vydatnost zdrojů a spotřebičů v daném místě, tj.
    množství veličiny vygenerované na jednotku objemu (nebo plochy,
    nebo délky, podle počtu dimenzí v úloze) za jednotku času,
    označíme $\sigma$.

Zákon zachování (se zohledněním toku a zdrojů) je vlastně celková
bilance stavové veličiny. Přirozeným jazykem je možno tuto bilanci
formulovat následovně.  

> Přírůstek množství veličiny je součtem přírůstku ze zdrojů a přírůstku způsobeného tokem.

Toto je jednoduchý, ale přitom neuvěřitelně silný nástroj, který
umožní popsat řadu zcela odlišných dějů. Pro použití v matematickém
modelu ale musíme jednotlivé pojmy kvantifikovat. Měřit rychlost, s
jakou se mění množství veličiny v daném místě umíme pomocí derivace
podle času. Měřit změny v toku přenášejícím sledovanou veličinu jsme
se naučili jako jednu z aplikací parciálních derivací: jedná se o
záporně vzatou derivaci podle prostorové proměnné vynásobenou
fyzikální materiálovou konstantou. Ještě se musíme naučit měřit intenzitu toku a její změny ve dvou nebo třech dimenzích.

## Tok a gradient v konstitutivních zákonech

https://youtu.be/xUhAudBfGLo 

```{prf:remark} Konstitutivní zákony
:nonumber:
 V aplikacích často formulujeme
zákony nebo vztahy mezi fyzikálními veličinami specifickými pro danou látku nebo materiál a udávají odezvu tohoto materiálu na externí stimul. Tyto zákony se nazývají *konstitutivní zákony* a formulujeme je pomocí gradientu a toku vektorového pole. Viz též [Wikipedie](https://en.wikipedia.org/wiki/Constitutive_equation).
```


\iffalse

<div class='obtekat'>

```{figure} vitr.jpg
Tok si snadno představíme mechanickým modelem. Například větru nebo vody. Zdroj: pixabay.com
```

</div>

\fi

Například vítr (tok
molekul vzduchu) je vyvolán nerovnoměrným rozložením vzduchu (jeho
hustoty a tím i tlaku) v prostoru a směřuje z míst s vyšším tlakem do
míst s tlakem nižším.  Větší rozdíl tlaků způsobí "větší vítr" a tím
větší tok vzduchu. Toto platí i pro jiné proudění, jak ukážeme dále.

Nerovnoměrnost v prostorovém rozložení charakterizuje gradient. 
V ustáleném stavu je pro široké rozmezí fyzikálních problémů závislost
intenzity toku na gradientu lineární.  A protože nulovému gradientu (nulovému stimulu) odpovídá nulový tok (nulová odezva),
bude tato lineární funkce přímou úměrností.

V dalším shrneme důležité praktické příklady, kdy je tok úměrný
gradientu.  Konstanta úměrnosti je obecně pouze konstantou pro daný
problém a dané hodnoty parametrů. Může se měnit s velikostí
studovaného objektu (například obsah průřezu geologické vrstvy, kterou
proudí voda), s fyzikálními vlastnostmi proudící látky
(např. viskozita nebo hustota tekutiny, stlačitelnost vzduchu), s fyzikálními vlastnostmi prostředí (např. velikost pórů v pórovitém
prostředí nebo vlhkost dřeva). Proto je možné tyto zákony najít v různých tvarech, s různými členy a případnými přídavnými konstantami,
které například odseparují vliv vlastností proudící látky a vliv vlastností prostředí. Vždy
záleží na konkrétní situaci, zvyklostech v příslušném podoboru, nebo
na přístupu autora. Není proto naší ambicí vést výklad dopodrobna,
všímejme si jenom základních myšlenek.

## Vícerozměrné konstitutivní zákony

Zákony uvedené níže byly často odvozeny v jednorozměrném případě a letmo zmíněny v přednášce Derivace II. V moderní formulaci používáme obecný vektorový zápis, který zohledňuje i směr. Konstanta úměrnosti potom zprostředkovává vztah mezi dvěma
vektory. Jedná se tedy z matematického pohledu o matici, která umožní
nejenom změnit délku vektoru a jeho jednotku, ale i směr. Tato matice
se navíc při změně báze transformuje speciálním způsobem, tak jako
vektory. Takové objekty nazýváme **tenzory**. Níže budeme pojmem
tenzor rozumět matici $3\times 3$ nebo $2\times 2$, podle
kontextu. (Obecněji je možno považovat skalární veličiny a vektory za
tenzory nižších řádů, toto my však dělat nebudeme.)

[Vizualizace toku a vrstevnic pro anizotropní materiál, kdy tok není vždy kolmý na směr maximálního spádu stavové veličiny.](https://sagecell.sagemath.org/?z=eJxlT89ugyAcvpv4DqSpEVvs1K2Xpexkeu5h2cV1hlmorCgN0E76TnuKvdhQu6zJOPwI34_vH4MdshHOZt1bNr-fWTc738txQ4ziHSyKJUq2qEhQut1GvmfkAcf5jC32iuw4bQ0sHL_fNPRCO-zU4sUSZYvlFbIYWhSnKHPvWjhOa_FD4nu6lp-wNo2Ak1WdPb0obei55RUFBDiT1Z0DwfrUHir6CKaAjTFBoMF0EgBBDO3gCLpzK6fCnLPTpf3-Aq4DH-g5DvQ0DEZW_o_wLA_uU5y_tuRdkF-vG4oL9GflextcydbIkyqPQhrI0NB9mBaB607ja12HNOSIww9qQgQYFwKvidA06oU2816iPNPKSFUyTsWud0NglBwuO5gOgTe9wF7zC8VpggDRR0cslespcRr9AMQpj4Y=&lang=sage&interacts=eJyLjgUAARUAuQ==) 

### Fickův zákon (difuze)

V roce 1855 německý lékař A. Fick objevil, že difuzní tok $\vec J$
(množství látky které projde při difuzi jednotkovou plochou za
jednotku času) je úměrný gradientu koncentrace $c$ této
látky. Matematicky vyjádřeno pomocí moderní terminologie to znamená, že platí
$$\vec J=-D\nabla c. $$
Veličina $D$ se nazývá difuzní koeficient. Pokud má $\vec J$ stejný
směr jako $\nabla c$, je $D$ skalární veličina. Pokud směry nejsou
stejné, je $D$ tenzor. Z fyzikálních důvodů je tenzor $D$ symetrický.

Difuzí se například dřevo zbavuje vlhkosti při vysoušení.

### Darcyho zákon (proudění podzemní vody)

\iffalse

<div class='obtekat'>

```{figure} karany.jpg
Vodárna [Káraný](http://www.vodarnakarany.cz/) infiltruje vodu do podzemí. Znalost, co se tam s vodou děje a kudy a jak teče je nezbytná. Základním zákonem pro popis tohoto děje je Darcyho zákon. Zdroj: nase-voda.cz, Nina Havlová
```

</div>

\fi

V letech 1855 a 1856 francouzský inženýr H. Darcy pokusy prokázal
přímou úměru mezi rozdílem tlaků na koncích
trubice naplněné porézní zeminou (jednalo se vlastně o rozdíl výšek
pro šikmou trubici) a rychlostí proudění vody touto trubicí. Tok
(množství vody, která proteče jednotkovou plochou za jednotku času) je
dán vztahem $$\vec q=-K\nabla p,$$ kde $p$ je tlak a $K$ je koeficient
vodivosti (někdy též koeficient filtrace), v obecném případě
symetrický tenzor, v izotropním případě, kdy $\vec q$ a $\nabla p$
mají stejný směr, veličina skalární.

Někdy se tento zákon neformuluje pomocí gradientu tlaku, ale pomocí
gradientu jiné veličiny, kterou zavádíme v hydrologii pro názorné
studium efektů, souvisejících s prouděním vody. Nejčastěji se jedná o
*vodní potenciál* a  hydraulickou výšku či 
[piezometrickou hladinu](https://cs.wikipedia.org/wiki/Hladina_podzemn%C3%AD_vody). Piezometrická hladina je veličina používaná k tomu, abychom do jednoho
jednoduše modelovatelného faktoru (má rozměr stejný jako délka)
započítali všechny veličiny mající vliv na proudění podzemní vody, od
rozdílu nadmořských výšek, přes kapilární a osmotické jevy až po
vnější síly vyvolané tlakem geologických vrstev a jiné. Jedná se
vlastně o celkovou energii vody s tím, že některé části považujeme za
zanedbatelné. Například často neuvažujeme
kinetickou energii nebo osmózu a kapilární jevy.

### Fourierův zákon (vedení tepla)

\iffalse

<div class='obtekat'>

```{figure} rozhrani.png
Na hranici tělesa je tok tepla dán okrajovou podmínkou vyjádřenou Fourierovým zákonem.  Zdroj: Cengel, Ghajar: Heat and Mass Transfer.
```

</div>

\fi

Fourierův zákon se týká vedení tepla a vyjadřuje, 
že vektor hustoty tepelného toku $\vec q$ vyvolaného gradientem teploty $\nabla T$
je dán vztahem 
$$\vec q=-k\nabla T.$$ 
Je-li materiál anizotropní, což je nejobecnější
případ, je veličina $k$ symetrickým
tenzorem. Je-li materiál izotropní, je
$k$ skalární veličinou, případně skalární veličina násobená
jednotkovou maticí, pokud potřebujeme zachovat její maticový charakter.

### Soretův efekt (termodifuze)

Tok tepla je vyvolaný nerovnoměrným rozložením teploty. Difuze chemické
látky je vyvolána nerovnoměrným rozložením koncentrace této
látky. Většinou je hybatelem procesu nerovnoměrnost v rozložení látky,
která se tímto procesem transportuje. Nemusí to však být
vždy. Příkladem je termodifuze, což je pohyb prvků vyvolaný
nerovnoměrným rozložením teploty. Například při difúzi vody ve dřevě s nerovnoměrným rozložením teploty je tok dán vztahem $$\vec J=-D\nabla c - sD\nabla T, $$
kde $s$ je koeficient termodifuze. 

Rozeznáváme kladný a záporný Soretův efekt. Při kladném dochází k transportu ve směru klesající teploty, při záporném naopak ve směru rostoucí teploty. Te je v kontrastu s ostatními konstitutivními zákony, kde tok proudí vždy jenom do míst s menší hustotou stavové veličiny. Viz Wikipedia a heslo Thermophoresis. Viz Wikipedia a heslo Thermophoresis.

## Speciální případy vztahu mezi gradientem a tokem

\iffalse

<div class='obtekat'>

```{figure} rezistory.png
Formálně jsou všechny konstitutivní zákony stejné a jsou stejné i jako zákon mezi elektrickým proudem a napětím. Proto je možné izolační vrstvy modelovat pomocí elektrických obvodů, rezistorů a vzorců pro jejich spojování z Ohmova zákona. Na obrázku je řez stěnou z dutých cihel a izolace. Zdroj: Cengel, Ghajar: Heat and Mass Transfer.
```

</div>

\fi

Uvažujme vztah mezi gradientem a tokem ve tvaru $$\vec j=-K\nabla u ,$$ kde $K$ je symetrický tenzor. Gradient má ve trojrozměrném případě vyjádření $$\nabla u  =\left(\frac{\partial u }{\partial x},\frac{\partial u }{\partial y},\frac{\partial u }{\partial z}\right)^T$$ a ve 2D $$\nabla u  =\left(\frac{\partial u }{\partial x},\frac{\partial u }{\partial y}\right)^T,$$ kde horní index $T$ značí transponovanou matici, tj. jedná se o sloupcový vektor.

### Obecný případ (anizotropní)

Veličina $K$ je matice $$K=\begin{pmatrix}  k_{11}& k_{12} & k_{13}\\  k_{21}& k_{22} & k_{23}\\  k_{31}& k_{32} & k_{33}\end{pmatrix}$$ jejíž komponenty splňují $k_{ij}=k_{ji}$. Často jsou všechny veličiny kladné a prvky v hlavní diagonále jsou dominantní.

Komponenty vektoru $\vec j=(j_x, j_y, j_z)^T$ jsou $$\begin{aligned}  j_x&=-k_{11}\frac{\partial u }{\partial x}-k_{12}\frac{\partial u }{\partial y}-k_{13}\frac{\partial u }{\partial z},\\  j_y&=-k_{21}\frac{\partial u }{\partial x}-k_{22}\frac{\partial u }{\partial y}-k_{23}\frac{\partial u }{\partial z},\\  j_z&=-k_{31}\frac{\partial u }{\partial x}-k_{32}\frac{\partial u }{\partial y}-k_{33}\frac{\partial u }{\partial z},\end{aligned}$$ což zjistíme prostým maticovým násobením. Prostor pro další úpravu není.

### Ortotropní případ, vhodně zvolené osy

\iffalse

<div class='obtekat'>

```{figure} lepenka.jpg
Ortotropní materiál je typicky materiál z jednotlivých vrstev. Typicky dřevo, půda z různých vrstev, lepenka. Zdroj: pixabay.com
```

</div>

\fi

V obecném případě je zpravidla možné transformovat soustavu souřadnic tak, aby tenzor $K$ byl diagonální. Pro praktické výpočty se toto však často nevyplatí. Pokud však je studovaný problém ortotropní, má charakteristické směry (přesněji, má tři roviny symetrie materiálových vlastností), je možné zvolit souřadnice v souladu s těmito směry a matice $K$ je diagonální. 

$$K= \begin{pmatrix}
  k_{11}& 0 & 0\\
 0& k_{22} & 0\\
  0& 0 & k_{33}
\end{pmatrix}
$$

Komponenty vektoru $\vec j$ jsou
$$
\begin{aligned}
  j_x&=-k_{11}\frac{\partial u }{\partial x},\\
  j_y&=-k_{22}\frac{\partial u }{\partial y},\\
  j_z&=-k_{33}\frac{\partial u }{\partial z}.
\end{aligned}
$$

S diagonální maticí se pracuje velmi dobře, protože má v hlavní
diagonále vlastní čísla. Tato vlastní čísla jsou fyzikální
charakteristikou úlohy. Například největší vlastní číslo a odpovídající
vlastní směr charakterizují směr, ve kterém je odezva materiálu na
vnější podnět maximální a vlastní číslo udává velikost této
reakce. Tyto fyzikální charakteristiky nemohou být závislé na volbě
souřadné soustavy, ve které úlohu popisujeme. Co se mění s volbou
souřadné soustavy jsou pouze souřadnice vlastního vektoru. Vlastní
čísla jsou však skalární a proto jsou invariantní při otočení soustavy
souřadnic. Pokud bychom neměli možnost zvolit
soustavu souřadnic tak, aby matice byla diagonální, máme alespoň
jistotu, že vlastní čísla zůstanou stejná. 

### Ortotropní případ ve 2D

Stejné jako ve 3D, pouze chybí třetí rovnice.

### Izotropní případ

Stejné jako ortotropní případ, ale navíc platí $k_{11}=k_{22}=k_{33}=k.$ Potom
$\vec j=-k\nabla u$, kde $k$ je konstanta a vektory toku a gradientu mají opačný směr.

## Divergence

https://youtu.be/wrYpaPerg3M

\iffalse

<div class='obtekat'>

```{figure} divergence.png
Divergence a tok pole $\vec q=(0,Q, R)$ tělesem nenulového objemu. Tok je zobrazen vždy ve středu stěny. Červené vektory vstupují do krychle a příslušné toky se počítají záporně. Modré vystupují ven a počítají se kladně. V tomto případě je celková bilance kladná, z objemu více vyteče, než vteče dovnitř. Divergence je kladná. Pokud v krychli množství veličiny neubývá, musí tam být zdroj této veličiny.
```

</div>

\fi

Budeme sledovat tok vektorového pole a bude nás zajímat, o kolik se tok v daném místě mění.

* Pro jednoduchost rozdělíme tok na tři nezávislé části ve směru jednotlivých os a vztáhneme vše k jednotkám času a průřezu, tj. budeme uvažovat hustotu toku nějaké fyzikální veličiny.
* Je-li tato hustota toku popsána vektorovým polem  $\vec q=(P,Q,R)$ v jednotkách kilogram na metr čtvereční za sekundu, znamená to, že kolmým průřezem jednotkového obsahu projde za jednotku času $P$ kilogramů sledované látky, jejíž tok popisujeme. Často se pracuje i s objemovým tokem, kdy množství neměříme v kilogramech ale v metrech krychlových a například při ustáleném proudění v trubici (hydrodynamika) je tok roven vektoru rychlosti a při proudění porézním materiálem (proudění podzemní vody) je roven filtrační rychlosti.
* Derivace $\frac{\partial P}{\partial x}$ udává, o kolik studovaný tok v daném místě vzroste ve směru osy $x$ a tento nárůst je vztažený na jednotku délky.
* Ve směru osy $y$ máme tok vyjádřený veličinou $Q$ a proto nás podobně zajímá $\frac{\partial Q}{\partial y}$.
* Analogicky $\frac{\partial R}{\partial z}$.
* Celková změna toku bude součtem všech tří příspěvků. Pokud je kladná, znamená to, že z daného místa více veličiny vytéká, než kolik teče dovnitř. Pokud je záporná, je tomu naopak. Jestli se v případě nerovnováhy v daném místě může proudící veličina tvořit nebo spotřebovávat nebo akumulovat nebo jestli v daném místě může ubývat z tohoto rozboru nezjistíme. Záleží na charakteru proudící veličiny a na okolnostech s tímto prouděním spojených. Tuto informaci nám pro další popis musí dodat externí věda (obecná fyzika, fyzika materiálu, fyzika životního prostředí, hydrologie, pedologie, ...).
* Při preciznější argumentaci dávající do souvislosti parciální derivace jednotlivých komponent toku s tím, co se reálně s vektorovým polem děje, je nutné si pomoci stejně jako u derivací, tj. uvažovat ne dané místo, ale jistý konečně velký objem (viz obrázek), vztáhnout dané veličiny na jednotku objemu a rozměry tohoto objemu limitně stáhnout k nule. Toto však již přesahuje ambice v našem kurzu a jedná se o formalismus, kterému se vyhneme přímým představením hotového výsledku.

<!--
Budeme sledovat tok vektorového pole ze zvoleného 
místa. Vyjádříme bilanci, o kolik je větší tok vektorového pole z daného místa ven ve srovnání s tokem tohoto pole dovnitř (viz krychlička na obrázku). Protože
záleží na objemu, ve kterém tok sledujeme, je  vztáhneme tento tok na
jednotku objemu.

Fyzikálně tok ven uvažujeme jako kladný a tok dovnitř jako záporný. Velikost toku rovinnou plochou určíme jako součin vektorového pole v tomto místě a  obsahu plochy.
Celkový tok $\vec q=(0,q_y,q_z)$ do krychle na obrázku je součtem toků levou boční stěnou a dolní stěnou, tj. 
$$Q_{in}=-q _y\Delta x \Delta z - q _z\Delta x \Delta y.$$
Podobně tok ven z krychle je  $$Q_{out}=\left(q_z+\frac {\partial q_z}{\partial z}\Delta z\right)\Delta x\Delta y + \left(q_y+\frac {\partial q_y}{\partial y}\Delta y\right)\Delta x\Delta z$$
a celková bilance je 
$$Q_{in}+Q_{out}= \left(\frac {\partial q_y}{\partial y}+\frac {\partial q_z}{\partial z}\right)\Delta x\Delta y\Delta z.
$$
V případě proudění i v ose $x$ bude přítomen ještě další analogický člen charakterizující tuto dodatečnou položku. 

-->

Výše uvedenými úvahami je motivována následující definice a věta. (Definice je maličko nepřesná, protože nemáme nástroje pro pečlivější formulaci.)

```{prf:definition} Divergence
:nonumber:
 *Divergence* vektorového pole $\vec F$ v daném bodě je převis toku vektorového pole z tohoto místa nad tokem do tohoto místa. Tento tok se počítá přes hranici infinitezimálně malého referenčního tělesa a je vztažený na jednotku objemu. Divergenci vektorového pole $\vec F$ označujeme $\nabla\cdot\vec F$ nebo $\mathop{\mathrm{div}} \vec F$.
```


```{prf:theorem} Výpočet divergence
:nonumber:

Pro vektorovou funkci $$\vec F=(P,Q,R)=P\vec i + Q\vec j + R\vec k,$$ kde $P$, $Q$ a $R$ jsou funkce tří proměnných $x$, $y$ a $z$ vypočteme divergenci vztahem 	  $$\nabla\cdot\vec F=\mathop{\mathrm{div}}\vec F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}.$$
Pro vektorovou funkci dvou proměnných vypočteme divergenci analogicky, pouze chybí třetí člen. 
```


```{prf:remark} Fyzikální interpretace divergence
:nonumber:
 Vektorové pole používáme k modelování toku veličin, které nás zajímají (teplo v materiálu, tekutina nebo chemická látka v materiálu, voda nebo plyn v půdě a podobně). Divergence vektorového pole udává tok z jednotkového objemu látky v daném místě. Udává, jestli se v daném místě a čase tok nabývá na intenzitě (kladná divergence) nebo ustává (záporná divergence). Tento efekt může být způsoben tím, že veličina přenášená tímto polem se v daném místě buď kumuluje, nebo ubývá a také tím, že daná veličina v bodě může vznikat nebo zanikat.
```


Divergence je lokální veličina. Udává informaci o daném bodě. Pro měření však je nutné mít konečný objem a pro stanovení toku konečně velkou hranici. Vzájemný vztah mezi lokální veličinou a konečným objemem je založený na předpokladu, že podmínky se nemění skokem a okolí každého bodu jsou nepříliš odlišné od podmínek v okolních bodech.

```{prf:remark} Fyzikální interpretace divergence v měřitelných pojmech
:nonumber:
 Protože tok přes hranici umíme měřit u těles, představíme si okolo bodu který nás zajímá, těleso. Například kouli nebo krychli. Poté určíme tok přes hranici. Tok hranicí ven počítáme kladně a dovnitř záporně. Celkový tok hranicí určíme jako součet přes všechny části hranice. Podíl celkového toku přes hranici tělesa a objemu tohoto tělesa je odhad pro divergenci v daném bodě.
```


Přesnou divergenci získáme postupem uvedeným v předchozí poznámce, pokud limitním přechodem stáhneme rozměry tělesa k nule. 

Pokud se daném místě množství veličiny nemění s časem, tj. žádná veličina se tam neakumuluje ani neubývá, mluvíme o stacionárním proudění a stacionárním poli. Situace se zjednoduší, protože potom divergence souvisí jenom s přítomností zdrojů a spotřebičů.

```{prf:remark} Praktická interpretace divergence stacionárního pole
:nonumber:
 Pokud při ustáleném proudění je v některém místě divergence kladná, znamená to, že v tomto místě musí být zdroj této veličiny. Pokud je záporná, je v daném místě spotřebič. Pro pohodlí při popisu toku bereme spotřebiče jako záporné zdroje. Vektorové pole, jehož divergence je rovna nule, se nazývá **nezřídlové pole**. To proto, že pokud toto pole popisuje ustálený tok, tak se jedná o tok v prostředí bez zdrojů a spotřebičů.
```


Ze střední školy z fyziky umíme modelovat vektorové pole
pomocí siločar. Siločáry nezřídlového pole nikde nezačínají ani
nekončí a jsou to uzavřené křivky. 
Například stacionární magnetické pole je
nezřídlové. Absence zdrojů magnetického pole se projevuje tak, že rozříznutím tyčového magnetu vzniknou dva menší plnohodnotné magnety. Nevznikne samostatný jižní pól a samostatný severní pól magnetu. To je rozdíl oproti poli elektrickému, kdy rozdělením tyče s opačně nabitými konci vznikne jedna kladně nabitá a jedna záporně nabitá tyč poloviční délky.

## Výpočet gradientu a divergence

https://youtu.be/UzT_PDj5ukY

Viz přednáška. 

## Rovnice kontinuity

https://youtu.be/_iHeE-9DJrA

\iffalse 

<div class='obtekat'>

```{figure} ucto.jpg
Rovnice kontinuity je vlastně bilance zisků a ztrát pro danou stavovou veličinu v libovolném bodě. Zdroj: pixabay.com
```

</div>

\fi

* Přírůstek stavové veličiny za jednotku času v jednotkovém objemu
  (nebo ploše, nebo délce, podle dimenzionality úlohy) je derivace
  hustoty $u$ podle času.
  $$\text{Přírůstek}=\frac{\partial u}{\partial t}$$
*  Přírůstek veličiny v jednotkovém objemu (nebo ploše, nebo délce) za
  jednotku času způsobený tokem $\vec \jmath$ je záporně vzatá divergence
  vektorového pole $\vec \jmath$. Tento přírůstek je způsobený snížením
  toku, proto má předřazeno záporné znaménko.
$$    \text{
        Přírůstek způsobený tokem
}=-\nabla\cdot \vec \jmath$$

Matematickou formulací celkové bilance  je **rovnice kontinuity**.
$$
      {\frac{\partial u}{\partial t}=\sigma -\nabla\cdot \vec \jmath}   $$

>Poznámka (fyzikální interpretace členů rovnice kontinuity).
>
>* Člen $\frac{\partial u}{\partial t}$ udává, jak rychle se roste hustota stavové veličiny $u$ v daném místě a čase.
>* Člen $\sigma$ udává vydatnost zdrojů stavové veličiny, přičemž spotřebiče jsou uvažovány jako zdroje záporné vydatnosti. Tento člen tedy udává, kolik stavové veličiny v tomto místě vzniká v jednotkovém objemu za jednotku času.
>* Člen $\nabla\cdot \vec j$ udává v daném bodě změnu ve velikosti proudění přenášejícím stavovou veličinu. Přesněji, udává, o kolik více veličiny z daného místa vyteče ve srovnání s množstvím veličiny, které do tohoto místa vteče. Jinak řečeno, udává, o kolik zesílí v daném místě tok $\vec \jmath$. My potřebujeme mít zachyceno zeslabení (množství které chybí v toku se "použije" na akumulaci veličiny v daném místě) a proto uvažujeme záporně vzatou divergenci, tj. $-\nabla\cdot \vec j$.
>* Pokud zdroje stavové veličiny neexistují, jedná se o *bezzdrojovou rovnici* a klademe $\sigma=0$.
>* Pokud studujeme systém v ustáleném stavu, kdy se stavová veličina nemění v čase, je člen $\frac{\partial u}{\partial t}$ na levé straně nulový. V tomto případě mluvíme o *stacionárním stavu* a *stacionární rovnici kontinuity*. Stacionární rovnice kontinuity typicky popisuje systémy, které byly dostatečně dlouhou dobu ve stabilních podmínkách a dosáhly rovnovážného stavu.
>* Viděli jsme, že za určitých podmínek mohou některé členy v rovnici kontinuty chybět. Naopak člen $\nabla\cdot \vec j$ charakterizující změny v toku je v rovnici kontinuity přítomen vždy. Bez něj by rovnice kontinuity ztratila smysl (resp. redukovala by se na triviální případ, kdy veličina v daném místě vzniká danou rychlostí a zůstává zde, tj. problém řešitelný čistě integrováním).

V matematice často rovnici kontinuity uvažujeme ve výše uvedeném tvaru.  Při
praktickém použití většinou preferujeme názornou interpretaci
jednotlivých veličin a proto se v rovnici mohou objevit další
konstanty úměrnosti, které umožní sladit jednotky a fyzikální
interpretaci členů. Někdy se naopak snažíme konstanty co nejvíce
redukovat metodami transformace popsanými v přednášce o diferenciálních rovnicích. Proto volíme vhodné násobky veličin
vystupujících v matematické formulaci tak, aby se co nejvíce konstant
eliminovalo, případně shluklo do jediné veličiny. Zkušenosti ukazují,
že je vhodné volit veličiny bezrozměrné. Například v publikaci
P. Horáček, Fyzikální a mechanické vlastnosti dřeva I je zavedena
[bezrozměrná vlhkost, bezrozměrný čas a bezrozměrná
vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9180;lang=cz)
na straně 61 pro rovnici popisující difuzi a [charakteristická délka,
Biotovo číslo (bezrozměrná tepelná vodivost) a bezrozměrná teplota,
bezrozměrný čas a bezrozměrná
vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9182;lang=cz)
pro rovnici popisující vedení tepla na stranách 88 a 89.

V této rovnici není zahrnut případ, kdy se veličina přenáší ještě i prouděním hmotného prostředí (konvekce).

\iffalse

`ww2:problems/difuzni_rce/interpretace_clenu.pg`

\fi

## Rovnice mělké vody

<div class='obtekat'>

\iffalse 

```{figure} ricka.jpg
Rovnici kontiuity známe ze středoškolské fyziky pro ustálené proudění. Naše obecnější formulace umí zachytit i nestacionární stav. Zdroj: pixabay.
```

\fi

</div>

Rovnici kontinuity můžeme použít pro popis vody v korytě. Úloha je jednodimenzionální a tok $Q$ je skalární veličina. Divergence toku se díky jednodimenzionálnosti redukuje na derivaci podle prostorové proměnné $\frac{\partial Q}{\partial x}$. Zachovávající se veličinou je množství vody. Hustota zachovávající se veličiny je množství vody na metr délky toku, tj. _průtočný průřez_ $A$ (obsah průřezu říčního toku  v daném místě). Zdroje zpravidla neuvažujeme, tj. $\sigma=0$. Rovnice kontinuity má potom tvar 
$$
      {\frac{\partial A}{\partial t}= - {\frac{\partial Q}{\partial x}}}
$$
a nazývá se Saint-Venantova rovnice nebo též *rovnice mělké vody*. Tato rovnice se používá při popisu *proudění v korytě* nebo při modelování *vln tsunami*.

V rovnici jsou dvě funkce, tok $Q$ definující pohyb stavové veličiny a
průřez $A$ definující množství stavové veličiny. Někdy je vhodnější
pracovat se stavovou veličinou $h$ udávající výšku hladiny. Jak jsme
zmínili v úvodní přednášce o derivacích, je derivace $\frac{\mathrm
dA}{\mathrm d h}$ rovna šířce hladiny. Abychom mohli celou rovnici
převést na tvar pracující jenom se stavovou veličinou $h$, je nutné udělat
nějaké dodatečné předpoklady, jako například pracovat s konkrétním
tvarem koryta.

## Proudění tekutiny v mechanice kontinua

\iffalse

<div class='obtekat'>

```{figure} med.jpg
Rovnice mechaniky kontinua dokáží popsat i děje, které se odehrávají v tekutinách tekoucích jinak, než voda nebo ideální tekutina. Běžným příkladem je med, technicky významným například beton. Kromě rovnice kontinuity je nutné dodat ještě další fyzikální vztahy. Zdroj: pixabay.com.
```

</div>

\fi

V mechanice kontinua podobně jako u vedení tepla neuvažujeme zdroje. Stavovou veličinou je hustota $\rho$, která popisuje množství látky v daném místě. Tato látka je přenášena tokem, který je roven součinu rychlosti $\vec u$ a hustoty $\rho$. Rovnice kontinuity popisující proudění dané rychlostí $\vec u$ má poté tvar
$$\frac{\partial \rho}{\partial t} + \nabla\cdot (\rho \vec {u}) = 0,$$
kde $\rho$ je hustota. 
Tato rovnice napsána pro vzduch je jednou z rovnic používaných při [modelování vývoje počasí](http://www-history.mcs.st-and.ac.uk/HistTopics/Weather_forecasts.html)

Pro nestlačitelnou tekutinu je hustota konstantní, což eliminuje
nestacionární člen a redukuje rovnici na $$ \nabla\cdot\vec
u =0.$$ Důsledkem této rovnosti je zvýšení rychlosti molekul
pohybující se nestlačitelné tekutiny při proudění místem s menším
průřezem.

[Středoškolský makroskopický tvar](https://cs.wikipedia.org/wiki/Rovnice_kontinuity#Rovnice_kontinuity_ve_st%C5%99edo%C5%A1kolsk%C3%A9_fyzice) jednorozměrné rovnice kontinuity pro proudění nestlačitelné tekutiny je $$S u = \mathrm{konst}.$$

## Difuzní rovnice

https://youtu.be/MH8IzenZZCo

Difuzní rovnice je rovnice kontiuity s dosazeným konstitučním vztahem
pro tok.  Použijeme-li pro kvantifikaci souvislosti toku a gradientu
lineární aproximaci, je možné psát
$$      \vec \jmath=-D\nabla u,$$
kde $D$ konstanta
úměrnosti. Pokud tok $\vec \jmath$ a gradient $\nabla u$ leží v jedné přímce,
je $D$ reálné číslo, jinak je $D$ matice. Například při
studiu pohybu vody ve dřevě se voda řídí nejen směrem maximálního
poklesu vlhkosti, ale stáčí se současně do podélného směru, ve kterém dřevo
vede vlhkost nejlépe. V takovém případě je $D$ matice. 
Spojením rovnice kontinuity
$$
      {\frac{\partial u}{\partial t}=\sigma -\nabla\cdot \vec \jmath}   $$
a vztahu  pro tok stavové veličiny dostáváme rovnici
$$
      {\frac{\partial u}{\partial t}=\sigma - \nabla\cdot \bigl(-D\nabla u\bigr)}.$$
      Tuto rovici je možno upravit na tvar
$$
      {\frac{\partial u}{\partial t}=\sigma + \nabla\cdot \bigl(D\nabla u\bigr)},$$
který se nazývá *difuzní rovnice*.

```{prf:remark} Fyzikální interpretace rovnice difuzní rovnice
:nonumber:

* Člen $\frac{\partial u}{\partial t}$ udává, jak rychle se mění hustota stavové veličiny $u$. Je stejný jako v rovnici kontinuity.
* Člen $\sigma$ udává vydatnost zdrojů stavové veličiny. Je stejný jako v rovnici kontinuity.
* Člen $\nabla u$ udává nerovnoměrnost v prostorovém rozložení stavové veličiny. Pomocí difuzní matice $D$ a konstitutivního zákona tuto nerovnoměrnost přepočítáme na tok, který se snaží uvažovanou nerovnoměrnost vyrovnat. Tento tok je reprezentován výrazem $-D\nabla u$.
* Záporně vzatá divergence toku udává, jak tok v daném místě ztrácí na intenzitě. Vzhledem k zápornému znaménku v konstitutivním zákoně má záporně vzatá divergence tvar $$\nabla\cdot \bigl(D\nabla u\bigr).$$ Představuje přírůstek hustoty stavové veličiny v daném místě za jednotku času, způsobený zeslábnutím toku.
* Rovnice jako celek vyjadřuje, že navýšení hustoty stavové veličiny (tj. množství stavové veličiny v jednotkovém objemu) je součtem navýšení díky zdrojům a navýšení díky zeslabení toku v daném místě.
```

## Vedení tepla

\iffalse

<div class='obtekat'>

```{figure} teplo.jpg
Stromy umí ochlazovat své okolí. Ulice v Melbourne vyfocená termokamerou to dokazuje. A difuzní rovnice toto dokáže modelovat. Photograph: City of Melbourne. Zdroj: theguardian.com.
```

</div>

\fi

Důležitým speciálním případem difuzní rovnice je rovnice vedení tepla.
Stavovou veličinou, která se zachovává v úlohách s vedením tepla, je vnitřní energie ve
formě tepla. Zpravidla nemá smysl uvažovat členy vyjadřující
zdroje, tj. $\sigma =0$. Protože teplo neměříme přímo, je vhodnější
model formulovat pro teplotu $T$. Jsou-li $\varrho$ a $c$ po řadě hustota a měrná tepelná kapacita materiálu, má člen vyjadřující změnu hustoty
energie v daném místě tvar
$\varrho c\frac{\partial T}{\partial t}.$ Úměrnost mezi gradientem
teploty a tokem tepla zprostředkovává
*Fourierův zákon*. Difuzní rovnice má v tomto případě tvar
$${\varrho c\frac{\partial T}{\partial t}=  \nabla\cdot\bigl(D\nabla T\bigr)}$$

```{prf:remark} Fyzikální interpretace rovnice vedení tepla
:nonumber:

* Veličina $\frac{\partial T}{\partial t}$ udává rychlost růstu teploty tělesa a koeficient $\rho c$ tuto hodnotu přepočítává na údaj, jak rychle roste vnitřní energie tělesa (kinetická energie molekul.)
* Výraz $D\nabla T$ udává (až na znaménko), jak se nerovnoměrnost v rozložení teploty vyrovnává tokem tepla. Přesněji, tok tepla je $-D\nabla T$.
* Člen $\nabla\cdot(D\nabla T)$ udává, kolik tepla z celkového toku v daném místě zůstává a podílí se na zvýšení teploty. Vzhledem k absenci zdrojů je to také jediný mechanismus, jak v daném místě může vnitřní energie přibývat či ubývat.
* Rovnice jako celek vyjadřuje to, že pokud z daného místa více energie odtéká, než kolik do místa proudí, dojde v tomto místě k odpovídajícímu snížení teploty. V tomto bodě je totiž divegrence toku $\nabla\cdot (-D\nabla T)$ kladná a výraz z rovnice $\nabla\cdot (D\nabla T)$ je proto záporný.
```


\iffalse

<div class='obtekat'>

```{figure} vrstvy.png
Na rozhraní vrstev ve vrstveném materiálu je spojité teplotní pole a tok tepla.  Zdroj: Cengel, Ghajar: Heat and Mass Transfer.
```

</div>

\fi

\iffalse

`ww2:problems/difuzni_rce/vedeni_tepla_vypocet.pg`

\fi

Tato rovnice je zobecnění rovnice vedení tepla v jedné dimenzi, kterou jsme
odvodili primitivními prostředky (jenom pomocí parciálních derivací, bez gradientu a divergence) ve tvaru
$$\rho c\frac{\partial T}{\partial t}=\frac{\partial}{\partial x}\left(D\frac{\partial T}{\partial x}\right)$$
v úvodní přednášce.

Rovnice vedení tepla se používá například při *tepelné ochraně budov*, při modelování *tepelných ostrovů* v krajině, při *tepelné modifikaci dřeva*, nebo při studiu *permafrostu*. 

V literatuře věnované problematice dřeva se rovnice vedení tepla ve dřevě označuje jako Druhý Fourierův zákon (P. Horáček, Fyzikální a mechanické vlastnosti dřeva I, str. 88).

V některých případech nemusí být člen charakterizující zdroje
nulový. Teplo může vznikat například při tření nebo při průchodu
elektrického proudu transformací z jiného druhu energie. Dále teplo vzniká například při betonování po [přidání vody do cementu](http://www.ebeton.cz/pojmy/hydratacni-teplo), známý je problém jak [uchladit Hooverovu přehradu](http://www.ebeton.cz/encyklopedie/hooverova-prehrada) při stavbě.

## Voda v porézním materiálu 

\iffalse

<div class='obtekat'>

```{figure} drevo.jpg
Difuzní rovnice se používá k modelování sušení dřeva. Zdroj: pixabay.com.
```

</div>

\fi

V porézním materiálu voda prostupuje materiálem a zachovává se její
množství, což bude stavová veličina. Hustotu tohoto množství, tj. obsah vody v jednotce
objemu, označíme $c$ a pro tuto veličinu formulujeme matematický
model. Zdroje neuvažujeme. Úměrnost mezi gradientem koncentrace vody a
jejím tokem zprostředkovává *Fickův
zákon*. Modelem je potom  difuzní rovnice bez zdrojů.
$$
      {\frac{\partial c}{\partial t}= \nabla\cdot \bigl(D\nabla c\bigr)}
	  $$
  Tato rovnice se používá například při modelování procesu
  *sušení dřeva* v sušárnách nebo při modelování *dřeva
    ve vlhkém prostředí*. Stejná rovnice napsaná pro vzduch se používá
  k modelování proudění v atmosféře při *předpovídání počasí*.

V literatuře věnované problematice dřeva se rovnice difuze použitá na modelování vlhkosti ve dřevě označuje jako Druhý Fickův zákon (A. Požgaj a kol., Štruktúra a vlastnosti dreva, str. 202, P. Horáček, Fyzikální a mechanické vlastnosti dřeva I, str. 60).

V praxi je dřevo často s jistou přesností homogenní, ale difuzní
koeficient dřeva závisí na vlhkosti, tedy vztah mezi gradientem
vlhkosti a difuzním tokem není lineární. Přesto i v tomto případě
používáme Fickův zákon, ovšem složky difuzního koeficientu
nepovažujeme za konstanty, jsou závislé na $c$ a jejím prostřednictvím
i na $x$.

## Rovnice podzemní vody

\iffalse

<div class='obtekat'>

```{figure} voda.jpg
Difuzní rovnice umí popsat proudění podzemní vody. Díky tomu dokážeme zabránit kontaminacím pitné vody z chemických provozů. Zdroj: pixabay.com.
```

</div>

\fi

Proudění podzemní vody je vlastně úloha s řekou se zasypaným
korytem. Taková voda teče ve srovnání s povrchovou vodou velmi pomalu,
protože prosakuje půdou. Prostor, kde se podzemní voda nachází, se
nazývá *zvodeň*. Stejně jako řeka v korytě na povrchu, i voda
v podzemní zvodni teče v jistém smyslu "z kopce". V tomto případě
však kromě nadmořské výšky může hrát roli i rozdíl tlaků nebo další
efekty. Vliv všech těchto efektů shrnujeme do jediného pojmu
*piezometrická výška*. Směr "z kopce" pro podzemní vodu je
poté směr poklesu piezometrické výšky. V daném místě se může voda
hromadit, to poznáme nárůstem hladiny spodní vody. Také může
z hlediska zvodně část vody zanikat, například pokud je zde čerpaná
studna nebo průsak do jiné zvodně. Voda může ve zvodni i vznikat,
například zasakovacím vrtem nebo průsakem dešťových srážek. Pokud do
celkové bilance započteme rozdíl mezi přítokem a odtokem a všechny
zdroje a spotřebiče, množství vody se zachovává.

Podzemní zvodeň je typickým porézním materiálem, přesto k modelování
vody v tomto prostředí přistupujeme speciálním způsobem. Úloha se většinou uvažuje ve dvou dimenzích, protože
horizontální rozměry zvodně jsou mnohem větší než její
hloubka. Zachovává se množství vody, ale stejně
jako u vedení tepla je výhodné formulovat model pro lépe
měřitelnou veličinu, *piezometrickou výšku*
$h$. Přírůstek množství podzemní vody za časovou jednotku na jednotkové ploše v daném
místě zvodně má tvar $S_S \frac{\partial h}{\partial t}$, kde $S_S$ je
*specifická zásobnost*.  Úměrnost mezi gradientem piezometrické výšky a
filtračním tokem  zprostředkovává *Darcyho
zákon*. Difuzní rovnice  má (s konstantou úměrnosti $T$, *transmisivitou*) tvar
$$ {S_S\frac{\partial h}{\partial t}=  \sigma + \nabla\cdot \bigl(T\nabla h\bigr).}$$ Tato rovnice se nazývá *rovnice podzemní vody*. Zdroje jsou nejčastěji zasakovací nebo odvodňovací vrty, dále studny, poldry, výkopy nebo zářezy. Informace získané z rovnice podzemní vody se využívají například
  k ochraně lomů, dolů a stavebních jam před *zaplavením*, k hospodaření s *pitnou vodou*,  k ochraně před šířením *kontaminace z chemických
  provozů*. Aplikace jsou dále v detekci zdroje kontaminace pitné vody a odhadu rychlosti  šíření kontaminace, včetně 
*kontaminace slanou mořskou vodou* v přímořských oblastech.

U proudění s napjatou hladinou (mezi dvěma nepropustnými vrstvami, angl. *confined aquifer*) transmisitiva závisí pouze na fyzikálních vlastnostech zvodně. Například pro homogenní izotropní materiál je konstantní. U proudění s volnou hladinou (bez horní nepropustné vrstvy, angl. *unconfined aquifer*) je transmisivita úměrná tloušťce vrstvy obsahující vodu. Zpravidla nulovou hodnotu piezometrické hladiny volíme na dolní nepropustné vrstvě a potom platí $T=kh$, kde $k$ závisí pouze na fyzikálních vlastnostech půdy. Proto se často rovnice podzemní vody pro proudění s volnou hladinou zapisuje ve tvaru
$$ {S_S\frac{\partial h}{\partial t}=  \sigma + \nabla\cdot \bigl(kh\nabla h\bigr).}$$

## Rovnice vedení tepla ve 2D v různých podmínkách

https://youtu.be/5hy6lB1O4KQ

\iffalse

<div class='obtekat'>

```{figure} VCJR_modifikace_pravidelne.jpg
Teplotní modifikace dřeva ve VCJR v Útěchově. Díky jednoduché geometrii vzorků je možno provést i přesný analytický výpočet teplotního pole. Výřez ukazuje detail čtyř vzorků. Jeden z nich je nařezán šikmo. V takovém případě je výpočet mnohem obtížnější než u vzorků, jejichž tvar respektuje anatomické směry ve dřevě. Zdroj: J. Dömény.
```

```{figure} VCJR_sindel.jpg
Teplotní modifikace šindele ve VCJR v Útěchově. Řídí se stejnou rovnicí jako hranoly na obrázku výše. Vinou komplikovaného tvaru je však matematické modelování teplotního pole možné jenom numerickou cestou. Skutečně, v podobných úlohách hraje geometrie úlohy důležitou roli a netriviální geometrie zpravidla znemožní efektivní řešení analytickou cestou. Zdroj: J. Dömény.
```

```{figure} rtb.png
Nestacionární rovnice vedení tepla. Měření teplotních charakteristik pomocí sledování odezvy na teplotní impuls na ÚNOD LDF MENDELU. Zdroj: R. Slávik.
```

</div>

\fi

Uvažujme rovnici vedení tepla ve dvou rozměrech a v prostředí bez zdrojů.

$$\rho c\frac{\partial T}{\partial t}=\nabla\cdot (D\nabla T)$$ (VP3)

### Stacionární stav

Stacionární stav znamená, že stavové veličiny nezávisí na čase. Derivace podle času je v takovém případě nulová. Rovnice {eq}`VP3` se redukuje na 
$$\nabla\cdot (D\nabla T)=0.$$

### Homogenní izotropní materiál a lineární materiálové vztahy

Materiál má ve všech místech (homogenní) a ve všech směrech (izotropní) stejné vlastnosti.
Veličina $D$ je reálná skalární veličina (konstanta).

Podle pravidla derivace konstantního násobku se rovnice {eq}`VP3` redukuje na  
$$\rho c\frac{\partial T}{\partial t}=D\nabla\cdot (\nabla T)$$
a ve složkách
$$\rho c\frac{\partial T}{\partial t}=D\left(\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}\right).$$
Pro $\tau=\frac{Dt}{\rho c}$ (změna jednotky času) dostáváme
$$\frac{\partial T}{\partial \tau}=\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}.$$

### Ortotropní materiál, nehomogenní nebo nelineární

Materiál má dva charakteristické směry související s rovinami
symetrie. Zvolíme soustavu souřadnic tak, aby osy byly orientovány ve
směru vlastních vektorů.

Veličina $D$ je diagonální matice. Pro $$D=\begin{pmatrix}D_x & 0\\ 0& D_y\end{pmatrix}$$ je tvar rovnice {eq}`VP3` ve složkách
$$\rho c\frac{\partial T}{\partial t}=\frac{\partial }{\partial x}\left(D_x\frac{\partial T}{\partial x}\right)
+\frac{\partial }{\partial y}\left(D_y\frac{\partial T}{\partial y}\right).$$

### Homogenní ortotropní materiál a lineární materiálové vztahy

Materiál má dva charakteristické směry související s rovinami symetrie a materiálové charakteristiky jsou ve všech místech stejné a nezávislá na $T$.
Stejné jako předchozí případ, ale $D_x$ a $D_y$ jsou konstanty. Podle pravidla pro derivaci konstantního násobku se rovnice {eq}`VP3` redukuje na 
$$\rho c\frac{\partial T}{\partial t}=D_x\frac{\partial^2 T}{\partial x^2}+D_y\frac{\partial^2 T}{\partial y^2}.$$

## Umění identifikace předpokladů z tvaru difuzní rovnice

Jasná kuchařka, jak identifikovat předpoklady vedoucí ke konkrétní formě difuzní rovnice může vypadat násedovně. Obecný tvar v kartézských souřadnicích je
$$\frac{\partial u}{\partial t} =\sigma +
\frac{\partial }{\partial x}\left(D_x\frac{\partial u}{\partial x}\right)+
\frac{\partial }{\partial y}\left(D_y\frac{\partial u}{\partial y}\right)+
\frac{\partial }{\partial z}\left(D_z\frac{\partial u}{\partial z}\right)
$$
a pokud máte před sebou podobnou rovnici, ve které některý člen chybí, znamená to, že tato rovnice v sobě již obsahuje jisté předpoklady. Ty se pokusíme identifikovat. Některý člen může být lehce modifikovaný, například a levé straně mohou figurovat dodatečné multiplikativní konstanty (například v případě rovnice vedení tepla) nebo člen popisující zdroje může být nekonstantní (například při studiu vývoje populace se zahrnutím prostorového rozložení používáme logistický růst $\sigma = ru\left(1-\frac uK\right)$), zajímavé však pro nás jsou podstatné odlišnosti shrnuté v následujících odrážkách. Vždy je to "něco za něco". Jednodušší rovnice se lépe dále zpracovává, ale neumí zachytit plnou škálu efektů, které jsou v obecné rovnici.

* Je v rovnici člen $\frac{\partial u}{\partial t}$ s derivací podle času? Pokud ano, je rovnice _nestacionární_ a dokáže popsat časový vývoj děje. Pokud ne, jedná se o _stacionánrní_ rovnici popisující děj po dosažení ustáleného stavu. Stacionární rovnice je jednodušší, ale nedokáže zachytit časový vývoj.
* Je v rovnici člen bez časové a prostorové derivace? Tj. v našem označení $\sigma$? Pokud ano, popisuje tento člen vydatnost zdrojů nebo spotřebičů a rovnice je schopna zachytit situace, kdy stavová veličina vzniká nebo zaniká. Pokud ne, jedná se o _bezzdrojovou rovnici_. Takové rovnice popisuje stav, kdy se stavová veličina může jenom přemisťovat nebo kumulovat. Bezzdrojová rovnice je jednodušší, ale nedokáže modelovat vznik či zánik stavové veličiny.
* Jsou přítomny všechny prostorové souřadnice, nebo jenom některé? Počet prostorových souřadnic defiuje _dimenzi problému_, tj. určuje, zda se jedná o úlohu v prostoru, v rovině nebo na přímce.
* Jsou všechny difuzní koeficienty stejné (například $D$), nebo jsou odlišeny (například indexy $D_x$, $D_y$, $D_z$)? Pokud jsou stejné, jedná se o _izotropní_ materiál a rovnice dokáže popsat pouze materiál mající ve všech směrech stejné vlastnosti. Pokud jsou difuzní koeficienty odlišeny, jedná se o _anizotropní_ nebo _ortotropní_ materiál a dokážeme s ní popsat i materiály mající díky své struktuře jiné vlastnosti v jednotlivých směrech.
* Jsou difuzní koeficienty uvnitř derivací ve členech typu $$\frac{\partial }{\partial x}\left(D_x\frac{\partial u}{\partial x}\right)$$ nebo jsou difuzní členy zjednodušeny do tvaru $$D_x\frac{\partial ^2 u}{\partial x^2}$$ s druhými derivacemi? Pokud jsou zjednodušeny do druhého tvaru se součinem difuzního koeficientu a druhé derivace, znamená to, že rovnice je sice jednodušší, ale rovnice je schopna popsat pouze materiál, který je _homogenní_ a konstitutivní zákon v tomto materiálu je _lineární_. V opačném případě (nehomogenita materiálu, nelinearita materiálu, případně obojí) necháváme difuzní koeficienty uvnitř derivace, tak jak to je v obecném případě. Rovnice je komplikovanější, ale umožňuje práci s obecnějšími materiály.

\iffalse

`ww2:problems/difuzni_rce/predpoklady.pg`

\fi

## Shrnutí, hlavní myšlenky

https://youtu.be/TjyB3kP2uXE

\iffalse

<div class='obtekat'>

```{figure} ../message.jpg
A jaká je hlavní message? Zdroj: pixabay.com
```

</div>

\fi

* Pomocí gradientu a aparátu lineární algebry můžeme vyjádřit vztah mezi pohybem fyzikální veličiny a mechanismem, který tento pohyb iniciuje. Většinou se jedná o vztah mezi vektorovým polem toku a gradientem jistého skalárního pole. 
* Pomocí parciálních derivací a divergence dokážeme určit, jestli se v nějakém místě veličina proudící tímto místem "ztrácí" nebo "přibývá".
* Dokážeme dokonce s rozumnou interpretací, čím případné ubývání přenášené veličiny může být způsobeno (zdroje a spotřebiče nebo akumulace v daném místě), zformulovat rovnici, která dané proudění plně popisuje. Výsledkem jsou rovnice vedení tepla, rovnice difuze, rovnice proudění podzemní vody a jiné.
* Obecná rovnice odvozená podle předchozích bodů je obecná a pro práci na konkrétní úloze se ji snažíme nějak blíže specifikovat. Například zjednodušit, pokud máme informaci o charakteru materiálových vztahů (lineární/nelineární) a materiálu (homogenní/nehomogenní). Jiným zjednodušením je, pokud se zajímáme o stacionární stav, který se nastolí po dosažení rovnováhy.
* Posláním široké škály příkladů různých specifikací rovnice kontinuity (vedení tepla, proudění povrchové a podzemní vody a další) je, aby si student uvědomil široký záběr obecné formulace rovnice kontinuity. Na zkoušku se naučte obecnou rovnici a jenom informativně si přečtěte její speciální případy. Obory pracující se dřevem (dřevařství, nábytek, dřevostavby) si uložte do paměti rovnice popisující modelování tepla a vlhkosti ve dřevě. Budou se vám hodit  ve studiu. Na krajinářství se zase zaměřte na modelování vody, mělké i podzemní.

## Shrnutí více matematickou formou

* Ukázali jsme si, že má smysl založit model na bilanci, která vyjadřuje, že rychlost růstu stavové veličiny je součtem příspěvku vygenerovaného zdroji a příspěvku přineseného tokem.
* Rychlost růstu je derivace podle času, $$\frac {\partial u}{\partial t}.$$
* Příspěvek přinesený tokem je roven zeslabení toku v daném místě. Zeslabení toku vypočteme jako záporně vzaté zesílení toku, tj. záporně vzatou divergenci toku, $$-\nabla\cdot \vec j.$$
* Celková bilance se poté nazývá rovnice kontinuity a má tvar $$
\frac {\partial u}{\partial t}=\sigma - \nabla\cdot \vec j. $$
* Tok $\vec j$ zpravidla vypočteme jako záporně vzatý gradient stavové veličiny vynásobený difuzní maticí, tj. $$\vec j=-D\nabla u.$$ 
* Spojením předchozích vztahů dostáváme difuzní rovnici 
$$
\frac {\partial u}{\partial t}=\sigma + \nabla\cdot \left(D\nabla u\right). $$ To je rovnice popisující obecně transport energie nebo hmoty prostředím. Například vedení tepla nebo difuzi vody při sušení dřeva.
* Pro konkrétní výpočet je často nutné rovnici zapsat v souřadnicích. Například pokud máme dvojrozměrný model a směr souřadných os zvolíme ve vlastních směrech matice $D$ (potom matice $D$ bude diagonální s diagonálními prvky například $D_x$ a $D_y$), má difuzní rovnice tvar 
$$ \frac {\partial u}{\partial t}=\sigma + \frac{\partial }{\partial x}\left(D_x \frac{\partial u}{\partial x}\right ) + \frac{\partial }{\partial y}\left(D_y \frac{\partial u}{\partial y}\right ). $$
* Pokud je materiál homogení a má lineární materiálovou odezvu, je dokonce možné rovnici dále zjednodušit na 

$$ \frac {\partial u}{\partial t}=\sigma + D_x\frac{\partial^2 u }{\partial x^2 } + D_y\frac{\partial^2 u }{\partial y^2 } .
$$ (N)

Tato formulace je jednodušší než předešlá, protože obsahuje druhé derivace místo kvaziderivací.
* Pokud je rovnice například stacionární (stavová veličina nezávisí na čase, derivace podle času je nulová), bezzdrojová (neobsahuje zdroje ani spotřebiče, veličina $\sigma$ je nulová), z homogenního a lineárního materiálu (viz předchozí bod) redukuje se rovnice {eq}`N` na  

$$ 0= D_x\frac{\partial^2 u }{\partial x^2 } + D_y\frac{\partial^2 u }{\partial y^2 } . 
$$ (S)

Tato rovnice je jednodušší než "plná rovnice" {eq}`N` a proto ji dokážeme řešit i ve složitějších podmínkách. Někdy například umíme vyřešit nestacionární rovnici {eq}`N` a máme dynamiku jak rychle roste stavová veličina, například jak rychle roste teplota v materiálu. To je nejlepší scénář, někdy však může být nerealizovatelný. Někdy ale umíme vyřešit jenom stacionární rovnici {eq}`S` a najdeme jenom rozložení stavové veličiny po dosažení rovnovážného stavu. To je také dobrá a užitečná informace sama o sobě. Navíc může sloužit jako odrazový můstek k řešení nestacionární rovnice {eq}`N` tak, že od stacionárního řešení postupujeme zpětně v čase.
* Pokud je materiál z předchozího bodu ještě navíc izotropní, tj.  pokud má stejné vlastnosti ve všech směrech, je $D_x=D_y$ a rovnici je možno vydělit do tvaru $$ 0= \frac{\partial^2 u }{\partial x^2 } + \frac{\partial^2 u }{\partial y^2 } .$$ O této rovnici si ukážeme, že zapojením druhých diferencí pro numerickou aproximaci druhé derivace se model redukuje na soustavu lineárních rovnic.

## Praktická aplikace (zajímavost z jiné oblasti než nauky o materiálu)

Jste frustrovaní, že k rovnici nemáme řešení? Bohužel ho není obecně možné najít. Rovnici dokážeme přesně vyřešit jenom ve velmi speciálních případech. I bez vyřešení však z rovnice získáváme užitečné informace. Navíc rovnice může být stavebním kamenem složitějšího modelu. Místo slibů konkrétní příklad zase na jiné (ale aktuální) téma. 

V článku  [A Local and Time Resolution of the COVID-19 Propagation—A
Two-Dimensional Approach for Germany Including Diffusion
Phenomena to Describe the Spatial Spread of the
COVID-19 Pandemic](https://arxiv.org/pdf/2101.12011)
je prostorové šíření epidemi COVID modelováno difuzní rovnicí (1) ve tvaru 
$$\frac{\partial c}{\partial t}=q+\nabla\cdot \left(D\nabla c\right),$$
což je přesně rovnice, se kterou jsme pracovali zde. Je to rovnice ve své  neobecnější formě, aby bylo možno zachytit 

* časový vývoj (o ten nám jde), 
* nehomogenitu v šíření (například ve městech je jiná rychlost šíření než na venkově) a
* existenci zdrojů (vir se umí množit). 

Tato rovnice se řeší pro Německo, což znemožňuje kvůli složité geometrii nalezení analytického přesného řešení. To totiž umíme v prakticky použitelné formě najít jenom pro obdélník a několik málo dalších množin. Proto se tento model řeší numericky. V prvním odstavci podkapitoly 4 článku je numerický model pro jednotlivé spolkové země označen číslem (7) a redukce na soustavu lineárních rovnic (8). V následujícím odstavci je zmíněna Jacobiho metoda pro numerické řešení soustav lineárních rovnic. S touto metodou jsme se setkali v předchozí přednášce o soustavách rovnic. 

Model je dokonce možné doplnit dynamikou růstu zahrnující nárůst nejenom vlivem difuze, ale i vlivem množení viru v daném místě. Přesněji, v odstavci 6 odkazovaného článku se model doplňuje rovnicemi (9) až (11)  ve tvaru
$$\begin{aligned}
\frac{\mathrm dS_j}{\mathrm dt}&=-\kappa_j\frac {I_j}{N_j}{S_j},\\
\frac{\mathrm dI_j}{\mathrm dt}&=\kappa_j\frac {I_j}{N_j}{S_j}-\eta_j I_j,\\
\frac{\mathrm dR_j}{\mathrm dt}&=\eta_j I_j.
\end{aligned} $$
Toto jsou již naši staří známí ze světa derivací funkce jedné proměnné. Například první rovnice vyjadřuje, že počet $S_j$ lidí zdravých a náchylných k onemocnění COVID19 ve spolkové zemi s indexem $j$ se snižuje rychlostí přímo úměrnou současně množství náchylných lidí a množství $I_j$ infikovaných lidí a nepřímo úměrnou celkové velikosti populace v této zemi $N_j$. Konstanta úměrnosti je $\kappa_j$ a abychom se mohli spolehnout na to, že tato konstanta je kladná, je úbytek skupiny dosud zdravých lidí zachycen záporným znaménkem na pravé straně rovnice. Podobně je možné interpretovat další rovnice, je to vlastně klasický [SIR model epidemie](https://www.matfyz.cz/clanky/matematika-koronaviru-matematicke-modely-sireni-epidemie). Prolistujete si výše odkazovaný anglický článek o modelování epidemie v Německu a všimněte si, že se nic ručně nemusí počítat. Rovnice se nasimulují v počítači a člověk jenom plní ty úlohy, které počítače neumí a nikdy umět nemůžou: sestaví model na základě své představy o fungování procesu a poté interpretuje výstup ze simulace.

