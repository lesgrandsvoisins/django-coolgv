# Loading environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

ifndef DOCKER_CONTAINER
	DOCKER_CONTAINER := web
endif

ifeq ($(USE_DOCKER),1)
	EXEC_CMD := docker-compose exec -ti $(DOCKER_CONTAINER)
	PROJECT_PATH := /home/wagtail/django-lgv/
else
	EXEC_CMD := 
	PROJECT_PATH := ${dir ${abspath ${lastword ${MAKEFILE_LIST}}}}
endif

venv:
	$(EXEC_CMD) python -m venv .venv

requirements:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install --upgrade pip
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/pip install -r requirements.txt

secretkey:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

startproject:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/django-admin startproject settings .

runserver:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python $(PROJECT_PATH)manage.py runserver

makemigrations:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python $(PROJECT_PATH)manage.py makemigrations

migrate:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python $(PROJECT_PATH)manage.py migrate

createsuperuser:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python $(PROJECT_PATH)manage.py createsuperuser --username admin --email chris@mann.fr --skip-checks

collectstatic:
	$(EXEC_CMD) $(PROJECT_PATH).venv/bin/python $(PROJECT_PATH)manage.py collectstatic --no-input