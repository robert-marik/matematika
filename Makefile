.PHONY: help install html pdf upload clean

help:
	@echo "make install  - nainstaluje balicky do aktivniho mamba prostredi (scripts/packages.sh)"
	@echo "make html     - kompilace do HTML (scripts/build.sh)"
	@echo "make pdf      - kompilace do PDF (scripts/build_latex.sh, vyzaduje LaTeX)"
	@echo "make upload   - nahrani HTML na GitHub Pages (scripts/upload.sh)"
	@echo "make clean    - smaze _build"

# Skripty se spousteji z adresare scripts (pouzivaji relativni cesty).
install:
	cd scripts && bash packages.sh

html:
	cd scripts && bash build.sh

pdf:
	cd scripts && bash build_latex.sh

upload:
	cd scripts && bash upload.sh

clean:
	rm -rf _build
