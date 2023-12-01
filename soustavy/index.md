# Soustavy lineárních rovnic

```{admonition} Motivace

* Pro popis přírodních dějů je ideální jazyk derivací, protože umožňuje pracovat s okamžitými rychlostmi změn fyzikálních veličin. Pokud mechanismus děje známe, je snadné naformulovat pomocí derivací příslušný matematický model, poté ovšem přijde fáze řešení. Tady málokdy vystačíme s analytickými metodami, které jsme si ukázali v přednášce věnované diferenciálním rovnicím. Často se uchylujeme k numerickému řešení. V naprosté většině případů se toto řešení redukuje na řešení soustav lineárních rovnic. Tyto soustavy ovšem bývají obrovské, řádově obsahující tisíce rovnic a neznámých a proto středoškolské metody nejsou použitelné (například nejsou dostatečně rychlé, nebo mohou být numericky nestabilní). Z tohoto důvodu je nutné se problematice soustav rovnic věnovat podrobněji. 
* Nalezení vlastních směrů matice je zásadní pro zjednodušení popisu anizotropního materiálu, protože díky tomu, že matice má v soustavě respektující vlastní směry diagonální tvar, se redukuje počet materiálových konstant. Hledání těchto směrů je vlastně řešení soustavy lineárních rovnic. Situace je relativně jednoduchá, protože soustava má dimenzi dva nebo tři a k tomu nekonečně mnoho řešení, což výpočty urychluje. (Například ve dvourozměrném případě to znamená, že jedna rovnice je násobkem druhé a nemusíme ji uvažovat.)
* Podrobněji viz [zde](https://user.mendelu.cz/marik/mtk/soustavy_motivace.pdf). Numerický výpočet vlastních čísel [zde](https://sagecell.sagemath.org/?z=eJyVVbtu4zgU7Q34H4gEgaWBVhtnMY0BFe4WWGyQYpDGMRa0zNiMJZLDh2LpH_IBi6lSThHMF2Qb2f-194qS7HiSYgxDosjLc1-Hh-fkRktS0SUV0pGcWp5yUpRKptxSUmTUWMFJyk1GyeG7YBsrdRkPB-fkRlpGFIAIupZLwbrFA4qSS56RJcvYhsiFppVrbRxCVvBugL4wYWVr_MBIzioOD2E4WjEL7849-pFW-m235UYzk_GckTU3Vq40zYmWVSYrBrYNnosJmv6N6TEEN2XOrObpBrNSsuKWFxD6kt1zwcEFIA8HPFdSWyJcrkpCDRGqn4NCqUzajC9iVeII11VmewPD6EJqgdNGGESbJkLFVGtaBrPZVTSeR7Nx9Md8HhJyjg2on0X9cgis_u67wYaDx4gUJAH3ccYFzVYx46tgCvtgY1G_Krl7YrYtTv2SrsnuqX4xLGvqhnXe_8AAIDmyYvYfk1LAWQUumoaT4QBgyNR5fPCYuyyYRi70C5pZB1kEB99C6jyYuvD3kykXhujkOhlfwm84cOusBNDZ1ScwVByfmoqlzJtXEJJ7qQknXBD4XrHgOpxDOh2HTM50ORx0VAKco-LBMJUm4CGUEMaGCxzPQ_RhvmobnPo6coZhHTvqPJh2Bg4BEHUj3XDgmQiuT4vWoDlEa3cj4Dskb8mNZVGaCxuctQS8ExfmTpxdTMN-5fb4pE3IhTm7eGyY0bXVNxVOYc8Q1hPkLboBguP52EggR84P5xGWMulUihyZ3InGSdE4yX9hZ-_uLymslhARFwXTlZDG8g72wKUiKuIvoSerhXYYJYUsqKifO694HKXbPVEjdt86MEi4WYZ3AOJi4TCTB2AFKELGDzXoNetQyd8--p1hEKS3u2YPXl2W0lCQitK3cNLFT3PgVTPVRi_e33AM6GXqQ0C6PQV8bwMWRGm6gbQ2JShZwYTXv9x1CggjJEpDLTy6xWwSXc7JG7745hG1_xd54_YgL6-op_tnXOysvJTuvmEWcglNbkQz-UkoiKd4_QIcr7-_R_K2CjdNCngfvL0sgFy-eqci7utz5D3EJg0H93wVEbo1EAwIa2zcAnXWBOPoKiKwaHjFkmB8FX32ykO3YAn2s8s5fsR4GfhyR2TBBeJ8vgybJQPJWW4zFoz-7K8Mf1E0p788SW7UOGhCmXHAh_9BUToNGA7K1mD8kUEf4hg-4FqIocLWMo2JBdtkayJSJiU8144lbeiKZgxskpFh3OQ8Hf2Uwi2vHDSqonCWlHT7_7itX-EWgCOGNW7G3T1wtJsaxVIbjNhX2N3OZ2zFQDAb4GR0c9xvX4OmE2v5GIT_A0gl31s=&lang=python&interacts=eJyLjgUAARUAuQ==)
```

