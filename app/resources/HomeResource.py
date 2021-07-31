from flask_restful import Resource


class HomeResource(Resource):
    def get(self):
        return {
            "msg": "This is home route with Get Request"
        }

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
