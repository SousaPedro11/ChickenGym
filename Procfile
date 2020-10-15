release: python3 run.py db init && python3 run.py db migrate && python3 run.py db upgrade
web: gunicorn run:app