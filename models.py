from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    filepath = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Research {self.title}>'