https://youtu.be/yAozKR9QBls

## Varianty zápisu soustavy lineárních rovnic

https://youtu.be/E1Ey_xz6_ig

Uvažujme následující tři problémy: 

1. Najděte všechna reálná čísla $x_1$, $x_2$, splňující dvojici rovnic $$ \begin{aligned}   4x_1&+5x_2=7\\   \phantom{4}x_1&-2x_2=4 \end{aligned} $$
1. Najděte všechna reálná čísla $x_1$, $x_2$, splňující vektorovou rovnici $$   \begin{aligned} \begin{pmatrix}       4\\1     \end{pmatrix}     x_1     +     \begin{pmatrix}       5\\-2     \end{pmatrix}     x_2     =     \begin{pmatrix}       7\\4     \end{pmatrix}   \end{aligned}$$
1. Najděte všechna reálná čísla $x_1$, $x_2$, splňující maticovou rovnici $$\begin{aligned}     \begin{pmatrix}       4&5\\1&-2     \end{pmatrix}     \begin{pmatrix}       x_1\\x_2     \end{pmatrix}     =     \begin{pmatrix}       7\\4     \end{pmatrix}   \end{aligned} $$

Všechny problémy jsou ekvivalentní a jedná se o jiný zápis téhož.
Jednou však používáme soustavu rovnic, vektory a jejich lineární
kombinaci a jednou matice a maticový součin!

## Soustava lineárních rovnic

```{prf:definition} Soustava lineárních rovnic
:nonumber:
 *Soustavou $m$ lineárních rovnic  o $n$ neznámých* nazýváme soustavu rovnic 
 
 $$  \begin{gathered}   a_{11}x_1+a_{12}x_2+a_{13}x_3+\cdots+a_{1n}x_n=b_1 \\   a_{21}x_1+a_{22}x_2+a_{23}x_3+\cdots+a_{2n}x_n=b_2 \\   a_{31}x_1+a_{32}x_2+a_{33}x_3+\cdots+a_{3n}x_n=b_3 \\   \vdots \\   a_{m1}x_1+a_{m2}x_2+a_{m3}x_3+\cdots+a_{mn}x_n=b_m \end{gathered} $$ (soustava1)
 
 Proměnné $x_1$, $x_2$, ..., $x_n$ nazýváme *neznámé*. Reálná čísla $a_{ij}$ nazýváme *koeficienty levých stran*, reálná čísla $b_j$ *koeficienty pravých stran* soustavy rovnic. *Řešením soustavy rovnic* rozumíme uspořádanou $n$-tici reálných čísel $[t_1, t_2, \ldots, t_n]$ po jejichž dosazení za neznámé (v tomto pořadí) do soustavy dostaneme ve všech rovnicích identity.
```


```{prf:definition} Matice soustavy
:nonumber:
 Matici 
  $$
   A=\left(
    \begin{matrix}
      a_{11}& a_{12}& a_{13}& \cdots{}& a_{1n}\\
      a_{21}& a_{22}& a_{23}& \cdots{}& a_{2n}\\
      \vdots{} &\vdots{}& {} &\ddots{}& \vdots{}\\
      a_{m1}& a_{m2}& a_{m3}& \cdots{}& a_{mn}\\      
    \end{matrix}\right)
  $$
nazýváme *maticí soustavy* {eq}`soustava1`.
Matici $$
A_r=\left(
  \begin{array}{ccccc|c}
    a_{11}& a_{12}& a_{13}& \cdots{}& a_{1n}&b_1\\
    a_{21}& a_{22}& a_{23}& \cdots{}& a_{2n}&b_2\\
    \vdots{} &\vdots{}& {} &\ddots{}& \vdots{}&\vdots\\
    a_{m1}& a_{m2}& a_{m3}& \cdots{}& a_{mn}&b_m\\
  \end{array}
\right)
$$
nazýváme *rozšířenou maticí soustavy* {eq}`soustava1`.
```


