# Úvod

Toto cvičení je pouze, pokud v týdením rozvrhu cvičení předchází přednášku.

## Množení bakterie _Escherichia coli_ (_E. coli_)

\iffalse 

![byfkfkrErbe, <https://commons.wikimedia.org/wiki/File:E_coli_at_10000x,_original.jpg>](ecoli.jpg)

\fi


Bakterie _E. coli_ se za optimálních podmínek dělí každých dvacet minut. Tj. za příhodné teploty, pH a při dostatku potravy z každé bakterie během dvaceti minut vzniknou bakterie dvě.

Na začátku je jedna jediná bakterie. Kolik bakterií bude za dva dny? Určete i výslednou hmotnost. Určete i funkci, která udává počet a hmotnost bakterií po uplynutí $t$ hodin. Hmotnost jedné bakterie uvažujte $10^{-12}\,\mathrm{kg}$.

Odhadněte, jestli celková hmotnost bude srovntalná s hmotností kočky (kilogramy), psa (nízké desítky kilogramů), člověka (vyšší desitky kilogramů), automobilu (tuny), Boeingu 737 (desítky tun), Empire State Building (stovky tisíc tun, <https://cs.wikipedia.org/wiki/Empire_State_Building>), Země ($5\times 10^{24}\,$kg).

Bakterie _E. coli_ je přítomna v lidském organismu ve střevech. Její případnáí přítomnost například v pitné vodě je indikátorem fekálního znečištění. Jedná se o dobře prozkoumanou bakterii, která se využívá v genovém inženýrství a biotechnologiích.

```{prf:example} Řešení
:class: dropdown
:nonumber:


Každých dvacet minut se množství bakterií zdvojnásobí. Za jednu hodinou jsou tři dvacetiminutovky. Počet zdvojnásobení je tedy roven počtu hodin vynásobených třemi.

Za $t$ hodin dostáváme
$$N(t)=1\cdot\underbrace{2\cdot 2 \cdot 2 \cdots 2}_{3t\text{-krát}} = 2^{3t}$$


Za dva dny, tj. za 48 hodin, dostáváme
$$N(48)=2^{3\times 48}=2^{144}=2\times 10^{43}.$$

Hmotnost bakterií dostaneme jako součin hmotnosti jedné bakterie a jejich počtu, tj. $$m(t)=2^{3t}\times 10^{-12}\,\mathrm{kg}.$$ Pro růst trvající dva dny dostáváme
$$m(48)=2\times 10^{31}\,\mathrm{kg},$$
což je více než hmotnost Země.
Šance, že by se podařilo bakterie "zásobovat" tak, aby se celé dva dny mohly množit optimální rychlostí, tedy není ani teoretická. Poměrně rychle dojde k vyčerpání zdrojů a omezení rychlosti růstu.


```

## Rychlost se může měnit

\iffalse 

![Theresa Knott, <https://commons.wikimedia.org/wiki/File:Pisa_experiment.png>](Pisa_experiment.png)

\fi

Uvažujme tři různé děje, kde nějaká veličina roste v čase.

* Dráha $s$ automobilu roste s časem $t$ podle funkce $$s=60t,$$
  kde dráhu a čas měříme v kilometrech a hodinách.
* Dráha $s$ objektu padajícího volným pádem (ve vakuu nebo při zandbání odporu vzduchu) roste s časem $t$ podle funkce $$s=5t^2,$$ kde dráhu měříme v metrech a čas v sekundách. Na obrázku je Galileův experiment ukazující, že rychlost volného pádu nesouvisí s hmotností, ale je opravdu jenom funkcí času.
* Počet bakterií _E. coli_ z předchozího příkladu jako funkce času v hodinách.

Porovnejte průměrnou rychlost za první dvě jednotky času (první dvě hodiny preo auto a bakterie, resp. první dvě sekundy v případě volného pádu) a za časový interval od 2 do 4 hodin resp. sekund.

Shrňte své pozorování a pokuste se toto pozorování zobecnit.


```{prf:example} Řešení
:class: dropdown
:nonumber:

U auta jsou obě průměrné rychlosti stejné a budou stejné i pro jakýkoliv jiný časový úsek.

U volného pádu a růstu bakterií průměrná rychlost roste.

```


## Rychlost nemusí být jenom pro funkce času

\iffalse 

![Harold17, <https://commons.wikimedia.org/wiki/File:Lanov%C3%A1_dr%C3%A1ha_Punkevn%C3%AD_jeskyn%C4%9B-Macocha,_lanovka(2).jpg>](Lanova_draha_Punkevni_jeskyne.jpg)

\fi


Jak rychle stoupá lanovka v Moravském krasu mezi Punkevními jeskyněmi a Macochou?

## Rychlost může záviset na jiné rychlosti


\iffalse 

![<https://ekolist.cz/cz/zpravodajstvi/zpravy/pred-50-lety-byl-objeven-nejdelsi-jeskynni-system-v-cr-amaterska-jeskyne>](stara_amaterska_jeskyne.jpg)

\fi


V Moravském krasu se po vydatných deštích zatopila jeskyně. S prohlídkami je nutné počkat, až voda opadne. Hladina vody klesá rychlostí 0.5 centimetru na metr krychlový, tj. pokud odteče metr krychlový vody, klesne hladina o půl centimetru. Přirozeným odtokem odtéká voda rychlostí tři metry krychlové za den. Jak rychle klesá hladina v centimetrech za den?

Vyřešte úlohu pro zadané konkrétní hodnoty a pokuste se sestavit obecný vztah, který umožní vypočítat rychlost poklesu hladiny v čase z rychlosti odtoku vody a rychlosti poklesu hladiny v závislosti na množství vody.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Za den odtečou tři metry krychlové. Každý metr krychlový, který odteče, způsobí pokles hladiny o půl centimeetru. Tři metry krychlové, které odtečou za den, tedy způsobí snížení hladiny o centimetr a půl. Voda klesá rychlostí jeden a půl centimetru za den. 

Pro jiné hodnoty je rychlost poklesu hladiny v centimetrech za den rovna rychlosti odtoku (v metrech krychlových za den) vynásobenému rychlostí, s jakou klesá hladina v závislosti na objemu odtečené vody (v centimetrech výšky hladiny na metr krychlový odtečené vody).

```

## Informační zdroje

* Moodle na MENDELU
* WeBWorK na UM 

Kde co najdu, jak se přihlásím, ukázky práce.
