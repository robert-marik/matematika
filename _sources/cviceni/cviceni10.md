<style>
	.example p img {float:none; max-width:100%;}
</style>


# Vlastní čísla a směry

> * Vlastní čísla umí numericky najít počítače, WolframAlpha, Python, Matlab, ... 
> * Pro Python ukázku výpočtu [vygeneruje ChatGPT](https://chat.openai.com/share/7cabf98a-1c64-418a-b61b-f1eba78c4ff1)
> * Některé výpočty jsou v [zápisníku pro Python](https://gist.github.com/robert-marik/87a5c146c98a8dc0840633e96a417214).

## Vektor, který není vlastním směrem

Ukažte, že vektor $\vec a=  \begin{pmatrix}    1\\2  \end{pmatrix}$
není vlastním směrem matice $$A=\begin{pmatrix}  3& 0 \\ 2 &4\end{pmatrix}.$$

```{prf:example} Řešení
:class: dropdown
:nonumber:

Pomocí maticového násobení vidíme, že platí
$$ A\vec a=\begin{pmatrix}  3& 0 \\ 2 &4\end{pmatrix}\begin{pmatrix}  1\\2\end{pmatrix}=\begin{pmatrix}  3\\2\end{pmatrix}+2\begin{pmatrix}  0\\4\end{pmatrix}=\begin{pmatrix}  3\\10\end{pmatrix}.$$

Výsledkem zobrazení vektoru pomocí matice je vektor který není násobkem původního vektoru (podle první komponenty by se muselo jednat o trojnásobek, ale to nekoresponduje s druhou komponentou) a proto se nejedná o vlastní vektor matice.

```

## Vektor, který je vlastním směrem

Ukažte, že vektor $\vec a=  \begin{pmatrix}    2\\3  \end{pmatrix}$  je vlastním směrem matice $$A=\begin{pmatrix}  6& 0 \\ 3 &4\end{pmatrix}$$  a určete příslušné vlastní číslo

```{prf:example} Řešení
:class: dropdown
:nonumber:

Pomocí maticového násobení vidíme, že platí
$$A\vec a=\begin{pmatrix}  6& 0 \\ 3 &4\end{pmatrix}\begin{pmatrix}  2\\3\end{pmatrix}=2\begin{pmatrix}  6\\3\end{pmatrix}+3\begin{pmatrix}  0\\4\end{pmatrix}=\begin{pmatrix}  12\\18\end{pmatrix}.$$

Výsledkem zobrazení vektoru $\vec a$ pomocí matice je vektor $\begin{pmatrix}  12\\18\end{pmatrix},$ který je šestinásobkem původního vektoru $\begin{pmatrix}  2\\3\end{pmatrix}$.
Protože je obraz násobkem vzoru, jedná se o vlastní vektor matice. Příslušné vlastní číslo je $6$, protože se vektor zobrazuje na svůj šestinásobek.

```

## Vlastní čísla a vektory matice $2\times 2$

Najděte vlastní čísla matice $$A=\begin{pmatrix}  -2 & 2 \\ 2 &1\end{pmatrix}$$
a jim příslušné vlastní vektory.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Vlastní čísla jsou nulovými body determinantu
$$\begin{vmatrix}  -2-\lambda &2 \\ 2 & 1-\lambda\end{vmatrix}=(-2-\lambda)(1-\lambda)-(2)(2)=\lambda^2+\lambda-6=(\lambda-2)(\lambda+3).$$

**Vlastní číslo $\lambda_1=2$.**
Protože platí $$A-2 I=\begin{pmatrix}  -2 & 2\\2&1\end{pmatrix}-\begin{pmatrix}  2&0\\0&2\end{pmatrix}=\begin{pmatrix}  -4 & 2\\ 2 &-1\end{pmatrix},$$
řešíme soustavu 
$$\begin{pmatrix}-4 & 2\\ 2 &-1\end{pmatrix}\begin{pmatrix}  x_1\\x_2\end{pmatrix}=\begin{pmatrix}  0\\0\end{pmatrix},$$
která má nekonečně mnoho řešení. Musíme najít alespoň jendo nenulové řešení. Pokud zapíšeme jako soustavu rovnic, dostáváme druhou rovnici ve tvaru
$$2x_1-x_2=0$$ a první rovnice je jejím násobkem. Volbou $x_1=1$ dostáváme $x_2=2x_1=2$ a vlastní vektor příslušný vlastnímu číslu $\lambda_1=2$ je $\vec e_1= \begin{pmatrix}
  1\\2
\end{pmatrix}.$ Tento vektor je dán jednoznačně až na nenulový konstantní násobek.

**Vlastní číslo $\lambda_2=-3$.**
Protože platí $$A-(-3) I=\begin{pmatrix}  -2 & 2\\2&1\end{pmatrix}+\begin{pmatrix}  3&0\\0&3\end{pmatrix}=\begin{pmatrix}  1 & 2\\ 2 &4\end{pmatrix},$$řešíme soustavu $$\begin{pmatrix}1 & 2\\ 2 &4\end{pmatrix}\begin{pmatrix}  x_1\\x_2\end{pmatrix}=\begin{pmatrix}  0\\0\end{pmatrix},$$
která má nekonečně mnoho řešení. Musíme najít alespoň jendo nenulové řešení. Pokud zapíšeme jako soustavu rovnic, dostáváme první rovnici ve tvaru
$$x_1+2x_2=0$$ a druhá rovnice je jejím násobkem. Volbou $x_2=1$ dostáváme $x_1=-2x_2=-2$ a vlastní vektor příslušný vlastnímu číslu $\lambda_2=-3$ je $\vec e_2=\begin{pmatrix}   -2\\1\end{pmatrix}.$ Tento vektor je dán jednoznačně až na nenulový konstantní násobek.

**Poznámka.** Protože je matice symetrická, jsou vlastní vektory na sebe kolmé. Proto není nutné druhý vektor počítat, ale stačí vzít libovolný vektor kolmý k prvnímu vlastnímu vektoru. V praxi tedy stačí vektoru $\vec e_1$ prohodit komponenty a na první nebo druhé pozici změnit znaménko. Tím dostaneme vektor $\vec e_2$.

```

## Transformace matice $2\times 2$ na diagonální tvar

Uvažujme symetrickou matici
$$ A=  \begin{pmatrix}  3 & 1\\  1 & 3\end{pmatrix}.$$

1. Určete vlastní čísla a jednotkové vlastní vektory této matice.
1. Sestavte matici $P$ tak, aby ve sloupcích obsahovala jednotkové vlastní vektory.
Pokud je to možné, napište matici $P$ tak, aby její determinant byl kladný.
1. Ověřte, že  $P^TAP=D$  je diagonální matice.

_Návod: Vlastní vektory příslušné různým vlastním číslům jsou na sebe kolmé._

```{prf:example} Řešení
:class: dropdown
:nonumber:

Charakteristický polynom je
$$  \begin{vmatrix}    3-\lambda & 1\\1 & 3-\lambda  \end{vmatrix}  =(3-\lambda)^2-1=9-6\lambda+\lambda^2-1=\lambda^2-6\lambda+8=(\lambda-4)(\lambda-2)$$
a vlastní čísla jsou $\lambda_1=2$ a $\lambda_2=4$.
Protože platí
$$A-\lambda_1 I  =  \begin{pmatrix}    3-2 & 1 \\    1 &3-2  \end{pmatrix}  =    \begin{pmatrix}    1 & 1 \\    1 &1  \end{pmatrix},$$
je vlastní vektor příslušný vlastní hodnotě $\lambda_1$ řešením soustavy
$$\begin{pmatrix}    1 & 1 \\ 1 &1  \end{pmatrix}\begin{pmatrix}  x_1\\x_2\end{pmatrix}=  \begin{pmatrix}    0\\0  \end{pmatrix}$$
To je vlastně dvakrát zopakovaná rovnice
$$  x_1+x_2=0,$$
která má řešení například $x_1=1$ a $x_2=-1$. Protože délka vektoru $(1,-1)$ je $\sqrt{1^2+(-1)^2}=\sqrt 2$, jednotkový vlastní vektor je $e_1=\left(\frac 1{\sqrt 2}, -\frac 1 {\sqrt 2}\right)^T$. Podobně by se dal najít jednotkový vlastní vektor příslušný druhé vlastní hodnotě, ale protože oba vektory musí být na sebe kolmé, stačí vzít jednotkový vektor, který je k $e_1$ kolmý, například
$e_2=\left(\frac 1{\sqrt 2}, \frac 1 {\sqrt 2}\right)^T$. Matici $P$ můžeme vzít
s $e_1$ v prvním a $e_2$ druhém sloupci, tj.
$$    P=  \begin{pmatrix}      \frac 1{\sqrt 2} & \frac 1{\sqrt 2}\\      -\frac {1}{\sqrt 2} & \frac 1{\sqrt 2}    \end{pmatrix}.  $$
  Rychlý výpočet ukazuje, že matice $P$ má determinant roven jedné. Kdyby vyšel roven minus jedné, stačí prohodit sloupce nebo jeden sloupec vynásobit faktorem $-1$.

Pokud ještě před násobením matic vytkneme opakující se faktor z obou matic, násobením dostáváme
$$  \begin{aligned}  P^TAP&=\begin{pmatrix}      \frac 1{\sqrt 2} & -\frac 1{\sqrt 2}\\      \frac {1}{\sqrt 2} & \frac 1{\sqrt 2}    \end{pmatrix}        \begin{pmatrix}    3 & 1 \\ 1 &3  \end{pmatrix}  \begin{pmatrix}      \frac 1{\sqrt 2} & \frac 1{\sqrt 2}\\      -\frac {1}{\sqrt 2} & \frac 1{\sqrt 2}    \end{pmatrix}\\&    =\frac 1{\sqrt 2}\frac 1{\sqrt 2}    \begin{pmatrix}      1 & -1 \\ 1 &1    \end{pmatrix}        \begin{pmatrix}    3 & 1 \\ 1 &3  \end{pmatrix}    \begin{pmatrix}      1 & 1 \\ -1 &1    \end{pmatrix}    \\&=    \frac 1{2}    \begin{pmatrix}      1 & -1 \\ 1 &1    \end{pmatrix}    \begin{pmatrix}      2 & 4 \\-2 & 4    \end{pmatrix}    \\&=    \frac 1{ 2}    \begin{pmatrix}      4& 0 \\ 0& 8    \end{pmatrix}=    \begin{pmatrix}      2& 0 \\0& 4    \end{pmatrix}.  \end{aligned}$$
Podle očekávání vyšla diagonální matice s vlastními hodnotami v hlavní diagonále.

```

## Poměr délky vzoru a obrazu vektoru

Pro matici $$A= \begin{pmatrix}   3&1\\1&3 \end{pmatrix}$$ z minulého příkladu a vektor $$\vec u=\begin{pmatrix}  -1\\2\end{pmatrix}$$
určete podíl délky obrazu $A\vec u$ a vzoru $\vec u$ při zobrazení pomocí matice $A$. Ověřte, že tento podíl leží mezi menší a větší vlastní hodnotou, které jsme vypočítali v předchozím příkladě.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Platí
$$A\vec u=\begin{pmatrix}  3&1\\1&3\end{pmatrix}\begin{pmatrix}  -1\\2\end{pmatrix}=-\begin{pmatrix}  3\\1\end{pmatrix}+2\begin{pmatrix}  1\\3\end{pmatrix}=\begin{pmatrix}  -1\\5\end{pmatrix}$$
a výpočetem délek vektorů
dostáváme
$$||\vec u||=\sqrt{(-1)^2+(2)^2}=\sqrt 5$$
a 
$$||A\vec u||=\sqrt{(-1)^2+(5)^2}=\sqrt {26}.$$
Podíl délek je
$$\frac{||A\vec u||}{||\vec u||}=\frac{\sqrt {26}}{\sqrt 5}\approx 2.28$$
což je podle očekávání hodnota mezi menší a větší vlastní hodnotou, které vyšly v předchozím příkladě.

```

<!--
% 

% # Komentář k předchozímu Zobrazení popsané maticí $A$
% je naznačeno na obrázku a jak vidno, mění tvar modrého jednotkového čtverce.

% \hbox to \hsize{\begin{minipage}[t]{0.35\linewidth}\vspace*{0pt}
% \begin{tikzpicture}[scale=1]
%   \draw[-latex](0,0)--(3,0);
%   \draw[-latex](0,0)--(0,1.5);

%   \fill[blue, opacity=0.5] (0,0) rectangle (1,1);
%   \fill[red, opacity=0.5] (0,0) -- (3,-1) -- (2,0) -- (-1,1) -- cycle;
%   \draw[ultra thick,blue,-latex] (0,0)--(1,1) node[right] {$u$};
%   \draw[ultra thick,red,-latex] (0,0)--(2,0) node[above right] {$u'$};

%   \draw[ultra thick,blue,-latex] (0,0)--(0,1) node[right] {$v$};
%   \draw[ultra thick,red,-latex] (0,0)--(-1,1) node[above right] {$v'$};
%   \draw (-0.5,1.7) node [right, gray] {\footnotesize Vzor je modře, obraz červeně.};
% \end{tikzpicture}

% Vektor $u$ se při zobrazení otočí po směru a $v$ proti směru
% hodinových ručiček. Někde mezi nimi bude vektor, který při zobrazení
% směr nemění. To bude vlastní vektor a z obrázku je možné odhadnout, že
% bude příslušný menší vlastní hodnotě.
% \end{minipage}\hfil\vrule\hfil
% \begin{minipage}[t]{0.62\linewidth}\vspace*{-10pt}
%   \begin{tikzpicture}[scale=1]
%       \draw (1.2,1.2) node [right,gray, text width=4cm] {\footnotesize Vzor je vybarven, obraz je znázorněn jenom obrysem, barvy obrazu a vzoru si odpovídají.};
%   \draw[-latex](0,0)--(3,0);
%   \draw[-latex](0,0)--(0,1.5);

%   \fill[blue, opacity=0.5] (0,0) rectangle (1,1);
%   \draw[ultra thick, blue] (0,0) -- (3,-1) -- (2,0) -- (-1,1) -- cycle;

%   \fill[green, opacity=0.5] (0,0)--(0.382683432365090,0.923879532511287)--
%   (-0.541196100146197, 1.30656296487638) --
%   (-0.923879532511287,0.382683432365090)--cycle;

%   \draw[ultra thick, green]  (0,0)--(0.224170764583983, 0.541196100146197)--(-2.93015126531497, 1.84775906502258)-- (-3.15432202989895, 1.30656296487638) -- cycle;
% \end{tikzpicture}

% Zobrazení symetrickou maticí $A$ uvažovanou v tomto příkladě si můžeme představit tak, že máme elastickou pásku, která se působením síly deformuje tak, že se natahuje v jednom směru a zužuje v příčném směru. Čtverec nakreslený na pásce tak, že jeho strany leží v těchto směrech (zelený) se deformuje na obdélník. Obecný čtverec (modrý) se deformuje tak, že se mění úhly. Na přednášce jsme si naznačili, jak se ukáže, že deformace v těchto směrech je extremální, vrátíme se k tomu v záverečném shrnutí na konci semestru, protože jde o kombinaci úlohy z lineární algebry a diferenciálního počtu.

% \end{minipage}}

% 
% ## Neceločíslená vlastní čísla a vektory matice $2\times 2$

-->

## Transformace tenzoru pootočením

Uvažujme tyč ve směru osy $x$ namáhanou v ose tahem, při kterém vzniká jednotkové tahové napětí. Tyč je slepena spojem, který svírá s kolmicí na osu úhel $\theta$. (Nakreslete si obrázek.) Normálovým napětím rozumíme napětí ve směru kolmém na spoj.

1. Ukažte, že pro nenulový úhel $\theta$ je normálové napětí ve
  spoji menší, než by odpovídalo normálovém napětí pro spoj kolmý na osu tyče.
1. Ukažte, že normálové napětí je klesající funkcí úhlu $\theta$ na intervalu od nuly do $\frac \pi2$.
1. Určete normálové a smykové napětí pro extrémní případ $\theta=\frac \pi 2$ a popište, jak by takový spoj vypadal.
1. Určete smykové napětí ve spoji a určte, pro jakou hodnotu úhlu je smykové napětí největší.
1. Určete, jestli je v tomto případě z hlediska působícího napětí výhodnější udělat šikmý spoj po směru nebo proti směru hodinových ručiček.  

```{prf:example} Řešení
:class: dropdown
:nonumber:

V souřadné soustavě podle zadání je tah ve směru osy $x$ roven jedné a další komponenty jsou nulové. Tedy $\sigma=\begin{pmatrix}  1 & 0 \\ 0& 0\end{pmatrix}.$ Budeme otáčet proti směru hodinových ručiček, tj. o kladný úhel $\theta$.

Dostáváme (při zkráceném označení $S=\sin\theta$ a $C=\cos\theta$)
$$\begin{aligned} R^{-1}\sigma R &=  \begin{pmatrix}    C & S\\ -S&C  \end{pmatrix}\begin{pmatrix}  1 & 0 \\ 0& 0\end{pmatrix}.  \begin{pmatrix}    C & -S\\ S&C  \end{pmatrix}  \\&=  \begin{pmatrix}    C & S\\ -S&C  \end{pmatrix}\begin{pmatrix}  C & -S \\ 0& 0\end{pmatrix}=\begin{pmatrix}  C^2 & -CS \\ -CS& S^2\end{pmatrix}\end{aligned}$$
a normálová a smyková složka napětí jsou po řadě $\cos^2\theta$ a $-\sin\theta \cos\theta = -\frac 12 \sin(2\theta).$

Odsud již dostaneme odpovědi na všechny uvedené otázky.

1. Normálové napětí udává funkce $$\cos^2\theta.$$ Ta je rovna jedné pro $\theta=0$, tj. pro nulový sklon spoje. Pro nenulový sklon je menší než jedna (uvažujeme sklon maximálně do 90 stupňů).
1. Derivace normálového napětí pro $\theta$ z intervalu od $0$ do $\frac \pi2$ je $$\frac{\mathrm d}{\mathrm d\theta}\cos^2{\theta}=2\cos\theta (-\sin\theta)=-\sin(2\theta)<0.$$ Záporná derivace značí klesající funkci. 
1. Pro $\theta=\frac \pi 2$ by normálové napětí bylo nulové a smykové také nulové. Jednalo by se vlastně o podélně spojené kusy materiálu a při uvedeném namáhání by bylo jedno, jestli jsou slepené nebo ne. 
1. Smykové namáhání je prvek v matici mimo hlavní diagonálu. V našem případě $-\frac 12 \sin(2\theta)$. Smykové namáhání je maximální, pokud má tato funkce maximum nebo minimum. Takový extrém je pro $2\theta=\frac \pi 2$ tj. pro $\theta = \frac\pi4.$ Maximální smykové namáhání je pro spoj skloněný pod úhlem 45 stupňů.
1. Nezáleží. Změnou znaménka u úhlu $\theta$ se napětí ve směru kolmo na spoj ani podél spoje nemění, funkce $\cos^2\theta$ i $\sin^2\theta$ jsou obě sudé. U smykového napětí se mění znaménko, ale to jenom znamená namáhání v opačném smyslu (Pokud si na stěnu materiálu nakreslíme čtvereček s jednou stranou podél spoje a s druhou stranou kolmo na spoj, podle směru sklonu spoje máme dva zrcadlové případy, jak se tento čtvereček deformuje. Tomu odpovídá opačné znaménko smykové derivace.)

\iffalse

Snadno je odpověď patrná i z obrázku, kde jsou vyneseny funkce z jednotlivých komponent transformovaného tenzoru. 

![](namahani.png)

[Kód pro vygenerování obrázku](https://sagecell.sagemath.org/?z=eJyFUD1ugzAU3pG4wxMTRA6NsnOLTo0ymOCCW2NbfobCIXoIxgy9QKVO7sFqh1KBMtSL38_3Z_NWK2NBdq0egSJIHUd8nrXUaqGs4GWux1CFvRY2juLINsxSKDw8F1yipheW7n2j-cORLPfxcMjiqKILkhpDx_TkK-QyvUlku90Nf1G4Guy3kM3-nOWPIcEzrwnQwSv7SDl2ZUiIqTcMfWhmAtkYb33ukvxnTCCO4PcIWjJRnBKpTOsmoXr3BZY20IM2vXQfoJAlBO73DCrTNe66ALAdX_32CpJ6YOMmT07O_iF0yJHZdJidEvfZMAFaKau-31kAEbDcClYkT27qOQqFdi3ia_Ak0a1JgFq9sGSWrw2vli8TrGbyr8NGvaXZD-3IwKg=&lang=python&interacts=eJyLjgUAARUAuQ==)

\fi

```

<!-- 
% ## Extrémy diagonálních prvků transformovaného tenzoru
-->

## Vlastní čísla a vektory matice $3\times 3$.

V cvičení z minulého týdne jsme ukázali, že nejobecnější symetrická matice zachovávající směr vektoru  $(1,0,0)^T$ má v prvním řádku a prvním sloupci jenom jeden nenulový prvek, prvek v hlavní diagonále.

Uvažujme matici
$$A=  \begin{pmatrix}  5 & 0 & 0\\  0 & 2 & 2\\  0 & 2 & 5\end{pmatrix},$$
která je tohoto typu.
Určete vlastní čísla a zbylé vlastní vektory matice.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Podle zadání víme, že jeden z vlastních vektorů je $e_1=(1,0,0)^T$ a protože se zobrazí na pětinásobek, je příslušná vlastní hodnota $\lambda_1=5$. Charakteristický polynom je
$$  \begin{aligned}  \begin{vmatrix}  5-\lambda & 0 & 0\\  0 & 2-\lambda & 2\\  0 & 2 & 5-\lambda\end{vmatrix}&=(5-\lambda)(2-\lambda)(5-\lambda)-(5-\lambda)\times 2\times 2\\& =(5-\lambda)\Bigl[(2-\lambda)(5-\lambda) -4\Bigr]\\&=(5-\lambda)(\lambda^2 -7\lambda +6)=(5-\lambda)(\lambda-1)(\lambda-6)\end{aligned}$$
Další dvě vlastní hodnoty jsou $\lambda_2=1$ a $\lambda_3=6$

Uvažujme matici
$$  A-1 I=  \begin{pmatrix}    4 & 0 & 0\\    0 & 1 & 2\\    0 & 2& 4  \end{pmatrix}.$$
Soustava
$$  \begin{pmatrix}    4 & 0 & 0\\    0 & 1 & 2\\    0 & 2& 4  \end{pmatrix}  \begin{pmatrix}    x_1\\x_2\\x_3  \end{pmatrix}  =  \begin{pmatrix}    0 \\0\\0  \end{pmatrix}$$
má řešení $x_1=0$ (plyne z první rovnice) a například $x_2=2$ a $x_3=-1$ (plyne z druhé a třetí rovnice, které jsou jedna násobkem druhé). Vlastní vektor příslušný vlastní hodnotě $\lambda_2=1$ je $e_2=(0,2,-1)^T$.

Uvažujme matici
$$  A-6 I=  \begin{pmatrix}    -1 & 0 & 0\\    0 & -4 & 2\\    0 & 2& -1  \end{pmatrix}.$$
Soustava
$$  \begin{pmatrix}    -1 & 0 & 0\\    0 & -4 & 2\\    0 & 2& -1  \end{pmatrix}  \begin{pmatrix}    x_1\\x_2\\x_3  \end{pmatrix}  =  \begin{pmatrix}    0 \\0\\0  \end{pmatrix}$$
má řešení $x_1=0$ (plyne z první rovnice) a například $x_2=1$ a $x_3=2$ (plyne z druhé a třetí rovnice, které jsou jedna násobkem druhé). Vlastní vektor příslušný vlastní hodnotě $\lambda_3=6$ je $e_3=(0,1,2)^T$.

```


