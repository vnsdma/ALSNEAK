# pylint: skip-file
from app import db, app
# Definisi Model

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category_product.id'))

if __name__ == '__main__':
    app.run()