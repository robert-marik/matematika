# Diferenciální rovnice 

https://youtu.be/gU6ClJwLFs0

> V této přednášce se seznámíme s diferenciálními rovnicemi. To není nic jiného, než správný název pro to, čemu jsme dříve říkali matematické modely formulované pomocí derivace. Viděli jsme, že tyto modely jsou v některých případech přirozeným matematickým aparátem pro popis reálně probíhajících dějů v přírodě. V přednášce se seznámíme se základním názvoslovím spojeným s touto problematikou, seznámíme se s metodami identifikace některých kvalitativních vlastností a u rovnic se separovanými proměnnými se naučíme hledat i analytické řešení. Protože se často setkáváme s modely nezávislými na čase, budeme se problematice těchto modelů věnovat podrobněji. Tyto modely mají tu vlastnost, že se ohraničená řešení po čase ustálí okolo stabilní hodnoty. Naučíme se hledat hodnoty odpovídající ustáleným řešením a z nich vybrat ty stabilní, k nimž systém může konvergovat, nebo nestabilní, které oddělují oblasti, ze kterých systém dospívá k jednotlivým stabilním stavům.


````{prf:algorithm} Motivace, přehled úspěchů
:class: dropdown

Diferenciální rovnice jsou jakýmsi zlatým grálem modelování. V historii byly matematické modely založené na těchto rovnicích přímou motivací k rozvoji diferenicálního počtu (aby bylo možno tyto rovnice formulovat) a integrálního počtu (aby bylo možno tyto rovnice řešit). Od té doby dosáhla trojice derivace+integrál+diferenciální rovnice na obrovskou řadu úspěchů napříč mnoha obory.

\iffalse

<div class='obtekat'>

```{figure} planet-neptune.jpg
Planeta Neptun. Její existence byla matematicky předpovězena na základě jinak nevysvětlitelných poruch v dráze planety Uran. Ještě týž den byl Neptun nalezen na obloze a následující den bylo potvrzeno, že se jedná o planetu. www.publicdomainpictures.net
```

```{figure} vodyanoj-kompyuterfoto7.webp
Analogové počítače využívaly toho, že různé děje mohou být popisovány stejnými diferenciálními rovnicemi. V SSSR se používaly do 80-tých let vzhledem k nedostatku polovodičů a politické definici kybernetiky jako buržoazní pavědy. https://un-sci.com/ru/2020/01/10/vodyanoj-kompyuter-gidrointegrator-lukyanova/
```

</div>

\fi

