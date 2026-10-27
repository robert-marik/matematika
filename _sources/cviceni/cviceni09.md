# Determinanty, soustavy rovnic

## Určete následující determinanty

1. $D_1=  \begin{vmatrix}    2 & -1 \\ 4 &3  \end{vmatrix}$
1. $D_2=  \begin{vmatrix}    2 & -1 \\ x-4 &y-3  \end{vmatrix}$
  ($D_2=0$ je přímka daná bodem $(4,3)$ a směrovým vektorem $(2,-1)$)
1. $D_3=  \begin{vmatrix}    2-\lambda & -1 \\ 4 & 3-\lambda  \end{vmatrix}$ (charakteristický polynom matice z prvního bodu)
1. $D_4=  \begin{vmatrix}    1 & -1 & 0\\ 2 & 3 & 1 \\ -1 &-1 & 2\end{vmatrix}$
1. $D_5=  \begin{vmatrix}    a & -1 & 0\\ 2 & 3 & 1 \\ -1 &-1 & 2\end{vmatrix}$  
1.  $D_6=  \begin{vmatrix}    2-\lambda & 0 & 0\\ 0 & 3-\lambda & 0 \\ 0 & 0& 7-\lambda \end{vmatrix}$  (charakteristický polynom diagonální matice)

```{prf:example} Řešení
:class: dropdown
:nonumber:

$$
  \begin{aligned}
    D_1&=2\cdot 3 - (-1)\cdot 4=6+4=10\\
    D_2&=2\cdot(y-3)-(-1)\cdot (x-4)=2y-6+x-4=x+2y-10\\
    D_3&=(2-\lambda)\cdot(3-\lambda)-(-1)\cdot 4 = \lambda^2-5\lambda+10\\
    D_4&=12\\
    D_5&=7a+5\\
    D_6&=(2-\lambda)(3-\lambda)(7-\lambda)
\end{aligned}
$$

```

## Soustava lineárních rovnic s jediným řešením

Vyřešte soustavu rovnic.

$$
  \begin{pmatrix}
1 &2 &2 \\
2 &2 &-1\\
2 &3 &1 \\
\end{pmatrix}
\begin{pmatrix}
  x_1\\x_2\\x_3
\end{pmatrix} =  \begin{pmatrix}
  3\\1\\-1
\end{pmatrix}
$$

Soustava rovnic je asi nejdůležitější aplikace lineární algebry, ale v dnešním světě není důvod ji řešit ručně. Je však užitečné si alespoň základní manipulace vyzkoušet na jednoduchém příkladě. Tento moc času nezabere.

## Soustava lineárních rovnic s nekonečně mnoha řešeními

Vyřešte soustavu rovnic.

$$
  \begin{pmatrix}
3 &-1 &-1 &-1\\ 
2 &1 &1 &-2 \\
1 &-2 &-2 &1 \\
3 &-1 &-1 &1 \\
\end{pmatrix}
\begin{pmatrix}
  x_1 \\ x_2 \\x_3\\x_4
\end{pmatrix} =  \begin{pmatrix}
  0 \\ 0 \\0\\0
\end{pmatrix}
$$

_Soustava s nekonečně mnoha řešeními typicky vychází při
  hledání vlastních čísel matice. Na tomto příkladě si osaháme případ
  homogenní soustavy a jednoparametrického řešení, tj. případ, který
  při výpočtu vlastních vektorů vychází nejčastěji._

<!--
% ## Soustava lineárních rovnic s parametrem
% Pro jakou hodnotu parametru má soustava nekonečně mnoho řešení?

% 

% 
% # Hlavní cvičení
% Cvičení ve středu ani ve čtvrtek se nekoná kvůli hlavnímu cvičení. Přednáška je beze změny.

-->


