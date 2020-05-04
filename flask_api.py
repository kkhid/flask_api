from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Name cannot be blank!")
        parser.add_argument("age", type=int, help="Age cannot be converted")
        args = parser.parse_args()
        if not args["name"]:
            abort(401, message="Name cannot be blank!")
        return {"name": "Hello {}!".format(args["name"]), "age": args["age"]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "q_param", type=int, location="args", help="q_param is numbers"
        )
        parser.add_argument("f_param", location="form")
        args = parser.parse_args()
        return {
            "post": "Hello World!",
            "q_param": args["q_param"],
            "f_param": args["f_param"],
        }


api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True)


# -----------------------------------
# GET
# curl localhost:5000?name='World'
# curl localhost:5000?name='Taro'\&age=88

# ERROR
# curl -i localhost:5000
# curl -i localhost:5000?name=
# curl -i localhost:5000?name='Taro'\&age=aaa

# -----------------------------------
# POST
# curl -X POST localhost:5000
# curl -X POST localhost:5000?q_param=100
# curl -X POST localhost:5000 -d f_param=form_parameter
# curl -X POST localhost:5000?q_param=100 -d f_param=form_parameter

# ERROR
# curl -X POST localhost:5000?q_param=query -d f_param=form_parameter
