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

sed -i 's/Corollary/Důsledek/' $directory/*/slidy.html
sed -i 's/Theorem/Věta/' $directory/*/slidy.html
sed -i 's/Remark/Poznámka/' $directory/*/slidy.html
sed -i 's/Definition/Definice/' $directory/*/slidy.html
sed -i 's/Example/Příklad/' $directory/*/slidy.html

# Copy custom css file
cp custom.css $directory/_static/styles/
cp custom.css $directory/_static/
