# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/pdf

sphinx-build ../ $directory -b latex

sed -i 's/sphinxShadowBox/comment/' $directory/python.tex 
sed -i 's/documentclass\[/documentclass[twocolumn,/' $directory/python.tex
cd $directory

sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}iffalse/\\iffalse/g' python.tex
sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}fi/\\fi/g' python.tex

sed -z -i 's/\\sphinxAtStartPar\nhttps:\/\/youtu.be/%%% /g' python.tex

sed -z -i s'/\\sphinxAtStartPar\n\\sphinxcode{\\sphinxupquote{ww2:/%/g' python.tex

# sed -i 's/\\part{Cvičení}/\\end{document}/' python.tex
sed -i 's/\\textbackslash{}/\\/' python.tex
sed -i 's/\\dm */\\dm/' python.tex
sed -i 's/\\begin{equation\*}/\\[/' python.tex
sed -i 's/\\end{equation\*}/\\]/' python.tex
sed -i 's/\\usepackage{geometry}/\\usepackage[margin=2cm]{geometry}/' python.tex

vlna python.tex

sed -i "s/title{Python}/title{Matematika}/" python.tex
sed -i 's/Corollary/Důsledek/' python.tex
sed -i 's/Theorem/Věta/' python.tex
sed -i 's/Remark/Poznámka/' python.tex
sed -i 's/Definition/Definice/' python.tex
sed -i 's/Example/Příklad/' python.tex

pdflatex python
pdflatex python
cd -
cp $directory/python.pdf Matematika.pdf

#echo "Pro upload na server spustit nasledujici prikaz"
#echo "scp Dynamicke_modely_populaci_text.pdf cornus.mendelu.cz:html/dmp/"


