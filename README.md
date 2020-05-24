# flask_api
## install required
```
pip install -r requirements.txt
```

## flask run
```
export FLASK_APP=flask_api.py
flask run
```

## gunicorn run
```
gunicorn flask_api:app -b 0.0.0.0:5000
```

---

## docker build
```
docker build -t flask_api:v1 .
```
## docker run
```
docker run -d -p 5000:5000 flask_api:v1
```

---

## docker-compose run
```
docker-compose up -d
```
