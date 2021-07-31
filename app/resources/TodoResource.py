from flask_restful import Resource


class SingleTodoResource(Resource):
    def get(self, id):
        from app.models.all_models import TodoModel
        from app.schemas.TodoSchema import TodoSchema

        todo_schema = TodoSchema()
        todo = TodoModel.query.filter_by(id=id).first()

        output = todo_schema.dump(todo)

        return output


class AllTodoResource(Resource):
    def get(self):
        from app.models.all_models import TodoModel
        from app.schemas.TodoSchema import TodoSchema

        todo_schema = TodoSchema(many=True)

        todos = TodoModel.query.all()

        output = todo_schema.dump(todos)

        return output
