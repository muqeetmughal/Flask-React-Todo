from app.extensions import ma


class TodoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        from app.models.all_models import TodoModel
        model = TodoModel
