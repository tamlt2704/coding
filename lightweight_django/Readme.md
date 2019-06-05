1. run django app

python hello.py 0.0.0.0:8000

Note: add ALLOWED_HOSTS=[ip] to run from remote host

install gunicorn. run: gunicorn hello --log-file=- --bind=0.0.0.0:8000
