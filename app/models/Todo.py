from app.extensions import db


class TodoModel(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    is_completed = db.Column(db.Boolean, default=False)

    # def __repr__(self):
    #     return f'Todo with ID: {self.id}, Name is: {self.name}, Completed Status is: {self.is_completed}'
