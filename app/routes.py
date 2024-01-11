from flask import request, render_template,session
from app import app
from app.controller import UserController, CategoryController, ProductController
from flask_session import Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/users', methods=['POST','GET'])
def users():
    """
    This function handles the requests related to users.
    """
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()
@app.route('/users/<id>', methods=['PUT','GET','DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
    
@app.route('/category', methods=['POST','GET'])
def categories():
    if request.method == 'GET':
        return CategoryController.index()
    else:
        return CategoryController.store()

@app.route('/category/<int:category_id>', methods=['GET','PUT','DELETE'])
def get_category(category_id):
    if request.method == 'GET':
        return CategoryController.show(category_id)
    elif request.method == 'PUT':
        return CategoryController.update(category_id)
    elif request.method == 'DELETE':
        return CategoryController.delete(category_id)
    
@app.route('/category', methods=['POST'])
def create_category():
    return CategoryController.store()


@app.route('/product', methods=['GET','POST'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    return ProductController.store()


@app.route('/product/<int:product_id>', methods=['GET','PUT','DELETE'])
def product(product_id):
    if request.method == 'GET':
        return ProductController.show(product_id)
    elif request.method == 'PUT':
        return ProductController.update(product_id)
    elif request.method == 'DELETE':
        return ProductController.delete(product_id)

@app.route('/')
def home():
    if not session.get("username"):
        # if not there in the session then redirect to the login page
        return render_template("login.html")
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["username"] = request.form.get("username")
        return UserController.login()
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Jika pengguna berhasil login, tampilkan halaman dashboard
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    return UserController.logout()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return UserController.register()
    return render_template('register.html')

@app.route('/edit_product/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    if request.method == 'PUT':
        return ProductController.edit_product(product_id)
    else:
        return render_template('dashboard.html')
    
@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if request.method == 'DELETE':
        return ProductController.delete_product(product_id)
    else:
        return render_template('dashboard.html')
    
@app.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if request.method == 'PUT':
        return ProductController.updateproduct(product_id)
    else:
        return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)
