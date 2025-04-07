.PHONY: init ci build rebuild migrate lang-make lang-compile reformat reformat-check flake8 isort isort-check lint

init:
	curl -sSL https://install.python-poetry.org  | python3 -
	poetry install

ci:
	poetry run pytest --cov=./

build:
	docker-compose build

rebuild:
	docker-compose build --force-rm --no-cache

migrate:
	docker-compose run --rm web python manage.py migrate

lang-make:
	poetry run python manage.py makemessages --no-location --no-wrap

lang-compile:
	poetry run python manage.py compilemessages

pytest:
	docker-compose run --rm web pytest

reformat:
	black .

reformat-check:
	black --check .

flake8:
	flake8 .

isort:
	isort .

isort-check:
	isort --check-only --diff

lint: reformat-check flake8 isort-check
