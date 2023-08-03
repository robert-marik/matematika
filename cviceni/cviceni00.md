# Úvod

Toto cvičení je pouze, pokud v týdením rozvrhu cvičení předchází přednášku.

## Množení bakterie _Escherichia coli_ (_E. coli_)

Bakterie _E. coli_ se za optimálních podmínek dělí za dvacet minut. Tj. za příhodné teploty, pH a při dostatku potravy z každé bakterie během dvaceti minut vzniknou bakterie dvě.

Na začátku je jedna jediná bakterie. Kolik bakterií bude za dva dny? Určete i výslednou hmotnost. Určete i funkci, která udává počet a hmotnost bakterií po uplynutí $t$ hodin. Hmotnost jedné bakterie uvažujte $10^{-12}\,\mathrm{kg}$.

Odhadněte, jestli celková hmotnost bude srovntalná s hmotností kočky (kilogramy), psa (nízké desítky kilogramů), člověka (vyšší desitky kilogramů), automobilu (tuny), Boeingu 737 (desítky tun), Empire State Building (stovky tisíc tun, <https://cs.wikipedia.org/wiki/Empire_State_Building>), Země ($5\times 10^{24}\,$kg).

```{prf:example} Řešení
:class: dropdown
:nonumber:

$$N(t)=2^{3t}$$

Za dva dny, tj. za 48 hodin, dostáváme
$$N(48)=2^{144}=2\times 10^{43}.$$

Hmotnost je $$m(t)=2^{3*t}\times 10^{-12}\,\mathrm{kg},$$ tj.
$$m(48)=2\times ^{31}\,\mathrm{kg},$$
což je více než hmotnost Země.

```

## Rychlost se může měnit


* Dráha $s$ automobilu roste s časem $t$ podle funkce $$s=60t,$$
  kde dráhu a čas měříme v kilometrech a hodinách.
* Dráha $s$ objektu padajícího volným pádem ve vakuu roste s časem $t$ podle funkce $$s=5t^2,$$ kde dráhu měříme v metrech a čas v sekundách.
* Exponenciální růst bakterií z předchozího příkladu, počet bakterií jako funkce času v hodinách.

Porovnejte průměrnou rychlost za první dvě jednotky času (první dvě hodiny, první dvě sekundy v případě voného pádu) a za časový interval od 2 do 4 hodin resp. sekund.


## Rychlost nemusí být jenom pro funkce času

Jak rychle stoupá lanovka v Moravském Krasu mezi Punkevními jeskyněmi a Macochou?

## Rychlost může záviset na jiné rychlosti

V Moravkém krasu se po vydatných deštích zatopila jeskyně. S prohlídkami je nutné počkat, až voda opadne. Hladina vody klesá rychlostí 0.5 centimetru na metr krychlový, tj. pokud odteče metr krychlový vody, klesne hladina o půl centimetru. Přirozeným odtokem odtéká voda rychlostí tři metry krychlové za den. Jak rychle klesá hladina v centimetrech za den?

Vyřešte úlohu pro kokrétní hodnoty a pokuste se sestavit obecný vztah, který umožní vypočítat rychlost poklesu hladiny v čase z rychlosti odtoku vody a rychlosti poklesu hladiny v závislosti na množství vody.