# Django Recipe API — Historical Learning Project

> **Status:** Archived / historical engineering project. This repository is retained for learning and provenance; it is not an actively maintained production API.

This project is a Django REST API exercise built around a recipe/user domain, Docker-based development and PostgreSQL-backed configuration.

## What it demonstrates

- Django 3.2-era application structure
- Django REST Framework
- custom user model and user API work
- OpenAPI/schema generation with drf-spectacular
- PostgreSQL configuration through environment variables
- Docker / Docker Compose development workflow
- automated tests and linting workflow

## Historical development commands

Representative commands used by the project include:

```bash
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py test"
```

Do not treat credentials that may appear in old tutorial notes or Git history as valid accounts.

## Security and maintenance status

The current tree no longer commits a reusable Django `SECRET_KEY`; local execution should provide `DJANGO_SECRET_KEY` through the environment. Database host/name/user/password configuration is also environment-driven.

The project uses an older Django generation and should not be treated as a current production baseline without dependency, security, deployment and API-design review.

## Archive policy

No feature development is planned here. If an API pattern remains useful, migrate the specific implementation idea into an actively maintained repository rather than reviving this project wholesale.

Archiving the repository does not imply that its dependencies or implementation reflect current engineering standards.
