# Úvod

Toto cvičení je pouze, pokud v týdením rozvrhu cvičení předchází přednášku. V první úloze si připomeneme exponenciální funkci a jednu její zajímavou vlastnost (neintuitivní rychlost růstu). V dalších úlohách se podíváme na výpočet rychlosti, protože na to navazujeme na přednášce. A na závěr něco k soustavám lineárních rovnic.

## Informační zdroje

* [Moodle na MENDELU, předmět Matematika](https://moodle.mendelu.cz/course/view.php?id=381). Přihlášení přes Shibboleth pomocí údajů pro přihlášení do UIS. Poté pro zápis do předmětu použijete kód rozlišující formu studia (presenční versus kombinovaná). Zde jsou učební materiáy, podmínky pro ukončení. Odsud se autentizujete do systému pro domácí úkoly.
* WeBWorK na UM. Systém pro domácí úkoly. Přístup je automaticky z Moodle opory. Domácí úkoly se otevírají a uzavírají podle nastaveného harmonogramu. Plněním těchto nepovinných domácích úkolů si můžete výrazně snížit laťku nutnou pro překonání zkoušky a vylepšit známku. Více viz podmínky pro ukončení předmětu v Moodle.


## Bakterie _Escherichia coli_ (_E. coli_)



\iffalse 

```{figure} ecoli.jpg
Bakterie *E. Coli*, autor: byfkfkrErbe, <https://commons.wikimedia.org/wiki/File:E_coli_at_10000x,_original.jpg>
```

\fi

Michael Crichton (autor scénáře k Jurskému parku) ve svém převratném sci-fi Kmen Andromeda (1969) napsal: _Matematika neomezeného růstu je děsivá. Jediná buňka bakterie E. coli se za příznivých okolností dělí každých dvacet minut. Na tom není nic tak zlého, pokud si neuvědomíme, že se bakterie dělí geometrickou řadou. Z jedné vzniknou dvě, ze dvou čtyři, ze čtyř osm a tak dále. Takto lze dojít k závěru, že by se za jeden den mohla jedna buňka rozrůst do superkolonie velikosti a váhy celé planety Země._

V něčem měl spisovatel pravdu. Bakterie _E. coli_ se za optimálních podmínek dělí každých dvacet minut. Tj. za příhodné teploty, pH a při dostatku potravy z každé bakterie během dvaceti minut vzniknou bakterie dvě.

Je pravdivý i zbytek? Uvažujme na začátku jednu jedinou bakterii. Kolik bakterií bude za 24 hodin? Určete i výslednou hmotnost. Určete i funkci, která udává počet a hmotnost bakterií po uplynutí $t$ hodin. Hmotnost jedné bakterie uvažujte $10^{-12}\,\mathrm{g}$.

Srovnejte s hmotností kočky (kilogramy), psa (nízké desítky kilogramů), člověka (vyšší desitky kilogramů), automobilu (tuny, $10^3\,\mathrm {kg}$), Boeingu 737 (desítky tun, $10^4\,\mathrm {kg}$), Empire State Building (stovky tisíc tun, <https://cs.wikipedia.org/wiki/Empire_State_Building>, $10^8\,\mathrm {kg}$), Země ($5\times 10^{24}\,$kg).

Bakterie _E. coli_ je přítomna v lidském organismu ve střevech a většina jejích kmenů je neškodná. Její případná přítomnost například v pitné vodě je indikátorem fekálního znečištění. Jedná se o dobře prozkoumanou bakterii, která se využívá v genovém inženýrství a biotechnologiích.

```{prf:example} Řešení
:class: dropdown
:nonumber:


Každých dvacet minut se množství bakterií zdvojnásobí. Za jednu hodinu jsou tři dvacetiminutovky. Počet zdvojnásobení je tedy roven počtu hodin vynásobených třemi.

Za $t$ hodin dostáváme pro počet bakterií funkci
$$N(t)=1\cdot\underbrace{2\cdot 2 \cdot 2 \cdots 2}_{3t\text{-krát}} = 2^{3t}.$$


Za den, tj. za 24 hodin, dostáváme
$$N(24)=2^{3\times 24}=2^{72}=4.7\times 10^{21}.$$

Hmotnost bakterií dostaneme jako součin hmotnosti jedné bakterie a jejich počtu, tj. $$m(t)=2^{3t}\times 10^{-12}\,\mathrm{g}=2^{3t}\times 10^{-15}\,\mathrm{kg}.$$ Pro růst trvající celý den dostáváme
$$m(24)=4.7\times 10^{6}\,\mathrm{kg}.$$ Není to hmotnost Země, ale i tak to je úctyhodné číslo. Šance, že by se podařilo bakterie "zásobovat" tak, aby se celý den mohly množit optimální rychlostí, tedy není ani teoretická. Poměrně rychle dojde k vyčerpání zdrojů a omezení rychlosti růstu.


Pro zajímavost, při růstu dva dny bychom měli
$$m(48)=2.2 \times 10^{28}\,\mathrm{kg},$$
což je více než hmotnost Země.

```

## Rychlost se může měnit

\iffalse 

```{figure} Pisa_experiment.png
Šikmá věž v Pise, na které prováděl své slavné experimenty s volným pádem G. Galilei, autor: Theresa Knott, <https://commons.wikimedia.org/wiki/File:Pisa_experiment.png>
```

\fi

Uvažujme tři různé děje, kde nějaká veličina roste v čase.

* Dráha $s$ automobilu roste s časem $t$ podle funkce $$s=60t,$$
  kde dráhu a čas měříme v kilometrech a hodinách.
* Dráha $s$ objektu padajícího volným pádem (ve vakuu nebo při zanedbání odporu vzduchu) roste s časem $t$ podle funkce $$s=5t^2,$$ kde dráhu měříme v metrech a čas v sekundách. Na obrázku je Galileův experiment ukazující, že rychlost volného pádu nesouvisí s hmotností, ale je opravdu jenom funkcí času.
* Počet bakterií _E. coli_ z předchozího příkladu jako funkce času v hodinách.

Porovnejte průměrnou rychlost za první dvě jednotky času (první dvě hodiny pro auto a bakterie, resp. první dvě sekundy v případě volného pádu) a za časový interval od 2 do 4 hodin resp. sekund.

Shrňte své pozorování a pokuste se odhadnou, pro jaké funkční závislosti budou
průměrné rychlosti stejné, ať použijeme libovolný interval. (Možná pomůže obrázek.)


```{prf:example} Řešení
:class: dropdown
:nonumber:

U auta jsou obě průměrné rychlosti stejné a budou stejné i pro jakýkoliv jiný časový úsek.

U volného pádu a růstu bakterií průměrná rychlost roste.

Průměrná rychlost nezávisí na intervalu, pokud je grafem přímka, tj. pro lineární funkce. 

Obrázky je možné vygenerovat pomocí [Wolfram Alpha](https://www.wolframalpha.com/input?i=draw+2%5E%283t%29) (jednoduché, rychlé) nebo pomocí [Pythonu](https://gist.github.com/robert-marik/d61794d36e9caf503dba96c61c856981) (vyspělejší postup, může být součástí složitější simulace, není nutné se bát syntaxe příkazů, pokud využijeme pomoc umělé interligence).

```


## Rychlost nemusí být jenom pro funkce času

\iffalse 

```{figure} Lanova_draha_Punkevni_jeskyne.jpg
Lanovka mezi Macochou a Punkevními jeskyněmi, autor: 
Harold17, <https://commons.wikimedia.org/wiki/File:Lanov%C3%A1_dr%C3%A1ha_Punkevn%C3%AD_jeskyn%C4%9B-Macocha,_lanovka(2).jpg>
```

\fi


Jak rychle stoupá lanovka v Moravském krasu mezi Punkevními jeskyněmi a
Macochou? Jedná se o nejprudší lanovku v ČR. Výškový rozdíl mezi stanicemi je
131 metrů, vodorovná vzdálenost je 207 metrů
(<https://www.kudyznudy.cz/ceska-nej/dopravni/lanovka-v-moravskem-krasu>).
Vypočtěte průměrnou rychlost stoupání lanovky (průměrný sklon). 


```{prf:example} Řešení
:class: dropdown
:nonumber:

$$\frac{131}{207}=0.63$$

```

## Rychlost může záviset na jiné rychlosti


\iffalse 

```{figure} stara_amaterska_jeskyne.jpg
<https://ekolist.cz/cz/zpravodajstvi/zpravy/pred-50-lety-byl-objeven-nejdelsi-jeskynni-system-v-cr-amaterska-jeskyne>
```

\fi


V Moravském krasu se po vydatných deštích zatopila jeskyně. S prohlídkami je nutné počkat, až voda opadne. Hladina vody klesá rychlostí 0.5 centimetru na metr krychlový, tj. pokud odteče metr krychlový vody, klesne hladina o půl centimetru. Přirozeným odtokem odtéká voda rychlostí tři metry krychlové za den. Jak rychle klesá hladina v centimetrech za den?

Vyřešte úlohu pro zadané konkrétní hodnoty a pokuste se sestavit obecný vztah, který umožní vypočítat rychlost poklesu hladiny v čase z rychlosti odtoku vody a rychlosti poklesu hladiny v závislosti na množství vody.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Za den odtečou tři metry krychlové. Každý metr krychlový, který odteče, způsobí pokles hladiny o půl centimetru. Tři metry krychlové, které odtečou za den, tedy způsobí snížení hladiny o centimetr a půl. Voda klesá rychlostí jeden a půl centimetru za den. 

Pro jiné hodnoty je rychlost poklesu hladiny v centimetrech za den rovna rychlosti odtoku (v metrech krychlových za den) vynásobenému rychlostí, s jakou klesá hladina v závislosti na objemu odtečené vody (v centimetrech výšky hladiny na metr krychlový odtečené vody).

```

## Soustavy lineárních rovnic

Soustavy dvou rovnic o dvou neznámých můžeme řešit dosazovací nebo sčítací metodou. Dosazovací metoda je jednodušší, ale sčítací metodu je snadné rozšířit na libovolný počet rovnic a libovolný počet neznámých. Zopakujeme si (ze střední školy) obě metody.


