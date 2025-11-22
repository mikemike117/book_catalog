from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

if __name__ == "__main__":
    print("Файл models.py запущен!")
    print("Проверка импортов...")
    
    try:
        from flask_sqlalchemy import SQLAlchemy
        print("SQLAlchemy импортирован успешно")
    except ImportError as e:
        print(f"Ошибка импорта: {e}")