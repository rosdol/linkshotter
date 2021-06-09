install:
	poetry install
	poetry run flask db upgrade
run:
	poetry run flask run