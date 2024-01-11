from app.model.product import Product
from flask import jsonify, request, render_template
from app import db

def index():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price, 'category_id': product.category_id} for product in products])

def store():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'], category_id=data['category_id'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully!'})

def update(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.name = data['name']
    product.price = data['price']
    product.category_id = data['category_id']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

def delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully!'})

def show(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'category_id': product.category_id})


def edit_product(product_id):
    # Fetch the product from the database based on the provided product_id
    # Update the product details using the data from the request (e.g., request.json)
    # Save the updated product details to the database

    # Example:
    product = Product.query.get(product_id)
    if product:
        product.name = request.json.get('name', product.name)
        product.price = request.json.get('price', product.price)
        product.category_id = request.json.get('category_id', product.category_id)
        # Update other product attributes as needed

        db.session.commit()
        return jsonify({'message': f'Product with ID {product_id} has been updated'})
    else:
        return jsonify({'message': 'Product not found'}), 404
    
    

def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})

def showproduct():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

def updateproduct(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.form
    product.name = data['name']
    product.price = data['price']
    product.category_id = data['category_id']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})