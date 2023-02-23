# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/html

# touch ../intro.md
sphinx-build -Ea ../ $directory -b html

# # Loop over lectures do open ipynb files in Colab rather than md files.
# echo "Fixing Colab links from md to ipynb."
# for i in $directory/prednaska/*.html
# do
#     sed -i 's/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/main\/prednaska\/\(..\)\.md/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/gh-pages\/_sources\/prednaska\/\1.ipynb/' $i
# done

# sed -i 's/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/main\/intro\.md/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/gh-pages\/_sources\/intro.ipynb/' $directory/intro.html

sed -i 's/<p>\\iffalse<\/p>//' $directory/*/*.html
sed -i 's/<p>\\fi<\/p>//' $directory/*/*.html
sed -i 's/<span>Example <\/span> (Řešení)/Řešení/' $directory/cviceni/cviceni*.html
sed -i 's/<body /<body class="cviceni" /' $directory/cviceni/cviceni*.html

sed -i 's/Corollary/Důsledek/' $directory/*/index.html
sed -i 's/Theorem/Věta/' $directory/*/index.html
sed -i 's/Remark/Poznámka/' $directory/*/index.html
sed -i 's/Definition/Definice/' $directory/*/index.html
sed -i 's/Example/Příklad/' $directory/*/index.html
sed -i 's/\\dm//' $directory/*/index.html

sed -i 's/<p><code class="docutils literal notranslate"><span class="pre">ww2:\(.*\)<\/span><\/code><\/p>/<a onclick=otevrit("\1"); target="_blank" class="WWotazka">Testová otázka<\/a>/' $directory/*/index.html

sed -i 's/<p>https:\/\/youtu.be\/\(.*\)<\/p>/<div class="Ycontainer"> <iframe class="responsive-iframe" src="https:\/\/www.youtube.com\/embed\/\1"><\/iframe> <\/div>/' $directory/*/index.html

sed -i 's/<p>manimp:\(.*\)|\(.*\)<\/p>/<div class="obtekat"><figure><a href="https:\/\/user.mendelu.cz\/marik\/manim\/\1" target=_blank><img src="https:\/\/user.mendelu.cz\/marik\/manim\/thumbs\/\1.jpg"><\/a><figcaption>\2 <a href="\/marik\/manim\/\1" class=but-prez target=_blank>Otevřít prezentaci<\/a><\/figcaption><\/figure><\/div>/' $directory/*/index.html

sed -i 's/<p>manim:\(.*\)|\(.*\)|\(.*\)<\/p>/<div class="obtekat"><figure><a href="https:\/\/user.mendelu.cz\/marik\/manim\/\1" target=_blank><img src="https:\/\/user.mendelu.cz\/marik\/manim\/thumbs\/\1.jpg"><\/a><figcaption>\3 <a href="https:\/\/user.mendelu.cz\/marik\/manim\/\1" class=but-prez target=_blank>Otevřít prezentaci<\/a> <a href="https:\\\\youtu.be\/\2" class=but-video target=_blank>Spustit video<\/a><\/figcaption><\/figure><\/div>/' $directory/*/index.html

sed -i 's/<p><img alt="\(.*\)" src="\(.*\)" \/><\/p>/<p><img src="\2" \/><figcaption>\1<\/figcaption><\/p>/' $directory/*/index.html

sed -i 's/<\/body>/<script>jQuery(".bd-toc").removeClass("show")<\/script><\/body>/' $directory/*/index.html
sed -i 's/<\/body>/<script>jQuery(".bd-toc").removeClass("show")<\/script><\/body>/' $directory/cviceni/cviceni*.html
sed -i 's/<body>/<script>jQuery(".bd-toc").removeClass("show")<\/script><\/body>/' $directory/cviceni/cviceni*.html


# Copy custom css file
cp custom.css $directory/_static/styles/
cp custom.css $directory/_static/
cp custom.js $directory/_static/
