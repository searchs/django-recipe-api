# django-recipe-api

```bash
docker-compose run --rm app sh -c "django-admin startproject app ."


docker-compose run --rm app sh -c "python manage.py collectstatic"

#Replace wirh Ruff [ruff check --fix]
docker-compose run --rm app sh -c "flake8"

# Testing
docker-compose run --rm app sh -c "python manage.py test"



```
