1. run django app

1.1 Hello World

	python hello.py 0.0.0.0:8000

	Note: add ALLOWED_HOSTS=[ip] to run from remote host

	install gunicorn. run: gunicorn hello --log-file=- --bind=0.0.0.0:8000

1.2 template

copy hello.py to project_name/project_name.py

django-admin createproject foo --template=project_name

variable pass as the context: project_name, project_directory, secret_key, docs_version
