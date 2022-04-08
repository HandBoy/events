SETTINGS := develop

help: 		## Show this help.
	@echo "Please use \`make <target>' where <target> is one of"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:		## Builds, (re)creates, starts, and attaches to containers for a service web.
	python manage.py runserver

migrations:	## Run makemigrations django command.
	python manage.py makemigrations

migrate:	## Run migrate django command.
	python manage.py migrate

db: migrations migrate

show_urls:	## Run migrate django command.
	python manage.py show_urls

test: 		## Run command test
	python manage.py test -v 2 --settings=config.settings.test

psql_start:	## Run command to start postgres container
	docker-compose -f docker/docker-compose.yml up -d events_db

psql_stop:	## Run command to stop postgres container
	docker-compose -f docker/docker-compose.yml stop events_db

psql_down:	## Run command to stop and also removes the stopped postgres container
	docker-compose -f docker/docker-compose.yml down

clean:		## remove all ".pyc" files
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf .pytest_cache
