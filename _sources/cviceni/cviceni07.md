# Diferenciální rovnice

_Umění najít řešení diferenciální rovnice je sympatické a naučíme se v úvodním příkladě. Není to však nic proti umění sestavit model (naučili jsme se již ve druhém týdnu a připomeneme si v následujícím příkladě s tloušťkou ledu), umění posoudit jednoznačnost řešení (většina modelů se řeší numericky a musíme být přesvědčeni o smysluplnosti takové činnosti) a  stabilitu řešení (řešení, která nejsou stabilní, jsou sice v souladu s přírodními zákony, ale pravděpodobnost jejich spontánního výskytu je nulová). Jednoznačnost a zjednodušenou verzi stability řešení (stabilita konstantních řešení) jsme viděli na přednášce a připomeneme v dalších příkladech._

## Řešení ODE a IVP 

1. $\frac{\mathrm dy}{\mathrm dx}=xy^2$
1. $\frac{\mathrm dy}{\mathrm dt}=te^y$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y,\ \ y(0)=1$
1. $\frac{\mathrm dr}{\mathrm dt}=kr^3,\ \ r(0)=r_0>0$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2,\ \ m(0)=0$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2,\ \ m(0)=-2$

```{prf:example} Řešení
:class: dropdown
:nonumber:

1. $\frac{\mathrm dy}{\mathrm dx}=x\cdot y^2$
   *  Konstantní řešení jsou řešení rovnice $$ y^2=0,$$ tj. je jediné konstantní řešení $$ y=0.$$
    * Pro nekonstantní řešení dostaneme po separaci  $$ y^{-2}\mathrm dy=x\mathrm dx $$ a integrováním $$ -\frac 1y=\frac 12 x^2+C.$$
1. $\frac{\mathrm dy}{\mathrm dt}=t\cdot e^y$
    * Konstantní řešení jsou řešení rovnice $$ e^y=0.$$ Protože tato rovnice nemá řešení, zadaná diferenciální rovnice nemá konstantní řešení.
    * Pro nekonstantní řešení dostaneme po separaci  $$ e^{-y}\mathrm dy= t\mathrm dt$$ a integrováním $$ -e^{-y}=\frac 12 t^2 +C.$$
1. $\frac{\mathrm dy}{\mathrm dx}=x\cdot \sqrt y$
    * Konstantní řešení jsou řešení rovnice $$ \sqrt y=0,$$ tj. jediné řešení $$ y=0.$$
    * Pro nekonstantní řešení dostaneme po separaci  $$ \frac 1{\sqrt y}\mathrm dy=x\mathrm dx $$ a integrováním $$ 2\sqrt y=\frac 12 x^2+C.$$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y,\ \ y(0)=1$
    * Konstantní řešení $$y=0$$ (viz předchozí příklad) nesplňuje počáteční podmínku a proto jej nemusíme uvažovat
    * Obecné řešení  $$ 2\sqrt y=\frac 12x^2 +C$$ dává po dosazení $x=0$ a $y=1$ rovnici $$2\sqrt 1=0+C.$$ Odsud dostáváme $C=2$ a řešení zadané počáteční úlohy je $$2\sqrt y=\frac 12 x^2+2.$$
1. $\frac{\mathrm dr}{\mathrm dt}=k\cdot r^3,\ \ r(0)=r_0>0$
    * Konstantní řešení jsou řešení rovnice $$ r^3=0,$$ tj. jediné konstantní řešení je $$ r=0$$ a toto řešení nesplňuje počáteční podmínku.
    * Pro nekonstantní řešení dostaneme po separaci  $$ r^{-3}\mathrm dr=k\mathrm dt $$ a integrováním $$ -\frac 12 r^{-2}=kt+C.$$ Dosazením počáteční podmínky $t=0$, $r=r_0$ dostáváme $$ -\frac 12 r_0^{-2}=C.$$ Tím je dána konstanta $C$ a po použití této konstanty v obecném řešení dostáváme řešení počáteční úlohy ve tvaru $$ -\frac 12 r^{-2}=kt-\frac 12 r_0^{-2}.$$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2$, $m(0)=0$
    * Konstantní řešení jsou řešení rovnice $$ m+2=0,$$ tj. $$ m=-2$$ a toto řešení nesplňuje počáteční podmínku.
    * Pro nekonstantní řešení dostaneme po separaci  $$ \frac1{m+2}\mathrm dm=dt $$ a integrováním $$ \ln|m+2|=t+C.$$ Po dosazení počáteční podmínky $t=m=0$ dostáváme $$C=\ln 2$$ a počáteční úloha má řešení $$\ln(m+2)=t+\ln (2).$$ (Vzhledem k počáteční podmínce je $m$ kladné a nemusíme psát absolutní hodnotu.)
1. $\frac{\mathrm dm}{\mathrm dt}=m+2$, $m(0)=-2$
    * Konstantní řešení jsou řešení rovnice $$ m+2=0,$$ tj. $$ m=-2.$$ Toto řešení splňuje počáteční podmínku.
    * Pravá strana má ohraničenou (dokonce konstantní) derivaci podle $m$. Proto je řešení každé počáteční úlohy určeno jednoznačně. Řešení z předchozího bodu je jediné a další nemusíme hledat.

```

