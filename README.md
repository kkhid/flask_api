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

---

# TEST Command
## GET
```
curl localhost:5000?name='World'
curl localhost:5000?name='Taro'\&age=88
```

## GET ERROR
```
curl -i localhost:5000
curl -i localhost:5000?name=
curl -i localhost:5000?name='Taro'\&age=aaa
```

---

## POST
```
curl -X POST localhost:5000
curl -X POST localhost:5000?q_param=100
curl -X POST localhost:5000 -d f_param=form_parameter
curl -X POST localhost:5000?q_param=100 -d f_param=form_parameter
```

## POST ERROR
```
curl -X POST localhost:5000?q_param=query -d f_param=form_parameter
```
