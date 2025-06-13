# pizzaApi 
# 🍕 Pizza Restaurant API

RESTful API built with Flask, SQLAlchemy, and Flask-Migrate. No frontend required — test via Postman.

## 📦 Setup

```bash
git clone https://github.com/<you>/pizza-api-challenge.git
cd pizza-api-challenge
pipenv install
pipenv shell

export FLASK_APP=server/app.py      # Windows: set FLASK_APP=server/app.py
flask db upgrade
python server/seed.py               # (optional) sample data
flask run
