sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}iffalse/\\iffalse/g' python.tex
sed -z -i 's/\\sphinxAtStartPar\n\\textbackslash{}fi/\\fi/g' python.tex

sed -z -i 's/\\sphinxAtStartPar\nhttps:\/\/youtu.be/%%% /g' python.tex

sed -z -i s'/\\sphinxAtStartPar\n\\sphinxcode{\\sphinxupquote{ww2:/%/g' python.tex