## Tloušťka ledu

\iffalse 

```{figure} ledni_medved.jpg
pixabay.com
```

\fi 

Takzvaný Stefanův zákon (J. Stefan, \"Uber die Theorie der Eisbildung, insbesondere \"uber die Eisbildung im Polarmeere, 1891) vyjadřuje že tloušťka ledu na hladině moře roste ve
stabilních podmínkách rychlostí nepřímo úměrnou této tloušťce. Zapište
tento fakt pomocí vhodného matematického modelu a najděte řešení
vzniklé diferenciální rovnice.

```{prf:example} Řešení
:class: dropdown
:nonumber:

$$
\begin{aligned}
\frac{\mathrm dh}{\mathrm dt}&=\frac kh\\
h\,\mathrm dh&=k\, \mathrm dt\\
\int h\,\mathrm dh&=\int k\, \mathrm dt\\
\frac {h^2}{2}&=kt+C\\
\end{aligned}
$$

```

## Model vypouštění nádrže

\iffalse 

```{figure} voda_plastovky.jpg
www.rodovystatek.cz
```

\fi 

Z fyziky je známo, že rychlost s jakou
vytéká tekutina otvorem u dna nádoby je úměrná odmocnině výšky hladiny
(protože se mění potenciální energie úměrná výšce na kinetickou
energii úměrnou druhé mocnině rychlosti). Proto je i rychlost s jakou
se zmenšuje objem vody v nádrži úměrná odmocnině výšky
hladiny.

Ukažte, že matematickým popisem procesu je diferenciální rovnice.
Napište rovnici pro výšku hladiny vody v nádrži jako funkci času.
Uvažujte tři případy:
nádrž *cylindrického tvaru* (válec postavený na podstavu),
nádrž ve tvaru
*kvádru* 
a nádrž ve tvaru *kužele* otočeného vrcholem dolů (trychtýř). 

_V tomto příkladě vystupuje derivace jak rychlost, ale po přepisu zadání do modelu máme v rovnici dvě různé veličiny, které se mění: objem vody a výšku hladiny. Musíme ještě najít a použít vztah mezi rychlostmi změn těchto veličin. Fyzikální zákon je formulován pro derivaci objemu a nás zajímá derivace výšky._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Buď $V$ objem vody a $h$ výška hladiny od dna.
Podle zadání ve všech případech platí $$\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h$$ a musíme derivaci $\frac {\mathrm dV}{\mathrm dt}$ vyjádřit pomocí $\frac {\mathrm dh}{\mathrm dt}$.

Pro cylindr, kvádr nebo jakoukoliv nádrž se svislými stěnami je objem úměrný výšce hladiny, $V=k_2 h$, a proto $\frac {\mathrm dV}{\mathrm dt}=k_2\frac {\mathrm dh}{\mathrm dt}$. Odsud
$$k_2\frac {\mathrm dh}{\mathrm dt}=\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h,$$
tj.
$$\frac {\mathrm dh}{\mathrm dt}=-\frac{k_1}{k_2}\sqrt h$$
a pro $k=\frac{k_1}{k_2}$ má model tvar
$$\frac {\mathrm dh}{\mathrm dt}=-k\sqrt h.$$

Pro kužel platí díky konstantnímu úhlu u vrcholu vztah $V=k_3h^3$ (díky podobnosti je objem přímo úměrný třetí mocnině libovolného délkového parametru) a proto
$\frac {\mathrm dV}{\mathrm dt}=k_3 \times 3h^2 \frac {\mathrm dh}{\mathrm dt}$.
Odsud
$$3k_3 h^2 \frac {\mathrm dh}{\mathrm dt}=\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h,$$
tj. 
$$\frac {\mathrm dh}{\mathrm dt}=-\frac{k_1}{3k_3}h^{-3/2}$$
a po přeznačení konstanty má model pro kuželovou nádrž tvar
$$\frac {\mathrm dh}{\mathrm dt}=-kh^{-3/2}.$$

```

## Problematika jednoznačnosti v modelu vypouštění nádrže

<div class="shorten" data-text="Příklad ukazuje, že nemusí být vždy jednoznačně určené řešení a že to není fyzikální nesmysl. Zde není jednoznačnost při prodlužování zpětně v čase.">

\iffalse 

```{figure} voda_plastovky.jpg
www.rodovystatek.cz
```

\fi 

Dříve jsme odvodili rovnici
$$\frac{\mathrm dh}{\mathrm dt}=-k\sqrt h$$
popisující úbytek hladiny vody v nádrži tvaru kvádru, ze které vypouštíme vodu.

1. Zkontrolujte, že pro $h>0$ má každá počáteční úloha jediné řešení. Interpretujte tento výsledek prakticky.
1. Pro $h=0$ by řešení nemuselo být určeno jednoznačně. A opravdu
  není. Řešením je například $h(t)=0$ nebo $$h(t)=   \begin{cases}
    \frac 14 k^2 t^2 & t<0\\
    0 & t\geq 0.
  \end{cases}$$
Zkontrolujte dosazením (pozor: pro $t<0$ platí $\sqrt {t^2}=|t|=-t$) a rozmyslete, jestli nejednoznačnost je jenom matematický trik, nebo jestli má
 fyzikální interpretaci.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Ad 1: Nabídneme dvě  varianty, pro argumentaci je možno použít kteroukoliv z nich. 

* *Podle obecné věty o jednoznačnosti:* Stačí ověřit, že pravá strana má ohraničenou parciální derivaci podle $h$. Protože platí
  $$\frac{\partial }{\partial h}(k\sqrt h)=k\frac 12
  h^{-1/2}=\frac{k}{2\sqrt h}$$ a tato derivace je definovaná a
  ohraničená v nějakém okolí libovolného bodu splňujícího $h>0$.
  Podle věty o existenci a jednoznačnosti řešení obecné
  diferenciální rovnice má počáteční úloha právě jedno řešení.
* *Podle věty o jednoznačnosti pro rovnici se separovanými proměnnými:* Stačí ověřit,
  že část závislá na $h$ je nenulová. Toto jistě platí, protože pro
  $h>0$ je $\sqrt{h}\neq 0$. 

Pokud je tedy v nádrži nějaká voda, je jednoznačně dáno, jak bude vytékat a je možné vypočítat, jaká bude v libovolném okamžiku hladina.

Ad 2: Pro $h=\frac 14 k^2 t^2$ a $t<0$ dostáváme
    $$\begin{aligned}
      \frac{\mathrm dh}{\mathrm dt}&=\frac 14 k^2 \cdot 2t = \frac 12 k^2 t\\
      -k\sqrt h&=-k\sqrt{\frac 14 k^2 t^2} = - k \frac 12 |k| \cdot |t| =       - k \frac 12 k (-t) = \frac 12 k^2 t
    \end{aligned}  $$
    a obě strany rovnice jsou stejné. Pro $h=0$ je dosazení triviální.

Je-li $h(t_0)=0$, může to být proto, že voda v čase $t_0$ právě vytekla, nebo proto, že vytekla před hodinou nebo proto, že v nádrži nikdy voda nebyla. Proto je nejednoznačnost přirozená. Například $h(t)=0$ je řešení odpovídající tomu, že voda v nádrži nikdy nebyla. Funkce $h(t)=\frac 14 k^2t^2$ pro $t<0$ odpovídá tomu, že pro $t<0$ v nádrži voda byla a vytekla v čase $t=0$.

```

</div>

## Stavebniny vedle čebínského nádraží: model

\iffalse 

```{figure} pokros.jpg
vlastní
```

\fi 

Hromada sypkého materiálu má tvar kužele. Úhel u vrcholu je
konstantní, daný mechanickými vlastnostmi materiálu a je nezávislý na
objemu. Předpokládejme, že personál stavebnin přisypává na hromadu
materiál konstantní rychlostí (v jednotkách objemu za jednotku
času). Tato hromada je však v poměrně otevřené krajině a vítr
rozfoukává materiál po okolí. Je rozumné předpokládat, že rozfoukávání
(opět v jednotkách objemu za jednotku času) se děje rychlostí úměrnou
povrchu návětrné strany pláště. Vyjádřete proces kvantitativně pomocí
derivací.  Napište rovnici pro derivaci objemu hromady podle času.

_Toto je podobný model jako model vypouštění nádrže, ale kratší. Opět máme po přepisu zadání do matematického modelu dvě veličiny měnící se s časem v jedné rovnici. Derivace objemu, která nás zajímá, již v rovnici přítomna naštěstí je. Stačí vyjádřit obsah pomocí objemu, nejlépe pomocí rozměrové analýzy._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Rychlost s jakou se mění objem je $\frac{\mathrm dV}{\mathrm dt}$, rychlost přisypávání označme $R$, povrch návětrné strany $S$.
Podle zadání platí
$$  \frac{\mathrm dV}{\mathrm dt} = R - k_0S.$$
Protože kužel má stále stejný tvar, objem jednoznačně determinuje rozměry, povrch kužele, nebo i povrch poloviny pláště, tj. povrch návětrné strany. Z rozměrové analýzy na základě Buckinghamova Pi-teorému z přednášky je zřejmé, že musí platit úměrnost mezi takovými mocninami těchto veličin, pro které jednotky "pasují", Existuje tedy konstanta taková, že $$S=k_1V^{\frac 23}.$$ Spojením těchto dvou vztahů dostáváme
$$  \frac{\mathrm dV}{\mathrm dt} = R - k V^{\frac 23},$$
kde $r$ a $k=k_0k_1$ jsou konstanty.

```

## Stavebniny vedle čebínského nádraží: stabilita řešení

\iffalse 

```{figure} pokros.jpg
vlastní
```

\fi 

Hromada sypkého materiálu má tvar kužele. Úhel u vrcholu je konstantní, daný
mechanickými vlastnostmi materiálu a je nezávislý na
objemu. V předchozím příkladě jsme sestavili diferenciální rovnici popisující růst hromady ve tvaru
$$\frac{\mathrm dV}{\mathrm dt}=R-kV^{\frac 23},$$
kde $R$ je rychlost přisypávání a $k$ konstanta.

1. Existuje konstantní řešení? Pokud ano, je stabilní nebo nestabilní? Zdůvodněte.
1. Může hromada skončit i při neustálém přisypávání celá rozfoukaná?
1. Mohou pracovníci navršit hromadu do libovolné výšky anebo pro velkou hromadu je již rozfoukávání rychlejší než přisypávání?

```{prf:example} Řešení
:class: dropdown
:nonumber:

Označme $f(V)=R-kV^{\frac 23}$.
Konstantní řešení je řešením rovnice $f(V)=0$, tj. $$R-kV^{\frac 23}=0.$$ Odsud
$$V_0=\left(\frac{R}{k}\right)^{3/2}.$$ Protože $f$ klesá v bodě $V_0$, je toto řešení stabilní.

Protože $f(0)>0$, malá hromada vždy roste a proto nemůže skončit celá rozfoukaná. Pro malý objem je přisypávání intenzivnější než rozfoukávání.

Protože $f$ je pro velké $V$ záporná, pro velkou hromadu objem ubývá (více se rozfouká než přisype) a hromadu není možné navršit libovolně velkou. 

```


