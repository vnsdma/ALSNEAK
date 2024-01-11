from flask import jsonify, request
from app.model.category_product import CategoryProduct
from app import app,db

def index():
    try:
        categories = CategoryProduct.query.all()
        return jsonify([{'id': category.id, 'name': category.name} for category in categories])
    except:
        return jsonify({'message': 'No categories found!'})
    

def show(category_id):
    try:
        categories = CategoryProduct.query.get_or_404(category_id)
        return jsonify({'id': categories.id, 'name': categories.name})
    except:
        return jsonify({'message': 'Category not found!'})

def store():
    data = request.json
    new_category = CategoryProduct(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'New category created!'})

def update(product_id):
    category = CategoryProduct.query.get_or_404(product_id)
    data = request.json
    category.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Category updated successfully!'})

def delete(category_id):
    category = CategoryProduct.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})