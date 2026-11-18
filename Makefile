# Preklad a publikace ucebniho textu Matematika
SCRIPTS = scripts
BUILD   = _build

.PHONY: all html pdf upload serve clean help

help:
	@echo "make html    - preklad webu do $(BUILD)/html"
	@echo "make pdf     - preklad PDF (scripts/Matematika.pdf)"
	@echo "make all     - html + pdf"
	@echo "make upload  - html a publikace na GitHub Pages (gh-pages)"
	@echo "make serve   - lokalni nahled webu na http://localhost:8000"
	@echo "make clean   - smazani $(BUILD) a pomocnych souboru LaTeXu"

all: html pdf

html:
	cd $(SCRIPTS) && bash build.sh

pdf:
	cd $(SCRIPTS) && bash build_latex.sh

upload: html
	cd $(SCRIPTS) && bash upload.sh

serve:
	python3 -m http.server -d $(BUILD)/html 8000

clean:
	rm -rf $(BUILD)
	find . -path ./.git -prune -o -type f \( -name '*.aux' -o -name '*.log' -o -name '*.fls' \
		-o -name '*.fdb_latexmk' -o -name '*.cb' -o -name '*.cb2' -o -name '*.out' -o -name '*.toc' \) -print -delete