## Vektorový zápis soustavy lineárních rovnic

  Soustavu {eq}`soustava1` lze ekvivalentně přepsat do vektorového
  tvaru
\dm $$    \begin{pmatrix}      a_{11}\\a_{21}\\\vdots\\a_{m1}    \end{pmatrix}    x_1+    \begin{pmatrix}      a_{12}\\a_{22}\\\vdots\\a_{m2}    \end{pmatrix}    x_2+    \begin{pmatrix}      a_{13}\\a_{23}\\\vdots\\a_{m3}    \end{pmatrix}    x_3+\cdots+    \begin{pmatrix}      a_{1n}\\a_{2n}\\\vdots\\a_{mn}    \end{pmatrix}    x_n=     \begin{pmatrix}      b_{1}\\b_{2}\\\vdots\\b_{m}    \end{pmatrix}. $$
  Vidíme tedy, že se vlastně jedná o problém, vyjádřit vektor složený
  z čísel na pravé straně soustavy rovnic jako  lineární
  kombinaci vektorů, které tvoří sloupce  matice
  soustavy.

## Maticový zápis soustavy lineárních rovnic

Soustavu {eq}`soustava1` lze ekvivalentně přepsat do maticového
tvaru pomocí  maticového součinu
$$
\left(
    \begin{matrix}
      a_{11}& a_{12}& \cdots{}& a_{1n}\\
      a_{21}& a_{22}&  \cdots{}& a_{2n}\\
      \vdots{} &\vdots{} &\ddots{}& \vdots{}\\
      a_{m1}& a_{m2}&  \cdots{}& a_{mn}\\
    \end{matrix}\right) 
\left(  \begin{matrix}
    x_1\\x_2\\ \vdots \\x_n
  \end{matrix}
\right)    = \left(  \begin{matrix}
    b_1\\b_2\\ \vdots \\b_m
  \end{matrix}
\right).
$$
  Tento tvar se používá často v inženýrských výpočtech pro
  úspornost. Symbolicky zpravidla píšeme soustavu lineárních rovnic ve
  tvaru 
$$
    A\vec x=\vec b,
    $$
    nebo $$AX=B$$
  kde $A$ je  matice soustavy a $\vec b$ resp. $B$ je vektor pravých stran.

## Využití inverzní matice pro řešení soustavy lineárních rovnic

https://youtu.be/YpbOWJ_6ZS4

\iffalse

<div class='obtekat'>

```{figure} matrix.jpg
Inverzní matice umožní zapsat elegantně řešení i neuvěřitelně komplexní a složité soustavy rovnic. Pro praktické počítání se však tato metoda moc nehodí a budeme ji muset ještě o něco vylepšit na iterační metodu. Zdroj: pixabay.com.
```

</div>

\fi

Z úvodní přednášky o lineární algebře víme, že pomocí maticového násobení je možné soustavu lineárních rovnic zapsat ve tvaru $$AX=B,$$ kde $A$ je matice soustavy, $X$ je sloupcový vektor neznámých a $B$ je vektor pravých stran. Pokud má matice $A$ inverzní matici, můžeme pomocí této matice soustavu vyřešit. Po vynásobení rovnice inverzní maticí zleva dostáváme
$$A^{-1}(AX)=A^{-1}B$$
a po uplatnění asociativního zákona 
$$(A^{-1}A)X=A^{-1}B.$$
Protože výraz v závorce je součinem matice s maticí inverzní, je tento
součin roven jednotkové matici, která je neutrálním prvkem při
násobení a proto okamžitě dostáváme řešení soustavy ve tvaru 
$$X=A^{-1}B.$$
Jako přirozený důsledek vidíme, že řešení je určeno
jednoznačně. Známe-li inverzní matici, můžeme řešení dokonce vypočítat
pro libovolnou pravou stranu velmi pohodlně a rychle pomocí maticového
násobení. Bohužel, výpočet inverzní matice je zpravidla velmi drahý
(vyžaduje velké množství operací) a numericky málo stabilní. Proto je
tento postup užitečným teoretickým nástrojem, ale v praxi postupujeme
poněkud odlišně.

