# flask_api

## required
```
pip install flask
```

---
## GET TEST
### Nomal
```
curl localhost:5000?name='World'
```
```
curl localhost:5000?name='Taro'\&age=88
```

### Error
```
curl -i localhost:5000
```
```
curl -i localhost:5000?name=
```
```
curl -i localhost:5000?name='Taro'\&age=aaa
```

---

## POST
### Nomal
```
curl -X POST localhost:5000
```
```
curl -X POST localhost:5000?q_param=100
```
```
curl -X POST localhost:5000 -d f_param=form_parameter
```
```
curl -X POST localhost:5000?q_param=100 -d f_param=form_parameter
```

### Error
```
curl -X POST localhost:5000?q_param=query -d f_param=form_parameter
```
