from app import db

class CategoryProduct(db.Model):
    __tablename__ = 'category_product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    products = db.relationship('Product', backref='category', lazy=True)