* Odvození [Keplerových zákonů](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion) pohybu planet matematickou cestou a tím potvrzení gravitačního zákona (Newton).
* Matematický aparát pro statické výpočty a výpočty [nosníků](https://cs.wikipedia.org/wiki/Bernoulliho%E2%80%93Navierova_hypot%C3%A9za) (Euler, Bernoulli, Timoshenko).
* Objev planety [Neptun](https://cs.wikipedia.org/wiki/Neptun_(planeta)) předpovězením existence této planety na základě jinak nevysvětlitelných poruch v dráze planety Uran (Verrier).
* Teorie rovnováhy populací na ostrovech (MacArthur, Wilson).
* Teorie epidemií (Kermack, McKendrick).
* [Chemické oscilátory](https://cs.wikipedia.org/wiki/Brusel%C3%A1tor) (Prigogine), Nobelova cena za nerovnovážnou termodynamiku.
* Modely konkurence živočišných druhů, [princip konkurenčního vyloučení](https://cs.wikipedia.org/wiki/Konkuren%C4%8Dn%C3%AD_vylou%C4%8Den%C3%AD) (Gause).
* Modely [predace](https://cs.wikipedia.org/wiki/Pred%C3%A1tor) živočišných druhů, oscilace v systému dravce a kořisti (Lotka, Volterra, Holling).
* Vysvětlení podstaty periodického přemnožování *[Choristoneura fumiferana](https://en.wikipedia.org/wiki/Choristoneura_fumiferana)* v kanadských lesích (Ludwig, Jones, Holling).
* Systémová biologie, výzkum složitých interakcí mezi enzymy, geny a proteiny v živých organismech (Alon).
* Výzkum meteoritů s rodokmenem ([Zdeněk Ceplecha](https://cs.wikipedia.org/wiki/Zden%C4%9Bk_Ceplecha), [Pavel Spurný](https://cs.wikipedia.org/wiki/Pavel_Spurn%C3%BD)), výpočet jejich místa dopadu a místa, odkud meteorit přiletěl. Nesmírně cenný zdroj studijního materiálu.
* Zaměřovače pro řízení protiletecké obrany ([Antonín Svoboda](https://historiepocitacu.cz/prukopnik-pocitacu-antonin-svoboda.html), český kybernetik). Svoboda  později konstruoval výkonnější zaměřovače, získal prestižní vyznamenání námořnictva USA, jeho práce pomohla rozhodnout válku v tichomoří. 

Někdy je nutné znát řešení rovnice, někdy stačí znát rovnici řídící studovaný proces a i bez znalosti řešení je možné získat užitečné informace.

* Chování řešení při změně rozměrů systému. Využívá se například v aerodynamických tunelech, kdy se rozměrné objekty testují na zmenšeninách. Dále se využívá tam, kde rovnici nedokážeme vyřešit, například model sesuvu hory do přehrady a následná tsunami v údolí Vajont nebo akustika v Janáčkově hudební síni.
* Náhrada jednoho problému jiným, který se chová stejně, ale je možné jej modelovat. Zahrnuje sestavování mechanických počítačů (zaměřovače prof. Svobody) nebo vodních počítačů ([Moniac](https://en.wikipedia.org/wiki/MONIAC) sestavený v roce 1949 pro model ekonomiky Nového Zélandu, [vodní integrátor](https://en.wikipedia.org/wiki/Water_integrator) používaný Ruskem do 80-tých let)

````

## Obyčejná diferenciální rovnice prvního řádu

https://youtu.be/GSjgp7FGvVw

Obyčejná diferenciální rovnice je rovnice, kde vystupuje neznámá
funkce a její derivace. Setkáváme se s ní například všude tam, kde
rychlost růstu nebo poklesu veličiny souvisí s její
velikostí. Například rychlost s jakou se mění teplota horkého tělesa
je funkcí teploty samotné. Rychlost tepelné výměny mezi dvěma tělesy
je totiž úměrná rozdílu jejich teplot (Newtonův zákon). Takto se
přirozeně diferenciální rovnice objevují v modelech nejrůznějších dějů
jevů. Podstatu děje, který modelujeme, musí dodat fyzika, biologie
nebo jiná aplikovaná věda. To v matematice obsaženo není. Matematika
poté poslouží k analýze, jaké jsou pozorovatelné důsledky a tím se
ověří, jestli příslušná aplikovaná věda správně vystihuje podstatu
modelovaného děje.

```{prf:definition} Diferenciální rovnice
:nonumber:
 *Obyčejnou diferenciální rovnicí prvního řádu rozřešenou vzhledem
k derivaci* (stručněji též diferenciální rovnicí, DR) s neznámou $y$
rozumíme rovnici tvaru 

$$ \frac{\mathrm{d}y}{\mathrm{d}x}=\varphi(x,y)$$ (r1)

kde $\varphi$ je funkce dvou proměnných.
```


(anglicky ordinary differential equation, ODE)

**Další formy zápisu** rovnice {eq}`r1` jsou
  $$y'=\varphi(x,y),$$
  $${\mathrm{d}y}=\varphi(x,y)\mathrm{d}x,$$
  $${\mathrm{d}y}-\varphi(x,y)\mathrm{d}x=0.$$

**Příklad.**  Najděte všechny funkce splňující $y'=2xy$. (Naučíme se řešit později.)

Diferenciální rovnice bývá v aplikacích matematickým modelem
kvantifikujícím scénář vývoje systému. Řešením jsou všechny možnosti,
jak se tento systém může vyvjíjet. K jednoznačnému předpovězení
budoucího stavu je ovšem nutno znát také stav počáteční, který ze
všech teoreticky možných průběhů vybere průběh odpovídající modelované
situaci. Tento stav vyjadřuje počáteční podmínka, uvedená v
následující definici.

```{prf:definition} Počáteční podmínka, Cauchyova úloha
:nonumber:
 Nechť $x_0$, $y_0$ jsou reálná čísla. Úloha najít
řešení rovnice {eq}`r1` 
$$  \frac{\mathrm{d}y}{\mathrm{d}x}=\varphi(x,y), $$ které splňuje zadanou *počáteční podmínku*

$$  y(x_0)=y_0 $$ (r2)

se nazývá *počáteční* (též *Cauchyova*) *úloha*. 

Řešení Cauchyovy úlohy nazýváme též *partikulárním řešením
rovnice*. Graf libovolného partikulárního řešení se nazývá *integrální
křivka*.
```


(anglicky initial condition, IC, initial value problem, IVP)

**Příklad (praktická interpretace řešení počáteční úlohy).**

* Pokud diferenciální rovnice udává rychlost ochlazování horkého nápoje a počáteční podmínka teplotu na počátku, je řešením počáteční úlohy funkce, do které dosadíme čas a přímo dostáváme teplotu nápoje v daném čase.
* Pokud diferenciální rovnice udává rychlost růstu populace živočišného druhu v čase a počáteční podmínka velikost populace na počátku sledování, je řešením počáteční úlohy funkce, do které dosadíme čas a přímo dostáváme velikost populace v daném čase.
* Pokud diferenciální rovnice udává rychlost nárůstu hladiny podzemní vody ve směru od čerpané studny a počáteční podmínka udává výšku hladiny ve studni, je řešením počáteční úlohy funkce udávající výšku hladiny podzemní vody jako funkci vzdálenosti od studny.

**Příklad.** Najděte všechny funkce splňující $y'=2xy$ a $y(0)=3$. (Naučíme se řešit později.)

```{prf:theorem} Eexistence a jednoznačnost řešení Cauchyovy úlohy
:nonumber:
 Má-li funkce $\varphi (x,y)$ ohraničenou parciální derivaci $\frac{\partial \varphi}{\partial y}$ v okolí počáteční podmínky, potom má počáteční úloha {eq}`r1`-{eq}`r2` právě jedno řešení definované v nějakém okolí počáteční podmínky.
```


**Příklad.** Rovnice 

$$y'=y$$ (rovnice3)

má řešení $y=e^x$, což nahlédneme
  snadno, protože exponenciální funkce se nemění derivováním. Dosazením je možné ukázat, že má dokonce řešení 
  
  $$y=Ce^x,$$ (rovnice4)
  
  kde $C$ je libovolné číslo.

**Příklad.** Řešení počáteční úlohy $$y'=y, \quad y(x_0)=y_0$$ najdeme tak, že využijeme řešení {eq}`rovnice4` a zařídíme, aby byla splněna počáteční podmínka. Tj. řešením počáteční úlohy je $$y=  (y_0 e^{-x_0}) e^x.$$ Vidíme, že toto řešení existuje pro každou počáteční podmínku a proto vzorec {eq}`rovnice4` popisuje dokonce **všechna** řešení rovnice {eq}`rovnice3`.

### Obecné a partikulární řešení

Řešení diferenciální rovnice je nekonečně mnoho. Zpravidla je dokážeme
zapsat pomocí jediného vzorce, který obsahuje nějakou (alespoň do
jisté míry libovolnou) konstantu $C$. Takový vzorec se nazývá **obecné
řešení rovnice**. Pokud není zadána počáteční podmínka a mluvíme o
**partikulárním řešení**, máme tím na mysli jednu libovolnou funkci
splňující diferenciální rovnici.

**Příklad:** Obecným řešením diferenciální rovnice $$y'=2xy$$ je $$y=Ce^{x^2}, \quad C\in\mathbb{R}.$$ Žádná jiná řešení neexistují,
všechna řešení se dají zapsat v tomto tvaru pro nějakou vhodnou
konstantu $C$.  Partikulárním řešením je například $y=5e^{x^2}$. Řešením počáteční úlohy $$y'=2xy, \quad y(0)=3$$ je $$y=3e^{x^2}.$$

\iffalse

**Softwarové řešiče ODE (symbolicky):**

* [Wolfram Alpha](http://www.wolframalpha.com/input/?i=solve+y%27%2Bx*y%3Dx%2Fy)
* [Matlab](https://www.mathworks.com/help/symbolic/solve-a-single-differential-equation.html)
* [Sage](https://sagecell.sagemath.org/?z=eJyrtE0rzUsuyczP01CvVNfUqNDk4lJWKMovy8tMTlWoVLet1K_QNuSCCdgqpGSmpWlU6lRoKtjaKgAlFbQVDEFajs5IPbowNe_wWq6U1OL8nLJUDageHYVKTb3ijPxyDU1kZQplQFuq8g4vLM5PAvJX5iqUlCUWlWLVnVpRkJiXogEzBgCkOj_s&lang=sage&interacts=eJyLjgUAARUAuQ==)

\fi

## Modely využívající diferenciální rovnice

https://youtu.be/UaSCLmV_g4o

### Tepelná výměna

\iffalse

<div class='obtekat'>

```{figure} hot.jpg
Tepelná výměna probíhá intenzivněji při velkém rozdílu teplot, https://pixabay.com
```

</div>

\fi

* Z fyziky víme, že *rychlost tepelné výměny mezi dvěma tělesy je úměrná rozdílu jejich
  teplot* (Newtonův zákon).
* Z přednášek o derivacích víme, že rychlost je matematicky
  derivace. Proces tepelné výměny probíhající podle Newtonova zákona
  je tedy možno modelovat diferenciální rovnicí $$ \frac{\mathrm
  dT}{\mathrm dt}=-k(T-T_0).  $$
* Rovnice udává, že teplota $T$ horkého tělesa se mění (rychlost změny
  je derivace) tak, že klesá (znaménko minus) rychlostí úměrnou
  (konstanta $k$) teplotnímu rozdílu mezi teplotou tělesa a teplotou
  okolí $T_0$ (člen $T-T_0$).
* K rovnici v ideálním případě dodáváme materiálovou charakteristiku
  (konstantu úměrnosti $k$) a počáteční teplotu. Řešením rovnice je
  funkce udávající závislost teploty na čase. Chceme-li znát teplotu
  za určitý čas, není nutné provádět pokus a čekat na uplynutí
  požadované doby. Můžeme teplotu přímo vypočítat.
* Jednotka konstanty úměrnosti $k$ je rovna převrácené hodnotě času. Tato konstanta číselně vyjadřuje rychlost ochlazování horkého tělesa v okamžiku, kde je jednotkový rozdíl teplot. Podrobnější rozbor těchto tvrzení je uveden v úvodní přednášce o derivaci, kdy jsme se s danou rovnicí setkali poprvé. 
* Někdy může být vhodné nesledovat teplotu $T$, ale rozdíl oproti
  okolní teplotě, $\tau=T-T_0$. Rovnice se potom zjednoduší na $$
  \frac{\mathrm d\tau}{\mathrm dt}=-k\tau,$$
  tedy na rovnici, kdy rychlost změny je úměrná funkční hodnotě.

### Datování pomocí uhlíku

\iffalse

<div class='obtekat'>

```{figure} archeology.jpg
Rovnice konstantního růstu nebo úbytku je základem datování pomocí uhlíku, https://www.flickr.com/photos/capturetheuncapturable, licence CC BY 2.0
```

</div>

\fi

* Při datování archeologických nálezů pozůstatků živých organismů se
  využívá fyzikálního poznatku, že radioaktivní prvky se rozpadají
  rychlostí, která je úměrná množství dosud nerozpadnutého materiálu.
* Rychlost, s jakou se mění množství (a tedy i koncentrace $y$ v daném
  vzorku) nerozpadnutého radioaktivního materiálu je tedy matematicky popsána rovnicí
  $$\frac{\mathrm dy}{\mathrm dt}=-\lambda y,$$
  kde $\lambda$ je konstanta úměrnosti. Tato rovnice je přirozeným
  důsledkem toho, že pro daný nestabilní izotop mají všechny atomy
  stejnou pravděpodobnost, že u nich dojde k rozpadu a tato
  pravděpodobnost se s časem nemění.
* Konstanta $\lambda$ má jednotku rovnu převrácené hodnotě jednotky času a udává rychlost radioaktivního rozpadu pro jednotkové množství vzorku. 
* Měříme množství radioaktivního uhlíku
  $^{14}C$ vztažené k množství stabilního $^{12}C$. Počáteční podmínka
  je známa (předpokládáme stejný poměr zastoupení jako relativně
  nedávno, před průmyslovou revolucí) a díky tomu můžeme najít funkci
  udávající, jak s časem klesá zastoupení radioaktivního uhlíku. Obsah
  radioaktivního i stabilního uhlíku je možné změřit a tím získáme
  odhad, kolik procent radioaktivního
  uhlíku se rozpadlo. Řešení počáteční úlohy poté použijeme pro odhad
  doby, kdy organismus přestal spotřebovávat uhlík z atmosféry. Tím získáme odhad, před kolika lety došlo ke smrti studovaného objektu.
* Při pokusu o datování kostí dinosaurů klesne množství
  radioaktivního uhlíku pod měřitelnou úroveň. Proto se
  v tomto případě používají látky s delším poločasem rozpadu.

### Vývoj populace a její ekologický lov

\iffalse

<div class='obtekat'>

```{figure} kralik.jpg
Při intenzivním lovu může dojít ke zničení populace https://pixabay.com
```

</div>

\fi

* Zkoumejme velikost $y$  určité populace, v prostředí s nosnou kapacitou $K$.
* Budeme pracovat s pojmem specifická míru růstu populace, což je rychlost růstu populace vztažená na jednotkové množství
  populace. Realistickým předpokladem dodaným biologickými vědami je, že v prostředí s omezenými úživnými
  vlastnostmi specifická míru růstu populace klesá s tím, jak se velikost populace přibližuje k nosné
  kapacitě, a specifická rychlost růstu populace je modelována funkcí $r\left(1-\frac yK\right)$.  Podle
  velkosti koeficientů v této rovnici dělíme živočichy na [r-stratégy
  a K-stratégy](http://cs.wikipedia.org/wiki/%C5%BDivotn%C3%AD_strategie) a
  toto dělení odráží, jak se snaží druh vyrovnávat se změnami prostředí.
* Za uvedených předpokladů je možno vývoj populace popsat rovnicí 
  $$\frac 1y \frac{\mathrm dy}{\mathrm dt}=r\left(1-\frac yK\right),$$ tj.
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right).$$ Tato rovnice se nazývá *logistická rovnice.* Podle ní je rychlost růstu úměrná současně velikosti populace a volnému procentu životního prostředí.
* Pokud lovem snížíme přírůstky populace, můžeme tento proces modelovat rovnicí 
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-h(y),$$
  kde $h(y)$ je intenzita lovu populace o velikosti $y$. Modelování
  tohoto procesu umožní nalezení ekonomicky výhodné ale přitom trvale
  udržitelné strategie lovu. Nejčatěji studované jsou případy konstantního lovu a lovu úměrného velikosti populace, tedy rovnice 
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-h$$
  a 
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-hy,$$
  kde $h$ je konstanta.

### Model ostrovní biogeografie

\iffalse

<div class='obtekat'>

```{figure} Mangrove_plants_swamp_in_Florida.jpg

Závěry modelu ostrovní biogeografie byly verifikovány pomocí experimentů na mangrovových ostrůvcích u pobřeží Floridy. Experimenty zahrnovaly vliv vzdálenosti od pevniny, vliv velikosti (některé ostrůvky byly uměle zmenšeny) a sledování kolonizace (na některých ostrůvcích byl zničen život, aby mohly být opětovně kolonizovány). Obrázek z https://commons.wikimedia.org/wiki/File:Mangrove_plants_swamp_in_Florida.jpg
```

</div>

\fi

Matematické modely je možné použít i pro studium ekosystémů. Následující model katapultoval jeho autory, Robert MacArthura a Edwarda Wilson mezi nejvýznamnější ekology. Slouží pro vysvětlení dynamické rovnováhy počtu druhů na ostrově, kdy se druhová skladba na ostrově mění, ale bohatost (počet druhů) zůstává. Původně byl odvozen pro skutečné ostrovy v moři, platí však pro jakýkoliv biotop odlišující se od okolí, například les v moři polí, vrcholky hor v moři krajiny s nižší nadmořskou výškou a podobně. Množství druhů, žijících na ostrově, označíme $N$. 

* Na ostrov migrují nové druhy, které se mohou trvale usadit. Kromě toho, některé druhy, které kolonizovaly ostrov v minulosti, pod tlakem nových kolonizátorů vymírají. Rychlost změny počtu druhů na ostrově je dána jako rozdíl rychlosti kolonizace a vymírání druhů. $$\frac{\mathrm dN}{\mathrm dt}=\text{kolonizace}-\text{vymírání}.$$
* Rozmanitější ekosystémy jsou stabilnější. Je-li na ostrově hodně druhů, je pro nové kolonizátory těžké se usadit. Proto je rychlost kolonizace klesající funkcí počtu druhů. Pro jednoduchost můžeme předpokládat, že rychlost kolonizace je nepřímo úměrná počtu druhů a tedy pro nějakou konstantu $k_1$ platí $$\text{kolonizace}=\frac{k_1}{N}.$$
* Je-li na ostrově více druhů, je pravděpodobnější, že některý vymře. Proto je rychlost mizení druhl z ostrova rostoucí funkcí počtu druhů. Pro jednoduchost můžeme předpokládat, že závislost je přímou úměrností, tj. $$\text{vymírání}=k_2 N$$ pro nějakou konstantu $k_2$.
  
Model má potom tvar $$\frac{\mathrm dN}{\mathrm dt}=\frac{k_1}{N}-k_2 N.$$ Analýza tohoto modelu dokáže objasnit, jak probíhá kolonizace a jaká je druhová pestrost v izolovaných biotopech. Umožňuje posoudit, jak se tato druhová pestrost mění s velikostí ostrova, jeho izolovaností (vzdáleností od pevniny) a má vliv například na posuzování míry ochrany chráněných lokalit v závislosti na jejich velikosti.

\iffalse


````{prf:algorithm} Rovnice samočištění jezer
:class: dropdown


<div class='obtekat'>

```{figure} voda.jpg
Jezero, ve kterém se přirozeně obměňuje znečištěná voda za čistou,  se dokáže samo zotavit ze znečištění.  Rychlost vyplavování nečistot je úměrná míře znečištění.  https://pixabay.com
```

```{figure} chirurg.jpg
Při operaci ztrácí pacient krvinky rychlostí úměrnou koncentraci krvinek. Pokud je tato koncentrace malá, pacient ztratí krvinek málo. Zdroj: https://pixabay.com
```

</div>


* Nechť veličina $y$ udává množství látky, která znečišťuje vodu v jezeře o objemu $V$.
* Předpokládejme, že do jezera přitéká čistá voda a stejnou rychlostí
  odtéká voda s nečistotami (hladina se nemění, je v ustáleném
  stavu). Nechť veličina $r$ udává, jaký objem vody se v jezeře takto
  vymění za jeden den.  Předpokládejme dále (poněkud nerealisticky),
  že rozdělení znečišťujících částic v jezeře je rovnoměrné.
* Úbytek hmotnosti nečistot za časovou jednotku je dán derivací
  $\frac{\mathrm dy}{\mathrm dt}$.
* Protože koncentrace nečistot v jezeře a v odtékající vodě je $\frac
  yV$, je úbytek znečištění možno vyjádřit též ve tvaru $\frac
  rVy$. Podíl $\frac rV$ je pro dané jezero kladná konstanta
  udávající, jak velká část z celkového množství vody se v jezeře
  vymění za časovou jednotku.  Označíme-li tuto konstantu symbolem
  $k$, je proces úbytku nečistot v jezeře popsán diferenciální
  rovnicí
  $$
  \frac{\mathrm dy}{\mathrm dt}  =-ky.
  $$
* Výše uvedená rovnice na nazývá *rovnice samočištění jezer*, ale
  tento název je čistě formální. Jedná se vlastně o stejnou rovnici,
  která popisuje radioaktivní rozpad nebo
  změnu rozdílu mezi teplotou horkého nápoje a místnosti při chladnutí
  nápoje.
* Stejnou rovnicí je možné popsat nejenom odbourávání nečistot z
  životního prostředí, ale i odbourávání léků nebo drog z
  těla. Považujme krevní oběh za jezero a lék nebo drogu za
  znečišťující látku. V případě, že rychlost odbourávání je úměrná
  koncentraci (platí pro farmakokinetiku prvního řádu, toto splňuje
  většina léčiv za běžných koncentrací), řídí se proces odbourávání
  stejnou diferenciální rovnicí.


### Akutní normovolemická hemodiluce


* Při chirurgické operaci dochází ke krvácení. Pacient ztrácí krev s
  ní i krvinky. Při konstantní intenzitě krvácení to znamená, že
  pacient ztrácí krvinky rychlostí úměrnou počtu krvinek. Formálně na
  krvinky v krvi můžeme pohlížet stejně jako na znečištění
  jezera. Jedná se o stejný proces vyplavování látek obsažených v
  tekutině, jenom měníme interpretaci veličin.
* Pokud očekáváme takový průběh operace, že i po uvedeném poklesu bude
  pořád množství krvinek nad minimální přípustnou hodnotou, je možné
  před operací toto množství snížit tím, že se část krve odebere a
  krev se poté doplní vhodnými roztoky.
* Protože pacient bude po výše uvedeném zákroku už od začátku operace
  menší počet krvinek, ztrácí tyto krvinky pomaleji a celkový úbytek
  během operace je menší. Na konci operace se pacientovi vrátí dříve
  odebraná krev. Výsledkem je, že po operaci v jeho těle koluje více
  krvinek, než pokud by byl operován s "původní krví".
* Aby metoda fungovala, je nutné odhadnout ztrátu krve během
  operace. Modelování pomocí diferenciálních rovnic dokáže
  předpovědět, kolik krve odebrat na začátku tak, aby i po plánované
  době operace zůstaly krevní hodnoty pacienta v bezpečných
  mezích. Pokud na začátku operace část krve dáme bokem a poté tekutiny
  doplňujeme fyziologickým roztokem (s tím, že vlastní krev vrátíme po
  skončení operace), jedná se o stejný proces a stejnou rovnici jako
  samočištění jezer. Pokud krev doplňujeme během operace z krve
  dopředu odebrané,
  dokážeme model samočištění jezer modifikovat pro daný proces.
* Metoda *akutní normovolemické hemodiluce* nachází v současné praxi
  široké využití v řadě operačních oborů. Poskytuje totiž možnost
  vyhnout se podání alogenní krevní transfuze a tím eliminovat rizika
  z ní vyplývající. Současně je tato metoda výrazně finančně levnější
  a její přínos je tak i ekonomický. (Podle https://zdravi.euro.cz/)


````

````{prf:algorithm} RC obvod
:class: dropdown

<div class='obtekat'>

```{figure} RC_circuit.png
RC obvod. Pro vysoké frekvence platí $V_c\approx \frac{1}{RC}\int_0^t V_{in}\,\mathrm dt.$  Zdroj: Wikipedia
```

```{figure} RC_circuit_drevostavba.jpg
Senzor pro sledování vlhkosti dřeva vyvinutý na ÚNOD LDF MENDELU a zabudovaný do dřevostavby.   Zdroj: R. Slávik et. al., A Nondestructive Indirect Approach to Long-Term Wood Moisture Monitoring Based on Electrical Methods (2019)
```

</div>

Při nabíjení kondenzátoru o kapacitě $C$ přes odpor o velikosti $R$ roste napětí na kondenzátoru, tím se mění nabíjecí proud a proto se mění i rychlost nabíení. Pomocí zákonů elektrotechniky je [možno ukázat](http://fyzikalniolympiada.cz/texty/matematika/difro.pdf), že nabíjecí proud $i$ kondenzátoru se řídí diferenciální rovnicí
$$R\frac{\mathrm di}{\mathrm dt}+\frac 1Ci=0.$$
Napětí na kondenzátoru je možno odvodit buď z proudu, napětí na rezistoru a napětí zdroje, nebo z celkového proudu, který prošel kondenzátorem.

Rovnice je tedy stejná jako rovnice radioaktivního rozpadu a rovnice samočištění jezer. Vhodnou manipulací s parametry součástek je možno měnit koeficient u této rovnice a vhodným spojováním těchto obvodů dokážeme podobně simulovat i složitější rovnice. To je bylo základem analogových počítačů, které nepracovaly s čísly, ale s napětími. Tyto počítače sehrály svou roli v době, kdy číslicové počítače byly nedostupné, pomalé a nespolehlivé. Tím byla historická úloha analogových počítačů splněna a již se nepoužívají. 

RC obvod jako takový má však důležité místo i dnes. Dokáže například filtrovat signály podle frekvence. Výpočet jeho charakteristiky (tj. vyřešení rovnice) a sledování napětí na kondenzátoru umožní měření elektrického odporu tam, kde není vhodné odpor určovat z proudu a napětí pomocí Ohmova zákona. Typickým příkladem je odpor dřeva a jeho vodivost, tj. převrácená hodnota odporu. Tato veličina se používá k rychlému stanovení vlhkosti dřeva, nebo je možno ji dlouhodobě sledovat pomocí senzorů zabudovaných do dřevostavby. 

Ve skutečnosti žádná elektronická součástka nemá ideální vlastnosti a proto se v obvodu projevují i nežádoucí parazitní charakteristiky. Pokud by toto bylo limitující, je možné obvod nahradit podobně se chovajícím zapojením s [operačním zesilovačem](https://cs.wikipedia.org/wiki/Zapojen%C3%AD_s_opera%C4%8Dn%C3%ADm_zesilova%C4%8Dem#Integra%C4%8Dn%C3%AD_zesilova%C4%8D) (odkazovaná stránka pracuje s rovnicí v integrálním tvaru).

````

````{prf:algorithm} Lovci meteoritů z ČSSR a ČR
:class: dropdown

<div class='obtekat'>

```{figure} benesov.jpeg
Tři dosud nalezené meteority Benešov. foto: Pavel Spurný, převzato z https://dvojka.rozhlas.cz/
```

</div>

Česká republika je na světové špičce v oblasti propočítávání dráhy meteoritů ze světelné stopy zachycené sítí bolidových kamer. Vědcům z Astronomického ústavu se podařilo 

* jako prvním na světě najít pozůstatky meteoritu propočítáním jeho dráhy ze snímků zachycených speciálními kamerami a zpětně propočítat, odkud meteorit přiletěl (meteorit Příbram, 1959, první "meteorit s rodokmenem", tj. s doloženým původem),
* jako prvním na světě najít pozůstatky meteoritu 20 let po dopadu použitím analýz, které v době dopadu meteoritu nebyly k dispozici (meteorit Benešov, dopad 1991, nalezen 2011),
* propočítat a najít (mimo jiné i na dně jezera!) zbytky meteoritu Čeljabinsk z roku 2013.

Meteority s vystopovaným původem jsou extrémně vzácné (do roku 2000 jenom 5 meteoritů, do roku 2016 pouze 31 meteoritů) a tým založený Zdeňkem Ceplechou a nyní vedený Pavlem Spurným se podílel na výpočtu drah většiny z nich.
Použité metody jsou popsány například v článku *Ceplecha, Revelle: Fragmentation model of meteoroid motion, mass loss, and radiation in the atmosphere, Meteoritics & Planetary Science 40, Nr 1, 35–54 (2005).* Například ztráta rychlosti třením v atmosféře je modelována rovnicí $$\frac{\mathrm dv}{\mathrm dt}=-K\rho m^{-1/3}v^{2}$$ a ztráta hmotnosti vypařováním 
$$\frac{\mathrm dm}{\mathrm dt}=-K\sigma \rho m^{2/3}v^3.$$
Jedná se o diferenciální rovnice, kde zrychlení (derivace rychlosti) a časová změna hmotnosti (derivace hmotnosti podle času, rychlost, s jakou ubývá hmotnost)  je úměrná vhodným mocninám těchto veličin.

````

\fi

\iffalse

`ww2:problems/diferencialni_rovnice/chata.pg`

\fi

## Geometrická interpretace a transformace jednotek

https://youtu.be/OgzYhnGj34I

### Geometrická interpretace ODE

manimp:Slope_field|Směrové pole diferenciální rovnice dává představu o chování řešení této rovnice.

Protože derivace funkce v bodě udává směrnici tečny ke grafu funkce
v tomto bodě, lze rovnici {eq}`r1` $$\frac{\mathrm dy}{\mathrm dx}=\varphi(x,y)$$ chápat jako předpis, který
každému bodu v rovině přiřadí směrnici tečny k integrální křivce,
která tímto bodem prochází.  Sestrojíme-li v dostatečném počtu
(například i náhodně zvolených) bodů $[x,y]$ v rovině vektory
$(1,\varphi(x,y))$, obdržíme **směrové pole diferenciální rovnice** —
systém lineárních elementů, které jsou tečné k integrálním křivkám.

Počáteční podmínka $y(x_0)=y_0$ geometricky vyjadřuje skutečnost, že graf
příslušného řešení prochází v rovině bodem $[x_0,y_0]$. Má-li tato
počáteční úloha jediné řešení, neprochází bodem $[x_0,y_0]$ žádná další
křivka. Má-li každá počáteční úloha jediné řešení (což bude pro nás
velice častý případ), znamená to, že integrální křivky se *nikde
neprotínají*.

<!--
## Numerické řešení IVP

<div class='obtekat'>

```{figure} euler.png
Eulerova metoda s velmi dlouhým krokem (modrou barvou) zaostává za přesným řešením (šedou  barvou). Pro lepší výsledek můžeme zmenšit krok nebo vylepšit metodu.
```

```{figure} rk.png
Metoda Runge Kutta s velmi dlouhým krokem (modrou barvou, jde jasně  vidět aproximace lomenou čarou). Přesné řešení je nakresleno šedou  barvou.
```

</div>

Řešení počáteční úlohy lze numericky aproximovat poměrně snadno:
začneme v bodě zadaném počáteční podmínkou a v okolí tohoto bodu
nahradíme integrální křivku její tečnou. Tím se dostaneme do dalšího
bodu, odkud opět integrální křivku aproximujeme tečnou.  Směrnici
tečny zjistíme z diferenciální rovnice, buď přímo z derivace (Eulerova
metoda).

Vyjdeme-li z počáteční úlohy $$\frac{\mathrm dy}{\mathrm dx}=\varphi(x,y), \quad y(x_0)=y_0,$$
má lineární aproximace řešení v bodě $[x_0,y_0]$ tvar $$y=y_0+\varphi(x_0,y_0)(x-x_0).$$
Funkční hodnotu v bodě $x=x_1$ označíme $y_1$ a tento bod bude dalším  body lomené čáry, tj. $$y_1=y_0+\varphi(x_0,y_0)(x_1-x_0).$$
Hodnota $x_1-x_0$ je krok Eulerovy metody označovaný $h$. Tento postup opkaujeme s počáteční podmínkou $y(x_1)=y_1$.
Iterační formule Eulerovy metody má potom následující tvar. $$\begin{aligned}x_{n+1}&=x_n+h, \ y_{n+1}&=y_n+\varphi(x_n,y_n)h.\end{aligned}$$

Stačí tedy mít zvolen *krok* numerické
metody (délku intervalu, na kterém aproximaci tečnou použijeme) a
výstupem metody bude aproximace integrální křivky pomocí lomené čáry.

**Vylepšení**

* Pro přesnější aproximaci je možné zjemnit krok $h$ (buď všude, nebo
  jenom tam, kde "je to potřeba").
* Pro přesnější aproximaci je možné použít místo $\varphi(x_n,y_n)$
  lepší směrnici, která dokáže zohlednit, jestli se růst zrychluje
  nebo zpomaluje (metoda Runge Kutta druhého nebo čtvrtého řádu, ...).
* Modely obsahující diferenciální rovnice obsahují zpravidla sadu
  parametrů charakterizujících fyzikální vlastnosti studovaných
  objektů. Pro numerické řešení musíme těmto parametrům dát konkrétní
  hodnoty a přicházíme tak o cennou informaci, jak řešení závisí na
  těchto parametrech. Vhodnou úpravou rovnice dokážeme počet parametrů
  eliminovat. Jednoduchým a často dostatečným způsobem je volba
  jednotek, obecnější metodou je transformace diferenciální rovnice
  uvedená v následujícím textu.

**Online řešiče ODE (numericky):**

* [dfield](http://math.rice.edu/~dfield/dfpp.html)
* [Sage](https://sagecell.sagemath.org/?z=eJyFj0EOgyAURPecgp3Q_hqh3f47sG-MMYopKRUjaOH29fcA7WYyk8y8ZCaRoUgsJ5EvRTJWXm4GXl595sgb4JoxN0SF9waaWrUUNIXDMqNxtDH43Xbr8yamLwoKHB2kEbi9XzGDncduCW5OkZbXFsKWli1hFX1YbDc568dKMqN-4vRf3OJDqoAPwYcVq9USlAmjzkbLOj7CW9AvJAH6iSTyA5etU1M=&lang=sage&interacts=eJyLjgUAARUAuQ==)

-->

### Transformace diferenciální rovnice

\iffalse

<div class='obtekat'>

```{figure} Vajont.jpg
Letecký snímek údolí Vajont krátce po katastrofě. [Video](https://youtu.be/BK5uwnVCeCw?t=2185) ukazuje, že při modelování procesu ve zmenšeném měřítku je nutné transformovat ostatní veličiny, například čas. Pro nás klíčová slova v čase 37:06 dokumentu jsou "tým techniků odhaduje nejvyšší možnou reálnou rychlost sesuvu půdy na jednu minutu, kterou pro simulaci přepočítají na čtyři sekundy". Čas ve zmenšeném modelu ubíhá jinou rychlostí než čas v reálném ději. Foto: Wikipedia.
```

```{figure} vajont_model.png
Model přehrady v údolí Vajont. Byl zdařilý, ale jeho použití s nesprávnými vstupními daty (podcenění odhadu rychlosti sesuvu hory) vedlo k tomu, že závěry nebyly relevantní. Vpravo tři postavy sledující pokus pomůžou s odhadem rozměrů. Zdroj: záběr z dokumentu Tsunami v horách a z filmu Vajont - šílenství mužů.
```

```{figure} janackova_sin.jpg
Model [Janáčkovy koncertní síně](https://www.irozhlas.cz/kultura/desetkrat-mensi-akusticky-dokonaly-model-janackovo-centrum_2107300010_btk) pro Brno. Desetkrát menší a proto s desetkrát většími frekvencemi. Zdroj: Tomáš Kemr, Český rozhlas.
```

</div>

\fi

Naučíme se vyjadřovat diferenciální rovnici v jiných proměnných tak,
aby bylo možné snížit počet parametrů v této rovnici. Pro jednoduchost
budeme uvažovat jenom případ, kdy nová proměnný je lineární funkcí
původní proměnné.

Uvažujme funkci $y$ proměnné $x$. Připomeneme si vzorce pro derivaci
součtu, derivaci konstantního násobku a derivaci složené funkce, ale
uvedeme si je v kontextu vhodném pro studium diferenciálních rovnic.

* Z derivace součtu a z derivace konstanty plyne pro funkci $y$ a konstantu $y_0$ vztah
 $$ \frac{\mathrm d (y\pm y_0)}{\mathrm dx} = \frac{\mathrm d y}{\mathrm dx} \pm \frac{\mathrm d y_0}{\mathrm dx} = \frac{\mathrm d y}{\mathrm dx} \pm 0= \frac{\mathrm d y}{\mathrm dx}.$$
* Z derivace konstantního násobku funkce plyne pro funkci $y$ a konstantu $k$ vztah
 $$ \frac{\mathrm d (ky)}{\mathrm dx} = k\frac{\mathrm d y}{\mathrm dx}.$$
* Z derivace složené funkce plyne pro konstantu $k$ a veličinu $X = kx$ vztah
  $$ \frac{\mathrm d y}{\mathrm d x} =    \frac{\mathrm d y}{\mathrm dX}   \frac{\mathrm d X}{\mathrm dx} =   \frac{\mathrm d y}{\mathrm d X} k   $$
  tj.
  $$ \frac{\mathrm d y}{\mathrm d (kx)} = \frac{\mathrm d y}{\mathrm d X} =      \frac 1k \frac{\mathrm d y}{\mathrm d x}.$$

Výše uvedené výpočty je možno shrnout do pravidla v následující poznámce.

```{prf:remark} Transformace diferenciální rovnice do jiných jednotek
:nonumber:
 Pro $Y=k_1(y-y_0)$ a $X=k_2 x$ platí   $$  \frac{\mathrm d Y}{\mathrm d X} =   \frac{\mathrm d \Bigl(k_1(y-y_0)\Bigr)}{\mathrm d (k_2 x)} = \frac{k_1}{k_2} \frac{\mathrm dy}{\mathrm dx}$$ a podobně (všimněte si druhé mocniny u $k_2$ díky druhé derivaci) $$  \frac{\mathrm d^2 Y}{\mathrm d X^2} = \frac{k_1}{k_2^2} \frac{\mathrm d^2y}{\mathrm dx^2}.$$   Výraz nalevo neobsahuje konstanty, které jsou ve výrazu   napravo. Tyto konstanty jsou v definici nových veličin $X$ a $Y$. 
```


Navíc vzorec z poznámky silně připomíná klasické počítání se   zlomky. Proto máme Leibnizův tvar zápisu derivací $\frac{\mathrm   dy}{\mathrm dx}$ při studiu diferenciálních rovnic více v oblibě, než zápis Lagrangeův, $y'$.

**Příklad.** Diferenciální rovnice tepelné výměny 

$$\frac{\mathrm dT}{\mathrm dt}=-k(T-T_\infty), \quad T(0)=T_0$$ (NZ-I)

obsahuje tři parametry: teplotu okolního prostředí $T_\infty$, počáteční teplotu $T_0$ a konstantu $k$ související s fyzikálními vlastnostmi prostředí. Postupně můžeme posunout  teplotní stupnici tak, aby teplota okolí byla nula a počáteční teplota jedna, tj. hodnotu $T$ snížíme o $T_\infty$ a upravíme dílek stupnice $(T_0-T_\infty)$-krát
$$\frac{\mathrm d\left(\frac{T-T_\infty}{T_0-T_\infty}\right)}{\mathrm dt}=-k\frac{T-T_\infty}{T_0-T_\infty}$$
vydělit konstantou $k$
$$\frac{\mathrm d\left(\frac{T-T_\infty}{T_0-T_\infty}\right)}{k\mathrm dt}=-\frac{T-T_\infty}{T_0-T_\infty}$$
a přeškálovat pomocí konstanty $k$ čas
$$\frac{\mathrm d\left(\frac{T-T_\infty}{T_0-T_\infty}\right)}{\mathrm d(kt)}=-\frac{T-T_\infty}{T_0-T_\infty}.$$
Po substituci $y=\frac{T-T_\infty}{T_0-T_\infty}$, $x=kt$ má úloha tvar

$$\frac{\mathrm d y}{\mathrm d x}=-y,\quad y(0)=1.$$ (NZ-II)

Nová rovnice {eq}`NZ-II` *neobsahuje žádné parametry* a proto je pro studium
jednodušší. Přesto je v ní obsažena veškerá informace obsažená v
rovnici {eq}`NZ-II`. Tuto informaci je však nutno interpretovat v kontextu
definice nových proměnných. Například to, že všechna řešení rovnice {eq}`NZ-II` konvergují k nule
znamená, že všechna řešení rovnice {eq}`NZ-I` konvergují k $T_0$. To, že řešení rovnice {eq}`NZ-II` klesne na poloviční hodnotu za čas $\ln 2$ znamená, že vzdálenost řešení rovnice {eq}`NZ-I` od rovnovážného stavu se na polovinu zmenší za čas $\frac 1k \ln 2$.

\iffalse

manimp:ODE_transformace|Vhodnou transformací je možno zredukovat počet parametrů v rovnici a tím usnadnit numerické simulace. Nematematická cesta k transformaci je vhodná volba jednotek pro sledované veličiny.

\fi

```{prf:remark} Nondimenzionalizace, rozměrová analýza
:nonumber:
Proces eliminace parametrů z modelu popsaného diferenciální rovnicí se nazývá nondimenzionalizace nebo rozměrová analýza modelu, protože eliminaci parametrů je vhodné provádět tak, aby výsledné nové veličiny vycházely bez fyzikálních jednotek. K tomu se provádí rozbor jednotek jednotlivých veličin. V jednoduchých případech však stačí primitivní postup popsaný v odstavcích výše a ukázaný na příkladu. V tomto příkladě veličina $x$ nemá fyzikální jednotku, protože je součinem konstanty $k$ (s jednotkou $\mathrm s^{-1}$) a času $t$ (s jednotkou $\mathrm s$). Je možné ji považovat za *bezrozměrný čas*. Veličina $y$ také nemá fyzikální jednotku, protože je podílem dvou teplot a je možné ji považovat za *bezrozměrnou teplotu*. 

V úloze s ochlazováním tělesa bylo zavedení nových veličin přirozené. I u méně zřejmých úloh zkušenosti ukazují, že je vhodné volit transformaci tak, aby vznikly veličiny bezrozměrné, které nemají fyzikální jednotku. Například v
*Horáček, Fyzikální a mechanické vlastnosti dřeva I* je zavedena [bezrozměrná vlhkost, bezrozměrný čas a bezrozměrná vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9180;lang=cz) na straně 61 pro rovnici popisující difuzi a [charakteristická délka, Biotovo číslo (bezrozměrná tepelná vodivost) a bezrozměrná teplota, bezrozměrný čas a bezrozměrná vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9182;lang=cz) pro rovnici popisující vedení tepla na stranách 88 a 89.

Obecné výhody transformace diferenciálních rovnic jsou následující.

* Po transformaci obsahuje rovnice v nových veličinách menší množství parametrů.
* Nové veličiny jsou bez fyzikální jednotky a tudíž vhodné pro numerické simulace, kdy se zpravidla o jednotky nestaráme.
* Nové veličiny zpravidla nabývají hodnot řádově srovnatelných s jedničkou. Nejedná se ani o tisíce ani o tisíciny. 

Všechny tři uvedené skutečnosti vedou k tomu, že s transformovanými rovnicemi se lépe pracuje v numerických modelech.
```


**Příklad.** Diferenciální rovnici logistického růstu s lovem konstantní intenzity $$\frac{\mathrm dx}{\mathrm dt}=rx\left(1-\frac xK\right)-h$$ je možno přepsat do tvaru 
$$\frac{\mathrm d\frac xK}{\mathrm d(rt)}=\frac xK\left(1-\frac xK\right)-\frac{h}{rK}$$
a po zavedení bezrozměrné velikosti populace $X=\frac xK$, bezrozměrného času $T=rt$ a bezrozměrné intenzity lovu $H=\frac{h}{rK}$ má model tvar
$$\frac{\mathrm dX}{\mathrm dT}=X\left(1-X\right)-H.$$ Jinými slovy, chování modelu například z hlediska konvergence řešení k nenulové hodnotě závisí na parametru $\frac{h}{rK}.$ Pokud se sníží nosná kapacita prostředí o dvacet procent, je nutné pro udržení stejného chování rovnice snížit lov nebo zvýšit koeficient $r$ tak, aby poměr $\frac{h}{rK}$ zůstal zachován. 

<!--

\iffalse 

## Malá odbočka - zaokrouhlovací chyby v numerických výpočtech

<div class='obtekat'>

```{figure} patriot.jpg
Součást protiraketového systému Patriot. Raketu Scud vystřelenou 25.2.1991 systém nesestřelil vinou zaokrouhlovací chyby. Zdroj: U.S. Army.
```

</div>

Uvedli jsme, že počáteční úlohu umíme vyřešit numericky. Ukázali jsme
si základní algoritmus (Eulerův) a řekli, že existují algoritmy
pokročilejší. Na tomto místě upozorníme na záludnosti skryté v
numerických výpočtech. Je iluzorní se domnívat, že zjemněním kroku při
numerickém řešení diferenciální rovnice vždy dostaneme přesnější
řešení. Toto platí jenom dokud se nedostaneme ke kritické hodnotě
kroku, kdy další snižování vede k tomu, že zpřesnění díky kratšímu
kroku se přebije akumulovanou chybou z velkého množství výpočtů nutně
zatížených zaokrouhlováním a dalším zjemňováním přesnost ztrácíme.

Zajímavá léčka je v samé podstatě výpočtů na počítači a to v
reprezentaci desetinných čísel ve dvojkové soustavě. Například číslo
0.1 je ve dvojkové soustavě periodické! Proto desetinásobným sečtením
tohoto čísla ve dvojkové soustavě nedostaneme (překvapivě) jedničku! Je to podobné, jako
bychom v námi běžně používané dvojkové soustavě třikrát sečetli jednu třetinu v desetinném tvaru
reprezentovaném konečným počtem desetinných míst, tj. například
třikrát sečetli číslo $0.33333333$. Nedostaneme přesně jedničku. 

Tento efekt měl i tragický důsledek. Software protiraketového
systému Patriot počítal čas postupným přičítáním desetiny
sekundy. Protože systém byl vytvořen a testován na mobilním zařízení,
které se často restartovalo a běželo krátkou dobu, ničemu to
nevadilo. Nasazení v systému Patriot však byla chyba. Při ostrém
nasazení systém běžel dlouho, zaokrouhlovací chyba se kumulovala
například 100 hodin. I když za tu dobu chyba dosáhla pouze zlomku
sekundy, raketa letící vysokou rychlostí již byla jinde, než systém
Patriot propočítal.  Dne 25.2.1991 systém Patriot během operace
Pouštní bouře na osvobození Kuvajtu od irácké okupace nesestřelil
útočící raketu Scud a ta zabila 28 vojáků osvobozující armády a okolo
100 osob zranila.

S chybami plynoucími ze zaokrouhlování se setkáme i při výpočtech mimo modelování diferenciálních rovnic. Viz například [Floating-point arithmetic may give
inaccurate results in
Excel](https://support.microsoft.com/en-us/help/78113/floating-point-arithmetic-may-give-inaccurate-results-in-excel).

\fi

-->

## ODE tvaru $\frac{\mathrm dy}{\mathrm dx}=f(y)$, autonomní ODE

https://youtu.be/SVDLZMIfW8Y

manim:Stabilita|Siu5ZgEA59s|Stabilitu autonomní diferenciální rovnice můžeme posoudit ze znaménka pravé strany. S minimem informací dokážeme poznat, jak se bude řešení chovat z hlediska konvergence ke stacionárnímu stavu.

Rovnice 

$$\frac{\mathrm dy}{\mathrm dx}=f(y)$$ (autonomni)

se nazývá *autonomní*, nebo též nezávislá na čase. Je speciálním
případem rovnice se separovanými proměnnými, která je uvedena na
dalším slidu a naučíme se ji řešit analytickou cestou. Proto se nyní
nebudeme zaměřovat na hledání obecného řešení, ale pokusíme se popsat
chování řešení, aniž bychom tato řešení znali. Pokusíme se s co
nejmenší námahou říct, jak se budou řešení chovat.

* Je-li $f(y_0)=0$, je konstantní funkce $y(x)=y_0$ řešením rovnice
  {eq}`autonomni`. Protože derivace konstantní funkce je nula, vidíme, že řešením
  rovnice $$f(y)=0$$ obdržíme všechna konstantní řešení rovnice {eq}`autonomni`. Tato konstantní řešení se nazývají *stacionární body*.
* Stacionární body a jim odpovídající konstantní řešení představují
  rovnovážný stav. Často nás zajímá, jestli při vychýlení z tohoto
  rovnovážného stavu má systém tendenci se vrátit do původního stavu,
  nebo se od původního stavu dále odchylovat.  
* Pokud se při malém
  vychýlení z rovnovážného stavu systém do tohoto stavu vrací, mluvíme
  o *stabilním stacionárním bodu*.
* Pokud se systém po malé výchylce do
  tohoto rovnovážného stavu nevrací, ale vyvíjí se k dalšímu
  stacionárnímu bodu nebo neohraničeně, mluvíme o *nestabilním
  stacionárním bodu.*

Následující věta umožní odlišit stabilní a nestabilní stacionární
body. Protože v přírodě dochází k drobným perturbacím neustále, udává
vlastně, které stacionární stavy jsou realizovatelné a můžeme je v
přírodě pozorovat a které jsou prakticky nerealizovatelné.

<!--
* Rovnici $$\frac{\mathrm dy}{\mathrm d x}=ky,$$ kde $k$ je konstanta,
  je možno přetransformovat na rovnici $\frac{\mathrm dy}{\mathrm
  d(kx)}=y$, kterou jsme studovali na jednom z úvodních slidů.  Proto
  není težké se přesvědčit, že obecným řešením této
  rovnice je funkce $$y=Ce^{kx}. \tag{♣♣}$$
  Jediné konstantní řešení této rovnice je $y=0$.  
    * Pro $k>0$ jsou funkce (♣♣)
    jsou neohraničené (kladné rostoucí nebo záporné klesající, podle
    znaménka konstanty $C$) na intervalu $[0,\infty)$. Jakákoliv
    odchylka od rovnovážného stavu neohraničeně naroste, konstantní
    řešení $y=0$ se proto klasifikuje jako nestabilní.
    * Pro $k<0$ se funkce (♣♣) na intervalu $[0,\infty)$
    blíží k nule. Ať je počáteční podmínka libovolná, všechna řešení se
    v čase blíží k nule. Jakákoliv
    odchylka od rovnovážného stavu neohraničeně časem vymizí. Nulové
    řešení je stabilní.

Vyzbrojeni předchozími speciálními případy budeme sledovat řešení
rovnice $$\frac{\mathrm dy}{\mathrm dx}=f(y)$$ v okolí bodu $y_0$
splňujícího $f(y_0)=0.$
To můžeme chápat tak, že modelovaný systém je ve stacionárním stavu s
konstantním řešením $y(x)=y_0$ a nějakými vnějšími vlivy došlo k
drobnému vychýlení z tohoto stavu.
Lineární aproximace (viz úvodní přednášky derivacích)
$$f(y)\approx f'(y_0)(y-y_0)$$ nám umožní rovnici aproximovat rovnicí
$$\frac{\mathrm dy}{\mathrm dx}=f'(y_0)(y-y_0)$$
neboli
$$\frac{\mathrm d(y-y_0)}{\mathrm dx}=f'(y_0)(y-y_0)$$
a po substituci $Y=y-y_0$, $k=f'(y_0)$ dostáváme rovnici
$$\frac{\mathrm dY}{\mathrm dx}=kY,$$
což je rovnice typu (♣). Stabilitu takové rovnice máme prozkoumánu a
proto můžeme udělat následující závěr.

-->

```{prf:theorem} Stabilita konstantních řešení
:nonumber:
 Jestliže platí $f(y_0)=0$, je
  konstantní funkce $y(x)=y_0$ konstantním řešením rovnice
  $$\frac{\mathrm dy}{\mathrm dx}=f(y).$$ Toto řešení je stabilní
  pokud $\frac{\mathrm df}{\mathrm dy}(y_0)<0$ a nestabilní pokud $\frac{\mathrm df}{\mathrm dy}(y_0)>0$.
```


Pro grafickou intepretaci je vhodné připomenout, že funkce s kladnou
derivací jsou rostoucí a funkce se zápornou derivací klesající. Pokud
má tedy pravá strana derivaci různou od nuly, poznáme stabilitu z monotonie pravé strany.

manim:Logistic|NyLkjOTYzVQ|U logistické rovnice s lovem dochází v závislosti na velikosti lovu buď ke snížení nebo k zániku stabilního stacionárního stavu.

**Příklad.** Logistická diferenciální rovnice s konstantním lovem
  $h$, tj. rovnice
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-h,$$
  má pro malé $h$ dva stacionární body. Funkce $ry\left(1-\frac
  yK\right)$ je parabola otočená vrcholem
  nahoru a s nulovými body $y=0$ a $y=K$. V prvním stacionárním bodě
  je funkce rostoucí a tento stacionární bod je nestabilní. Ve druhém
  stacionárním bodě je funkce klesající a tento stacionární bod je
  stabilní. Jak se zvyšuje faktor $h$, graf paraboly se posouvá směrem
  dolů a oba stacionární body se posouvají směrem k sobě a k  vrcholu. Jejich stabilita zůstává neporušena. To znamená, že sice
  pořád existuje stabilní stav, ale se zvyšující se intenzitou lovu se
  tento stacionární stav dostává stále blíže ke stavu nestacionárnímu a
  rovnováha je tedy poněkud křehká. 

```{prf:remark} Autonomní rovnice s rozdílem na pravé straně
:nonumber:
 Rovnice $$\frac{\mathrm dy}{\mathrm dx}=g(y)-h(y)$$ má stacionární bod $y_0$, jestliže $$g(y_0)=h(y_0).$$ Často jsou funkce $g$ a $h$ zadány graficky a stacionární bod je v průsečíku grafů funkcí $g$ a $h$. Ze vzájemné polohy těchto grafů také vidíme, zda je stacionární bod stabilní (funkce $g$ je napravo od bodu $y_0$ pod funkcí $h$ a nalevo nad ní) nebo nestabilní (naopak).
```


<div class='obtekat'>

```{figure} img_earth_balance_2.png
Funkce z pravé strany rovnice pro teplotní bilanci Země
```

</div>

**Příklad.** Teplotní bilanci Země je možno vyjádřit [rovnicí](http://user.mendelu.cz/marik/wiki/doku.php?id=ode)
$$\frac{\mathrm dT}{\mathrm dt}=R_{\text{in}}(T)-R_{\text{out}}(T),$$ kde $R_{\text{in}}$ a $R_{\text{out}}$ jsou funkce dané na obrázku. Vidíme tři průsečíky, tj. tři stacionární body. Uvažujme stacionární bod nejvíce napravo. Malá výchylka nahoru k větší teplotě nás posune do oblasti, kde převažuje vyzařování energie, $R_{\text{out}}$ je vetší než $R_{\text{in}}$, pravá strana je záporná a teplota klesá zpět do stacionárního stavu. Podobně, malá výchylka směrem dolů způsobí nárůst a opět návrat do stacionárního stavu. Stacionární stav zcela vpravo je tedy stabilní. Podobně ukážeme, že stacionární stav odpovídající průsečíku zcela vlevo je také stabilní. Naopak, stacionární stav uprostřed je nestabilní, libovolná výchylka z tohoto stavu způsobí přechod systému do některého ze stabilních stavů.

\iffalse

`ww2:problems/diferencialni_rovnice/stabilita_autonomni.pg`

`ww2:problems/diferencialni_rovnice/model.pg`

`ww2:problems/diferencialni_rovnice/05.pg`

`ww2:problems/diferencialni_rovnice/06.pg`

\fi

<!--

##  Příklad - časový rozestup mezi trolejbusy

\iffalse

<div class='obtekat'>

```{figure} trolejbus.jpg
Trolejbus jezdící okolo LDF. Dříve se běžně dlouho čekalo a poté jelo několik trolejbusů za sebou. s IDS JMK a koordinací dopravy k tomuto nedochází, ale občas trolejbus čeká na odjezd podle jízního řádu. Autor: Dezidor, CC BY 3.0.
```

</div>

\fi

Uvažujme dva trolejbusy jedoucí za sebou po stejné trati. Označme
$x(t)$ jejich časový odstup. Pokud první trolejbus zastaví na určité
zastávce v čase $t$, druhý trolejbus na tuto zastávku dorazí v čase
$x(t)$. Naším úkolem je zjistit, jak se $x(t)$ mění s rostoucím $t$.

Předpokládejme, že

* první vůz jede konstantní rychlostí (není dopravní špička)
* pokud žádní pasažéři nečekají na druhý vůz, druhý vůz se
  pohybuje rychleji než první vůz a oba vozy se "sjedou", tj. $x(t)$
  klesá, pokud na druhý vůz nečekají žádní pasažéři
* rychlost druhého vozu klesá s rostoucím počtem pasažérů, kteří
  čekají na zastávce 
* počet pasažérů kteří čekají na zastávce roste s rostoucím
  intervalem mezi oběma vozy.

Uvažujme, že všechny závislosti popsané výše jsou lineární (přímá
úměrnost).

Situaci je možno modelovat diferenciální rovnicí
$$ 
  \frac{\mathrm dx}{\mathrm  dt}=\beta x-\alpha,
$$
kde $\alpha$ a $\beta$ jsou kladné reálné konstanty. Tato rovnice má konstantní řešení $x=\frac \alpha\beta$. Toto řešení je nestabilní, protože 
$$\frac{\mathrm d}{\mathrm dx}(\beta x-\alpha)=\beta>0.$$ Žádné jiné
konstantní řešení neexistuje a proto všechna řešení klesají na nulu
nebo neohraničeně rostou.

Vzhledem k nestabilitě stacionárního řešení nemůžeme nechat řidiče
veřejné dopravy jezdit "jak jim to vyjde". Situace by směřovala k
tomu, že cestující budou nejprve dlouho čekat na trolejbus a nakonec
přijede několik trolejbusů těsně za sebou. (Podle knihy P.  Blanchard,
R. L. Devaney, G.  R. Hall: Differential equations, Cengage Learning
(2006), 828 pp.)

-->

## ODE tvaru $\frac{\mathrm dy}{\mathrm dx}=f(x)g(y)$ (rovnice se separovanými proměnnými)

https://youtu.be/NNQADiRyTEA

```{prf:definition} ODE se separovanými proměnnými
:nonumber:
 Diferenciální rovnice tvaru

$$    \frac{\mathrm dy}{\mathrm dx}=f(x)g(y) $$ (ODE-S)

kde $f$ a $g$ jsou funkce spojité na (nějakých) otevřených intervalech
se nazývá *obyčejná diferenciální rovnice se separovanými proměnnými.*
```


**Příklad:** Rovnice $$y'+xy +xy^2=0$$ je rovnicí se separovanými
  proměnnými, protože je možno ji zapsat ve tvaru $$y'=-xy(y+1).$$
  Rovnice $$y'=x^2-y^2$$ není rovnice se separovatelnými proměnnými.

### Řešení ODE se separovanými proměnnými

1.  Má-li algebraická rovnice $g(y)=0$ řešení $k_1$, $k_2$, …, $k_n$,
    jsou konstantní funkce $y\equiv k_1$, $y\equiv k_2$, …,
    $y\equiv k_n$ řešeními rovnice.

2.  Pracujme na intervalech, kde $g(y)\neq 0$ a odseparujeme proměnné.
    $$          \frac{\mathrm{d}y}{g(y)}=f(x)\mathrm{d}x$$

4.  Získanou rovnost integrujeme. Tím získáme obecné řešení v implicitním tvaru.
    $$           \int \frac{\mathrm{d}y}{g(y)}=\int f(x)\mathrm{d}x+C$$

5.  Pokud je zadána počáteční podmínka, je možné ji na tomto místě
    dosadit do obecného řešení a určit hodnotu konstanty $C$. Tuto
    hodnotu poté dosadíme zpět do obecného řešení a obdržíme řešení
    *partikulární*.

6.  Pokud je to možné, převedeme řešení (obecné nebo partikulární) do
    explicitního tvaru (vyjádříme odsud $y$).

Poslední krok (převod do explicitního tvaru) je volitelný, zpravidla
záleží na tom, co dalšího hodláme s řešením dělat. Pro většinu výpočtů
je však explicitní tvar vhodnější než tvar implicitní a proto se o něj
vždy snažíme.

```{prf:remark} Zápis partikulárního řešení pomocí určitého integrálu
:nonumber:
 V případě počáteční podmínky $y(x_0) = y_0$ je možné spojit třetí a čtvrtý krok a použít určitý integrál
$$
\int_{y_0}^y \frac{\mathrm{d}t}{g(t)}=\int_{x_0}^x f(t)\mathrm{d}t.
$$
```


Počáteční úloha má jediné řešení, pokud má pravá strana ohraničenou parciální derivace podle $y$, jak je zmíněno v úvodu přednášky. Nicméně pro diferenciální rovnici se separovanými proměnnými je možné vyslovit následující mnohem jednodušší postačující podmínku pro jednoznačnost řešení.

```{prf:theorem} existence a jednoznačnost řešení Cauchyovy úlohy pro rovnici se separovanými proměnnými
:nonumber:
 Je-li $g(y_0)\neq 0$, má počáteční úloha $$\frac{\mathrm dy}{\mathrm dx}=f(x)g(y),\qquad y(x_0)=y_0$$ právě jedno řešení definované v nějakém okolí počáteční podmínky.
```

\iffalse

````{prf:algorithm} Diferenciální rovnice růstu vodní kapky
:class: dropdown

Příklad ukazuje, že i u modelů přírodních procesů může být více než jedno řešení. A že to není v rozporu s tím, jak chápeme fyziku a její kauzalitu.


<div class='obtekat'>

```{figure} london.jpg
Londýnská mlha. Dnes už to není jako za časů Sherloka Holmese. Poslední velká mlha (Pea soup fog) byla v roce 1952. Zdroj: Wikipedia.
```

</div>


Modelujme růst kulové kapky. Ta roste tak, že na povrchu kondenzují
vodní páry. Kapka proto roste tak, že její objem se zvětšuje rychlostí
úměrnou povrchu. Povrch je zase úměrný druhé mocnině poloměru a
poloměr je úměrný třetí odmocnině objemu. Platí tedy (po sloučení všech konstant úměrnosti do jedné)
$$\frac{\mathrm dV}{\mathrm dt}=kV^{2/3}.$$  
Tato rovnice má konstantní řešení $V=0$. Nekonstantní řešení dostaneme
po úpravě
$$V^{-2/3}\mathrm dV=k\mathrm dt$$
a po integraci
$$\int V^{-2/3}\mathrm dV=k\int \mathrm dt,$$
což dává
$$3V^{1/3}=kt+C$$
a
$$V=\left(\frac 13 kt+ \frac 13 C\right)^3,$$
tj.
$$V=\left(k_0t+ c\right)^3,$$
kde $k_0=\frac 13 k$ a $c=\frac 13 C$ jsou konstanta spojená rychlostí
kondenzace a integrační konstanta.

Všimněte si, že počáteční úloha s počáteční podmínkou $V(0)=0$ má
konstantní nulové řešení $$V(t)=0$$ a nenulové řešení
$$V(t)=(k_0t)^3.$$ Máme zde tedy nejednoznačnost v řešení počáteční
úlohy. Tato nejednoznačnost není v rozporu s větou o existenci a
jednoznačnosti řešení, protože pravá strana je nulová (podmínka pro
separovatelnou rovnici není splněna) a nemá ohraničenou derivaci podle
$V$ (podmínka pro obecnou rovnici také není splněna). A nejednoznačnost má v tomto případě dokonce fyzikální význam. Plynné
skupenství může existovat i pod bodem kondenzace. Takovému jevu se
říká přechlazená pára. Aby došlo ke kondenzaci, musí být k dispozici
kondenzační jádra, například nečistoty ve vzduchu. Proto ve
znečištěném ovzduší dochází častěji ke kondenzaci a tvorbě mlhy. Své
by o tom mohli vyprávět obyvatelé Londýna, kteří se proslulých mlh
zbavili poté, co se omezilo topení uhlím. My dnes spíše známe
přechlazenou tekutinu ve formě hřejících polštářků, kde se po lupnutí
plíškem spustí přeměna skupenství na pevné spojená s intenzivním
uvolněním tepla.

````

````{prf:algorithm} Diferenciální rovnice vyšších řádů
:class: dropdown

https://youtu.be/ahkeA6fopaQ


<div class='obtekat'>

```{figure} satelit.jpg
Téměř veškerá klasická mechanika a dynamika pohybů se redukuje na studium diferenciálních rovnic druhého řádu. Ve vesmíru i na Zemi. Zdroj: pixabay.com.
```

```{figure} nosnik.jpg
Příhradový nosník. Vzpěry jsou namáhány v ose. Teorii vybudoval v 18. století L. Euler, ale začala se dále rozvíjet a využívat až po sérii pádů příhradových železničních mostů v 19. století. Zdroj: www.ceskestavby.cz.
```

</div>


Je-li $x$ poloha tělesa, je derivace $\frac{\mathrm dx}{\mathrm dt}$
rychlost a druhá derivace $\frac{\mathrm d^2x}{\mathrm dt^2}$
zrychlení. Podle Newtonova pohybového zákona je součin hmotnosti a
zrychlení roven výsledné působící síle. Tato síla může mít složku
závislou na poloze (například síla, která vrací těleso do rovnovážné
polohy), složku závislou na rychlosti (odporová síla prostředí) a
složku nezávislou na poloze i rychlosti (například vnější síla). Proto
je přirozené v podstatě jakýkoliv pohyb v mechanice modelovat pomocí
diferenciální rovnice druhého řádu $$m \frac{\mathrm d^2x}{\mathrm
dt^2} = - kx - b \frac{\mathrm dx}{\mathrm dt} + F.$$ Přirozeně přitom
formulujeme počáteční podmínky pro počáteční polohu a počáteční
rychlost, tj. $x(t_0)=x_0$, $\frac{\mathrm dx}{\mathrm
dt}(t_0)=x_1$. Každá počáteční úloha má právě jedno řešení. Taková
úloha se zpravidla řeší podobně jako u diferenciálních rovnic prvního
řádu: najde se obecné řešení a poté se ze všech funkcí, které splňují
danou diferenciální rovnici, vybere ta jediná, která splňuje i
počáteční podmínky. Numerický výpočet se děje podobně jako u rovnice
prvního řádu: řešení se prodlužuje po malých krocích a v rámci každého
kroku aproximujeme pohyb rovnoměrným pohybem. ([Film Hidden figures a hlavní hrdinka propočítávající dráhu pro návrat prvního amerického astronauta.](https://www.youtube.com/watch?v=v-pbGAts_Fg))

Při studiu deformací nosníků nebo kmitů strun, ploch či těles se
setkáme s diferenciálními rovnicemi typů $$\frac{\mathrm d^2x}{\mathrm
dt^2} + kx = q $$ a $$\frac{\mathrm d^4x}{\mathrm dt^4} = q. $$ U
takových úloh definujeme podmínky ve dvou různých bodech. Například u
struny nebo u oboustranně vetknutého namáhaného nosníku je v bodech
uchycení nulová výchylka a proto je přirozené formulovat okrajové
podmínky $x(0)=0$ a $x(l)=0$. Řešení takové úlohy existuje jenom pro
některé kombinace parametrů. Fyzikální rozbor ukazuje, že okrajová
podmínka je to místo, kde se objeví efekt, že struna kmitá jenom na
některých frekvencích (na základní frekvenci na kterou je naladěna a
na vyšších harmonických frekvencích). Úlohy s okrajovými podmínkami se
v praxi vyskytují v poměrně komplikovaných situacích (posuzování ne
jednoho nosníku, ale celé konstrukce) a proto se zpravidla řeší
přibližně a převádí se na řešení soustav lineárních rovnic. 

**Poznámka** Při odvození rovnice udávající deformaci zatíženého nosníku se vychází z rovnice $$\frac 1R = \frac{M}{EI},$$ kde $R$ je poloměr oskulační kružnice (jeho převrácená hodnota je křivost), $M$ je ohybový moment a $E$ a $I$ jsou konstanty související s materiálem a tvarem nosníku. Je-li osa podél nosníku $x$ a osa $y$ kolmo, je křivost dána pomocí druhé a první derivace vztahem 
$$\frac 1R = \frac{\frac{\mathrm d^2y}{\mathrm dx^2}}{\sqrt{\left(1+\left(\frac{\mathrm dy}{\mathrm dx}\right)^2\right)^3}}.$$ Toto vede na velmi komplikovanou rovnici. Pro malé deformace je první derivace blízká k nule a pokud využijeme lineární aproximaci 
$$\frac{\alpha}{\sqrt{(1+x^2)^3}}= \alpha (1+x^2)^{-3/2}\approx \alpha ,$$
dostáváme $$\frac 1R \approx \frac{\mathrm d^2y}{\mathrm dx^2},$$ což veškeré výpočty značně zjednodušuje.



## Diferenciální rovnice metodou konečných diferencí


Z přednášek o derivaci máme aproximace derivací
$$ \frac{\mathrm d f}{\mathrm dx}=f'(x)\approx  \frac{f(x+h)-f(x-h)}{2h}  $$
a 
$$ \frac{\mathrm d^2f}{\mathrm dx^2}=f''(x)\approx  \frac{f(x-h)-2f(x)+f(x+h)}{h^2}.  $$
Využijeme tuto informaci k ukázce použití na příkladu nosníku s kombinovaným namáháním.

**Příklad** (podle Autar Kaw et al.: [Finite Difference Method for
Ordinary Differential
Equations](http://nm.mathforcollege.com/topics/finite_difference_method.html).)
Deformace $y$ nosníku délky $L$ podepřeného na koncích, vystaveného
vertikálnímu zatížení $q$ a axiálnímu namáhání $T$ je dána rovnicí
$$\frac{d^2 y}{dx^2}-\frac {T}{EI} y=\frac{qx(L-x)}{2EI},$$ kde $E$ je
materiálová charakteristika a $I$ je veličina související s průřezem
nosníku (kvadratický moment průřezu, souvisí s velikostí i s tvarem). Okrajové podmínky jsou $y(0)=0$ a $y(L)=0$. 
Po dosazení za druhou derivaci dostáváme
$$\frac{y(x-h)-2y(x)+y(x+h)}{h^2}-\frac {T}{EI}
y(x)=\frac{qx(L-x)}{2EI}.$$ Pokud délku nosníku $L$ rozdělíme na $n$
částí délky $h$ a pokud označíme $x_i=hi$, $y_i=y(x_i)$, rovnice se
redukuje na rovnici $$\frac{y_{i-1}-2y_i+y_{i+1}}{h^2}-\frac {T}{EI}
y_i=\frac{qx_i(L-x_i)}{2EI}.$$ To je pro $i$ od $i=1$ po $i=n-1$
celkem $n-1$ lineárních rovnic. K tomu přidáváme rovnice na koncích
podepřeného nosníku, kdy platí $y_0=0$ a $y_n=0$. Celkem tedy máme
soustavu $n+1$ lineárních rovnic o $n+1$ neznámých. Soustava je
řešitelná. Protože pro jemné dělení je rovnic obrovské množství, není
vhodné se problém snažit zdolat metodami řešení rovnic známými ze
střední školy. Problematika spadá do oboru nazývaného lineární
algebra, kterému se začneme věnovat na příští přednášce.

Pro analogickou úlohu se vzpěrnou tlakovou pevností dřeva viz
též A. Požgaj, Štruktúra a vlastnosti dreva str. 359.


````

\fi

## Shrnutí, hlavní myšlenky

\iffalse

<div class='obtekat'>

```{figure} ../message.jpg
A jaká je hlavní message? Zdroj: pixabay.com
```

</div>

\fi

* Aplikované vědy (fyzika, biologie, nauka o materiálu, hydrologie) přirozeně formulují své zákony a poznatky mimo jiné i kvantitativně a pomocí pojmů vyjadřujících rychlosti změn. Při přepisu těchto zákonitostí do matematických modelů používáme derivaci jako rychlost růstu (případně záporně vzatou derivaci, jako rychlost poklesu). 
* Pokud známým způsobem souvisí změna veličiny popisující stav systému s velikostí této veličiny, je příslušným matematickým modelem diferenciální rovnice. S tímto jsme se setkali již mnohokrát ve cvičení během semestru.
* Naučili jsme se základní diferenciální rovnice řešit analyticky, řekli jsme si, že se dají řešit numericky (v praxi využijeme předpřipravené procedury a proto se touto problematikou nemusíme zabývat do hloubky) a naučili jsme se i rovnice transformovat do jiných proměnných, které mohou být pro studium problému přínosnější, než původní veličiny.

