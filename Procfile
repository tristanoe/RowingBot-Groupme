clock: python clock.py
a: heroku ps:scale clock=1
b: ps:scale clock=1
web: gunicorn groupme-bot:app --preload --log-file=-

