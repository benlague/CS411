ENVIRONMENT ?= dev
FLASK_DEBUG ?= 1

lint-py:
	flake8 src/python

lint-js:
	npm run lint --prefix src/javascript/web-app

lint: lint-py lint-js

install-deps-py-dev:
	pip install -r src/python/requirements-dev.txt

install-deps-py-core:
	pip install -r src/python/requirements.txt

install-deps-py: install-deps-py-dev install-deps-py-core

install-deps-js-dev:
	npm install --prefix src/javascript/web-app --only=dev

install-deps-js-core:
	npm install --prefix src/javascript/web-app --only=prod

install-deps-js: 
	npm install --prefix src/javascript/web-app

install-deps: install-deps-py install-deps-js

run-server:
	export ENVIRONMENT=${ENVIRONMENT}  && \
	export FLASK_DEBUG=${FLASK_DEBUG} && \
	export FLASK_APP="src/python/services/api/app:app" && \
	flask run -h 0.0.0.0 -p 8001

run-client:
	npm run serve --prefix src/javascript/web-app

db-migrate:
	export ENVIRONMENT=${ENVIRONMENT} && \
	export FLASK_APP="src/python/services/api/app:app" && \
	flask db migrate -m "$(MESSAGE)"

db-upgrade:
	export ENVIRONMENT=${ENVIRONMENT}  && \
	export FLASK_APP="src/python/services/api/app:app" && \
	flask db upgrade

db-downgrade:
	export ENVIRONMENT=${ENVIRONMENT}  && \
	export FLASK_APP="src/python/services/api/app:app" && \
	flask db downgrade

unit-tests-py:
	pytest src/python/tests/unit

integration-tests-py:
	pytest src/python/tests/integration

all-tests-py:
	pytest src/python/tests
