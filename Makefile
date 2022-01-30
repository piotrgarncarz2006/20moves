.DEFAULT: help
help:
	@echo "make install"
	@echo "       copy game to /usr/local/bin directory"
	@echo "make dependencies"
	@echo "       install dependencies"
install: dependencies
	cp . /usr/local/bin -r
dependencies:
	pip3 install pygame
