test:
	clear
	pytest -v

coverage:
	pytest -v --cov-report term --cov-report html:htmlcov --cov-report xml --cov-fail-under=90 --cov=src/