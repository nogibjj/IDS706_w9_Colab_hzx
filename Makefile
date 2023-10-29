install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py
	python -m pytest --nbval notebook/*.ipynb

format:	
	nbqa black notebook/*.ipynb
	black *.py 

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# Use Ruff instead of pylint
	nbqa ruff notebook/*.ipynb --ignore F403,F405,E501,E402,F401
	ruff check *.py --ignore F403,F405,E501
	

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