## Inverzní matice k diagonální matici

Diagonální matice (tj. matice, které mají nenulové prvky jenom na hlavní
diagonále) se vzhledem k násobení chovají velice hezky: součinem je
taková matice, která je diagonální a na hlavní diagonále má prvky
vytvořené jako součin odpovídajících prvků násobených matic.

$$\begin{pmatrix}  2&0&0 \\  0&3&0 \\  0&0&12  \end{pmatrix}\begin{pmatrix}  5&0&0 \\  0&7&0 \\  0&0&1  \end{pmatrix}=\begin{pmatrix}  10&0&0 \\  0&21&0 \\  0&0&12  \end{pmatrix}$$

Proto je snadné zařídit, aby v hlavní diagonále vyšly jedničky. Stačí
uvažovat podobně jako v následujícím příkladě.
$$\begin{pmatrix}  2&0&0 \\  0&3&0 \\  0&0&12  \end{pmatrix}\begin{pmatrix}  \frac 12&0&0 \\  0&\frac 13&0 \\  0&0&\frac1{12}  \end{pmatrix}=\begin{pmatrix}  1&0&0 \\  0&1&0 \\  0&0&1  \end{pmatrix}$$
a tedy
$$\begin{pmatrix}  2&0&0 \\  0&3&0 \\  0&0&12  \end{pmatrix}^{-1}=\begin{pmatrix}  \frac 12&0&0 \\  0&\frac 13&0 \\  0&0&\frac1{12}  \end{pmatrix}.$$

## Iterační metoda řešení soustav lineárních rovnic

Na předchozím slidu jsme viděli, že je jednoduché najít inverzní
matici k matici diagonální. Toho využijeme pro řešení soustavy
lineárních rovnic iterační metodou. Představíme si nejednodušší, přesto však velmi mocnou metodu, **Jacobiho metodu**.

V úvodní přednášce z lineární algebry jsme modelovali rozložení teploty ve dvourozměrné
desce pomocí soustavy rovnic
$$\begin{pmatrix} \phantom{-}4&-1& \phantom{-}0&-1\\ -1& \phantom{-}4&-1& \phantom{-}0\\ \phantom{-}0 &-1& \phantom{-}4&-1\\ -1& \phantom{-}0&-1& \phantom{-}4\end{pmatrix}\begin{pmatrix}  x_1\\x_2\\x_3\\x_4\end{pmatrix}=\begin{pmatrix}  30\\60\\70\\40\end{pmatrix}.$$
Pro
$$A=\begin{pmatrix} \phantom{-}4&-1& \phantom{-}0&-1\\ -1& \phantom{-}4&-1& \phantom{-}0\\ \phantom{-}0 &-1& \phantom{-}4&-1\\ -1& \phantom{-}0&-1& \phantom{-}4\end{pmatrix}, \quad X=\begin{pmatrix}  x_1\\x_2\\x_3\\x_4\end{pmatrix},\quad B=\begin{pmatrix}  30\\60\\70\\40\end{pmatrix}$$ tedy 

$$AX=B.$$ (soustava1b)

Rozdělíme matici $A$ na součet diagonální matice a matice s nulami v hlavní diagonále, tj. na součet matic
$$D=\begin{pmatrix} 4&0&0&0\\ 0& 4&0&0\\0 &0& 4&0\\ 0&0&0& 4\end{pmatrix}\quad \text{a}\quad T=\begin{pmatrix} \phantom{-}0&-1& \phantom{-}0&-1\\ -1& \phantom{-}0&-1& \phantom{-}0\\ \phantom{-}0 &-1& \phantom{-}0&-1\\ -1& \phantom{-}0&-1& \phantom{-}0\end{pmatrix}$$
Potom můžeme psát rovnici ve tvaru
$$(D+T)X=B$$
a odsud
$$\begin{aligned}DX+TX&=B\\ DX&=B-TX\end{aligned}$$ a využitím inverzní matice

$$X=D^{-1}(B-TX).$$ (soustava2b)

Definujme nyní iterační vzorec

$$X_{k+1}=D^{-1}(B-TX_k).$$ (soustava3b)

