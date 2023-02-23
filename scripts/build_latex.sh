# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/pdf

sphinx-build ../ $directory -b latex

cp prednasky_definice.tex $directory/
cp cviceni_definice.tex $directory/
cp custom_preamble.tex $directory/

cd $directory

sed -i 's/sphinxShadowBox/comment/' python.tex
sed -i 's/sphinxtheindex/comment/' python.tex
sed -i 's/documentclass\[/documentclass[twocolumn,/' python.tex

sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}iffalse/\\iffalse/g' python.tex
sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}fi/\\fi/g' python.tex

sed -z -i 's/\\sphinxAtStartPar\nhttps:\/\/youtu.be/%%% /g' python.tex

sed -z -i s'/\\sphinxAtStartPar\n\\sphinxcode{\\sphinxupquote{ww2:/%/g' python.tex
sed -z -i s'/\\sphinxAtStartPar\nmanim[^\n]*\n//g' python.tex
sed -z -i s'/\\sphinxAtStartPar\n\\egroup/\\egroup/g' python.tex

sed -i 's/\\part{Cvičení}/\\part{Cvičení}\\input cviceni_definice.tex/' python.tsed -i 's/\\part{Přednášky}/\\part{Přednášky}\\input prednasky_definice.tex/' python.tex

sed -i 's/\\textbackslash{}/\\/g' python.tex
sed -i 's/\\dm */\\dm/' python.tex
sed -i 's/\\begin{equation\*}/\\[/' python.tex
sed -i 's/\\end{equation\*}/\\]/' python.tex
sed -i 's/\\begin{split}/\\relax /' python.tex
sed -i 's/\\end{split}/\\relax /' python.tex
sed -i 's/\\usepackage{geometry}/\\usepackage[margin=2cm, left=1.5cm, right=1.5cm]{geometry}/' python.tex
sed -i 's/\\usepackage{unicode-math}//' python.tex

vlna python.tex

sed -i "s/title{Python}/title{Matematika}/" python.tex
sed -i 's/Corollary/Důsledek/' python.tex
sed -i 's/Theorem/Věta/' python.tex
sed -i 's/Remark/Poznámka/' python.tex
sed -i 's/Definition/Definice/' python.tex
sed -i 's/Example/Příklad/' python.tex
sed -i 's/begin{sphinxadmonition}{note}{Příklad (Řešení)}/begin{sphinxadmonition}{note}{Řešení}/' python.tex

xelatex python
xelatex python
xelatex python

cd -
cp $directory/python.pdf Matematika.pdf

#echo "Pro upload na server spustit nasledujici prikaz"
#echo "scp Dynamicke_modely_populaci_text.pdf cornus.mendelu.cz:html/dmp/"


