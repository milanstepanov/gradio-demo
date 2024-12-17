install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint *.py


format:
	black *.py


run:
	python hello.py


all: install,lint, format
