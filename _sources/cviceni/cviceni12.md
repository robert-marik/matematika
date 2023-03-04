# Dvojný integrál

## Kvadratický moment pro obdélník

Vypočtěte integrál
$$
\begin{aligned}
 \iint_\Omega y^2\,\mathrm dx \mathrm dy,\\
\end{aligned}
$$
přes obdélník se stranami podél os, se středem v počátku a délkou stran $a$ a $b$, tj. přes množinu $\Omega$ danou nerovnostmi
$$
\begin{aligned}
  -\frac a2\leq &x\leq \frac a2,\\
  -\frac b2\leq &y \leq \frac b2.
\end{aligned}
$$

```{prf:example} Řešení
:class: dropdown
:nonumber:

$$
\begin{aligned}
  \iint_\Omega y^2\,\mathrm dx \mathrm dy
  = \int_{-\frac a2}^{\frac a2} \,\mathrm dx \times \int_{-\frac b2}^{\frac b2}y^2\,\mathrm dy=a\times \left[\frac 13 y^3\right]_{-\frac b2}^{\frac b2}=a\times \left(\frac 13 \times \frac {b^3}{8} + \frac 13 \times \frac {b^3}{8}\right)=   \frac 1{12}ab^3
\end{aligned}
$$

```

## Těžiště trojúhelníku

<!-- 
\Tobrazek{\begin{tikzpicture}[scale=3]
  \draw[black,fill=green, domain=0:1] (0,0) -- (0,1) -- plot ({\x},{1-\x})--cycle;
%  \draw[black,domain=0:1.2] plot ({\x},{1-\x}) node[right]{$y=1-x$};
  \draw[->] (0,0)--(1.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,1.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (1.5,1.5);
    \draw[thin, dashed, gray] (0,0) grid (4,3);
  \end{scope}
\end{tikzpicture}
}
-->

Vypočtěte integrál
$$  \iint_\Omega x\,\mathrm dx \mathrm dy
$$
přes trojúhelník $\Omega$ s vrcholy v bodech $(0,0)$, $(1,0)$ a $(0,1)$ a poté vydělením obsahem trojúhleníka najděte $x$-ovou polohu těžiště.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Rovnice přímky, ve které leží přepona trojúhelníka, je
$$y=1-x$$ a trojúhelník tedy je možno zapsat soustavou nerovností

$$
\begin{aligned}
  0\leq &x\leq 1,\\
  0\leq &y \leq 1-x.
\end{aligned}
$$

Použitím těchto nerovností můžeme dvojný integrál transformovat na dvojnásobný a vypočítat.
$$
\begin{aligned}
  \iint_\Omega x\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{1-x} x\,\mathrm dy\mathrm dx
  =\int_0^1 \left[xy\right]_0^{1-x}\,\mathrm dx
  =\int_0^1 x(1-x)\,\mathrm dx
  \\&=\int_0^1 x-x^2\,\mathrm dx
  =\left[\frac 12 x^2 - \frac 13 x^3\right]_0^1
  \\&=\frac 12 -\frac 13 =\frac 1{6}
\end{aligned}
$$

$$x_T=\frac{\frac 16}{\frac 12}=\frac 13$$

```

## Velikost tlakové síly na hráz přehrady

Viz video ke cvičení a text k přednášce.

## Působiště tlakové síly na hráz přehrady

Viz video ke cvičení a text k přednášce.