Podobně jako u Markovových řetězců můžeme najít postupnými iteracemi z
vhodného (nebo libovolného) počátečního stavu stacionární stav, kdy se
$X_k$ dalšími iteracemi nemění a tím dostaneme řešení rovnice {eq}`soustava2b`,
která je ekvivalentní rovnici {eq}`soustava1b`. Protože inverzní matici počítáme
pro matici diagonální, je tento výpočet velice rychlý a levný. Vlastně
není vůbec nutné mít k dispozici maticový počet. Iterace dostaneme
tak, že z první rovnice osamostatníme $x_1$, z druhé rovnice $x_2$
atd. Výchozí odhad dosadíme do pravých stran a obdržíme zpřesněný
odhad. Postup opakujeme, dokud nejsou dvě následující iterae
dostatečně blízké.

**Poznámka.** Předchozí postup je možné použít jenom v případě, že
iterační proces {eq}`soustava3b` konverguje. Pokud by nekonvergoval, není možné o
řešení rovnice nic říct, pouze to, že Jacobiho metoda
nefunguje. Postačující podmínka, kdy Jacobiho metoda konverguje, je
aby každý řádek měl v hlavní diagonále číslo, které je v absolutní
hodnotě větší než je součet absolutních hodnot zbylých čísel v tomto
řádku. Matice, která splňuje tuto podmínku se nazývá *řádkově ostře
diagonálně dominantní matice* a pro takovou matici Jacobiho metoda
konverguje. Podobně je možné uvažovat *sloupcově ostře diagonálně
dominantní matice* porovnáním absolutních hodnot diagonálních prvků se
součty absolutních hodnot ostatních prvků v daných sloupcích a i pro
sloupcově ostře diagonální matice metoda konverguje. I přes
jednoduchost tohoto kriteria se s diagonálně dominantními maticemi
setkáváme v aplikacích poměrně často. Podíváme-li se, jak byla
odvozena soustava popisující rozložení teploty na tepelně vodivé
desce (poslední slajd minulé přednášky), není to až takové překvapení.

