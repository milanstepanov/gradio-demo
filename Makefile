install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint: format
	pylint *.py

test:
	pytest -vv --cov

format:
	black *.py


run:
	python hello.py


all: install lint test