[Online výpočet.](https://sagecell.sagemath.org/?z=eJxtj8FqwzAMhu-BvIPoLk5wMnfzOij4kJDTTjv0EMjC8GK31aFycMzY3n5O03YMZozRL_3SJ1fqpIPHL9Z1khdrLuLT8y5Gi4zxnDqrJb_Ivs_SpL41Pwq-EfxZcCn6rAxe0zS6ybJoSpNGyRyNpYDh-_3SIWOlQfpU6_v_iztVFU2atDfEk-DX-xcBdzC6QQc7EIIzR23A28kSzuy984CABNF_sOxBZNs0gXhaRWxeIGd1scvbLCJHjxSArV704D7w6OBkgzN6C2-04m1JzOABw6Rkdv7W1f4aaWQvzMVMrCrjbOvn_fKaw2_nD3USakw=&lang=sage&interacts=eJyLjgUAARUAuQ==)

Podobnými iteračními metodami je možné efektivně řešit soustavy o
tisících rovnic a neznámých. Výpočty probíhají rychle a nejsou náročné
na paměť jako u přímých metod, známých například ze střední
školy. Tímto způsobem se řeší soustavy rovnic při modelování namáhání
konstrukcí, vedení tepla, proudění vody apod.

## Hodnost matice

https://youtu.be/HF-RDBZUenY

Iterační metoda funguje pro soustavy s jediným řešením. Pokud však hledáme vlastní vektory, musíme být schopni umět řešit i soustavy s nekonečně mnoha řešeními.

Matice řádu $m\times n$ obsahuje celkem $m\cdot n$ čísel. Jedná se tedy
o relativně komplikovaný objekt. V matematice se často snažíme
složitější objekty nějakým způsobem charakterizovat pomocí objektů
jednodušších, např. pomocí čísel. Jedno už známe, determinant. Dalším 
z těchto čísel je hodnost matice, kterou si nadefinujeme nyní.

```{prf:definition} Hodnost matice
:nonumber:

  Buď $A$ matice. *Hodností matice* rozumíme
  maximální počet lineárně nezávislých řádků matice.
  Hodnost matice $A$ označujeme ${h(A)}$.
```


Poznámka: Hodnost je v anglické literatuře označována jako *rank*.

Schodovitý tvar jsme si představili u determinantu. U matice ve
schodovitém tvaru je určení determinantu velmi jednoduché. Podobný
efekt vidíme i u hodnosti.

```{prf:definition} Schodovitý tvar
:nonumber:

  Řekneme, že matice $A$ je ve *schodovitém tvaru*, jestliže
  případné nulové řádky jsou uspořádány na konci matice a nenulové
  jsou uspořádány tak, že každý následující řádek začíná větším počtem
  nul než řádek předchozí.
```


```{prf:theorem} Hodnost matice ve schodovitém tvaru
:nonumber:

   Hodnost matice, která je ve schodovitém
  tvaru je rovna počtu jejích nenulových řádků.
```


**Příklad.**  Matice $A=   \begin{pmatrix}     2&2&2&3&-1&5\\     0&0&1&0&0&3\\     0&0&0&-1&2&1\\     0&0&0&0&0&0   \end{pmatrix}$ je ve schodovitém tvaru a $h(A)=3$. Matice   $B=  \begin{pmatrix}     2&2&2&3&-1&5\\      0&0&1&0&0&3\\      0&0&3&-1&2&1    \end{pmatrix}$ není ve  schodovitém tvaru a její  hodnost na první pohled nepoznáme.

## Výpočet hodnosti

Výpočet hodnosti se provádí postupným nahrazením zadané matice maticí, která má stejnou hodnost, ale postupně se přibližuje schodovitému tvaru. Uvedeme si jenom základní postup. Tento se sice dá vylepšit, pro nás je však důležité, že i bez jakýchkoliv vylepšení vždy vede k cíli. (Alespoň teoreticky.)

```{prf:theorem} Řádkové operace zachovávající hodnost matice
:nonumber:

Následující operace nemění hodnost matice:

1. vynechání řádku složeného ze samých nul, nebo vynechání řádku,
    který je totožný s jiným řádkem, nebo vynechání řádku, který je
    násobkem jiného řádku,
1. vynásobení nebo vydělení libovolného řádku nenulovým číslem,
1. záměna pořadí řádků,
1. ponechání jednoho řádku beze změny a opakované přičtení
    libovolných násobků tohoto řádku k nenulovým násobkům ostatních
    řádků matice.

Libovolnou matici lze konečným počtem těchto úprav převést do schodovitého tvaru.
```


Následující věta udává, že veškerá tvrzení, uvedená v souvislosti s
hodností pro řádky matice, se dají přeformulovat i pro sloupce matice.

```{prf:theorem} Hodnost transponované matice
:nonumber:
  Transponování nemění  hodnost matice.
```

## Existence a jednoznačnost řešení soustavy lineárních rovnic  

V případě, že matice soustavy je čtvercová již víme, že řešení je
určeno jednoznačně právě tehdy, když má matice soustavy matici
inverzní.  O počtu řešení v obecném případě obdélníkové matice, kdy
matici inverzní nemá smysl uvažovat, nám dávají informaci dvě
následující věty.  První se týká existence řešení a druhá identifikuje
případ, kdy řešení je určeno jednoznačně.

```{prf:theorem} Frobeniova věta, Kronecker-Capelliho věta
:nonumber:
 Soustava lineárních rovnic je řešitelná právě tehdy, když její matice soustavy a rozšířená matice soustavy mají stejnou hodnost.
```


```{prf:theorem} Jednoznačnost řešení
:nonumber:
 Nechť soustava lineárních rovnic má řešení. Toto řešení je právě jedno, pokud je společná hodnost matice soustavy a rozšířené matice soustavy rovna počtu neznámých. V opačném případě je společná hodnost matice a rozšířené matice soustavy menší než počet neznámých. 
```


## Gaussova eliminace

Spočívá v reprezentaci soustavy pomocí rozšířené matice soustavy a
převodu této matice na schodovitý tvar pomocí řádkových operací
zachovávajících hodnost. Tyto operace zachovávají i množinu řešení
soustavy. Jakmile je matice ve schodovitém tvaru, zpětnou substitucí
postupně dopočítáváme jednotlivé proměnné. (Formálně to u čtvercových
regulárních matic odpovídá použití inverzní matice k matici, která má
pod hlavní diagonálou nuly. Ale postup funguje i pro obecnější matice
a dá se realizovat jednoduchými prostředky a postupným dosazováním.)

Gaussova eliminace je velice flexibilní a univerzální, umožní nám
řešit i soustavy mající nekonečně mnoho řešení. V tomto případě
dokážeme zapsat řešení pomocí parametrů.

**Příklad.**

$$
\begin{aligned}
  x_1+2x_2+2x_3+x_4&=0\\
  x_1-x_2+x_3-2x_4&=1\\
  x_2-2x_3+x_4&=2
\end{aligned}
$$

Rozšířená matice soustavy je
$$\left(
  \begin{array}{cccc|c}
 1& 2& 2& 1& 0\\
 1& -1& 1& -2& 1\\
 0& 1& -2& 1& 2
  \end{array}\right)
  $$

  V prvním kroku převedeme na tvar, kdy jednom jeden řádek začíná nenulovým prvkem. První řádek už nijak neupravujeme a opíšeme jej. Místo druhého řádku napíšeme jeho součet s $(-1)$-násobkem prvního řádku. 
$$ \left( \begin{array}{cccc|c}
 1& 2& 2& 1& 0\\
 0& -3& -1& -3& 1\\
 0& 1& -2& 1& 2
    \end{array}\right)
    $$

V dalším kroku převedeme na tvar, kdy z řádků začínajících jednou nulou ponecháme jenom jeden a ostatní upravíme tak, aby začínaly alespoň dvěma nulami. K tomu je vhodné nejprve přehodit poslední dva řádky, abychom mohli použít k vytváření nul jedničku.
$$ \left( \begin{array}{cccc|c}
 1& 2& 2& 1& 0\\
 0& 1& -2& 1& 2\\
 0& -3& -1& -3& 1
    \end{array}\right)
    $$

Nyní provedeme potřebnou úpravu. První dva řádky opíšeme. Místo třetího řádku napíšeme jeho součet s trojnásobkem druhého řádku.
$$ \left( \begin{array}{cccc|c}
 1& 2& 2& 1& 0\\
 0& 1& -2& 1& 2\\
 0& 0& -7& 0& 7
    \end{array}\right)
    $$

Nyní přepíšme do tvaru soustavy rovnic

$$
\begin{aligned}
    x_1+2x_2+2x_3+x_4&=0\\
  x_2-2x_3+x_4&=2\\
-7x_3\phantom{+x_4}&=7
\end{aligned}
$$

Z poslední rovnice máme snadno $x_3=-1$. Tuto hodnotu použijeme ve
druhé rovnici. 
$$
\begin{aligned}
  x_2-2x_3+x_4&=2\\
  x_2+2+x_4&=2\\
  x_2+x_4&=0\\
\end{aligned}
$$
Protože však máme pořád dvě neznámé, jednu z nich
zvolíme za parametr. Nechť je například $x_4$ a nechť je parametr označen jako $t$.
$$
  x_4=t
$$
Rovnice má poté tvar
$$
  x_2+t=0.
$$
Odsud již snadno dostáváme
$$
  x_2=-t.
$$
Vypočtené hodnoty dosadíme do první rovnice a určíme zbývající
neznámou $x_1$.
$$
\begin{aligned}
  x_1+2x_2+2x_3+x_4&=0\\
  x_1-2t-2+t&=0\\
  x_1&=2+t
\end{aligned}
$$
Řešení je $x_1=2+t$, $x_2=-t$, $x_3=-1$, $x_4=t$, kde $t$ je libovolné reálné číslo. Vektorově (maticově) máme řešení ve tvaru
$$\begin{pmatrix}  x_1\\x_2\\x_3\\x_4\end{pmatrix} = \begin{pmatrix}  2+t\\-t\\-1\\t\end{pmatrix}=\begin{pmatrix}  2\\0\\-1\\0\end{pmatrix}+t\begin{pmatrix}  1\\-1\\0\\1\end{pmatrix}.$$

## Gaussova-Seidelova iterační metoda

https://youtu.be/KBg1tllDhxM

Gaussova-Seidelova iterační metoda je jakýsi mezikrok mezi Jacobiho
iterační metodou a Gausovou eliminací. Postupujeme jako v Jacobiho
metodě, ale všechny zpřesněné hodnoty použijeme okamžitě, když jsou k
dispozici. Nikoliv až v další iteraci jako u Jacobiho metody. Metoda
konverguje za stejných podmínek jako Jacobiho metoda, ale rychleji a
přesto nevznikají vyšší nároky na výpočetní výkon.

Použijeme příklad z [Wikipedie](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#An_example_for_the_equation_version).
Soustavu $$\begin{array}{rrrrl}
10x_1 &-   x_2 &+  2x_3 &       & = 6, \\
 -x_1 &+ 11x_2 &-   x_3 &+ 3x_4 & =  25, \\
 2x_1 &-   x_2 &+ 10x_3 &-  x_4 & =  -11, \\
      &   3x_2 &-   x_3 &+ 8x_4 & =  15.
\end{array}$$
s diagonálně dominantní maticí převedeme na iterační tvar
$$
\begin{aligned}
  x_1 & = x_2/10 - x_3/5 + 3/5, \\           
x_2 & = x_1/11 + x_3/11 - 3x_4/11 + 25/11, \\
x_3 & = -x_1/5  + x_2/10 + x_4/10  - 11/10, \\
x_4 & = -3x_2/8  + x_3/8 + 15/8.
\end{aligned}
$$
Poté vyjdeme z počátečního odhadu řešení a dosazujeme do pravých
stran.

U Jacobiho metody pro počáteční odhad vypočteme nejprve všechny
pravé strany a dosadíme do proměnných na levé straně jako zpřesnění
počáteční aproximace. Tento postup opakujeme.

U Gaussovy-Seidlovy metody nejprve pomocí počátečního odhadu vypočteme
z první rovnice $x_1$ a tuto hodnotu ihned použijeme při výpočtu $x_2$
z další rovnice. Obojí, $x_1$ i $x_2$ už využijeme při výpočtu $x_3$ a
tak dále. Po výpočtu $x_4$ je první iterace dokončena a postup opět
opakujeme, dokud dvě po sobě jdoucí iterace nejsou dostatečně blízké.

S nulovou počáteční aproximací dostáváme v prvním průchodu
$$
\begin{aligned}
x_1 & = 3/5 = 0.6, \\
x_2 & = 0.6/11 + 25/11 = 2.3272, \\
x_3 & = -0.6/5 +(2.3272)/10-11/10 = -0.9873,\\ 
x_4 & = -3(2.3272)/8 +(-0.9873)/8+15/8 = 0.8789.
\end{aligned}
$$
Jak vidno, vypočtenou hodnotu $x_1$ ihned použijeme pro výpočet $x_2$. Obě tyto hodnoty ihned použijeme pro výpočet $x_3$ a tak dále. V dalších iteracích postup [opakujeme](https://sagecell.sagemath.org/?z=eJytUMGKwjAQvRf6D0NPraakk6RShJ4X9rpXL3WtEpAorcLk73eyCYt4UJFNIC8z782DeefJuguUxefwfdrajevjKao8IxSkBGlBpm_E782z_WkCC9bBNLjDWGJTrfMM-HiEHkhJbKAG0rKFJYQXEq0CjRKR-0wz1qAXZGJHtYxJqVlZs5Rnl8mR0QTkGcTwSVITpOyiZAfRt2PAVnZRcLuCR-GV8Fp4E8lzXN0KV7IOdvZgL3O_qkKt7mp9V5ubmqNKVsXGfQzXea6_Rrsbj39pvhkpPY6UXo6UXo-UnkX6b6n9AO8SliU=&lang=sage&interacts=eJyLjgUAARUAuQ==). Mimo jiné hodnoty v paměti přímo přepisujeme a nemusíme držet v paměti starou a novou hodnotu. 

## Shrnutí, hlavní myšlenky

https://youtu.be/aeUs2y2QrRw

\iffalse

<div class='obtekat'>

```{figure} ../message.jpg
A jaká je hlavní message? Zdroj: pixabay.com
```

</div>

\fi

* Řada numerických metod pro řešení modelů založených na matematickém modelování fyzikálních zákonů se v nějaké fázi redukuje na řešení soustav lineárních rovnic. Kromě toho se se soustavami lineárních rovnic setkáváme při hledání vlastních směrů matic, což je důlležité pro matice reprezentující materiálové charakteristiky. 
* Ukázali jsme si tři různé formulace soustav lineárních rovnic, klasickou pomocí rovnic, vektorovou pomocí jedné vektorové rovnice a maticovou pomocí jediné maticové rovnice a jediné maticové operace, maticového součinu. 
* Ukázali jsme si, že v případě známé inverze k matici soustavy se řešení redukuje na součin inverzní matice s maticí pravých stran.
* Kromě možnosti využít inverzní matici jsme si ukázali další tři metody řešení. Dvě čistě numerické metody (Jacobiho a Gaussova-Seidelova metoda) a jednou univerzální (Gaussova eliminační metoda).
