# pylint: skip-file
from flask import request,render_template, request, redirect, url_for, flash, jsonify,session, Flask
from app.model.user import Users
from app import response, db
from flask_session import Session
import bcrypt

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "Berhasil")
    except Exception as e:
        print(e)
        
def store():
    try:
        name = request.json['name']
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        
        users = Users(name=name,username=username, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.ok('','Successfully create data!')
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        user = Users.query.filter_by(id=id).first()
        user.email = email
        user.name = name
        user.setPassword(password)
        
        db.session.commit()
        
        return response.ok('','Successfully update data')
    except Exception as e:
        print(e)
        
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty')
        db.session.delete(user)
        db.session.commit()
        
        return response.ok('','Succesfully delete data!')
    except Exception as e:
        print(e)
def transform(users):
    array = []
    for i in users:
        array.append({
            'id' : i.id,
            'name' : i.name,
            'email' : i.email
        })
    return array

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    
    return data

def get(username):
    try:
        user = Users.query.filter_by(username=username).first()
        if not user:
            return response.badRequest([], 'Empty....')
        data = singleTransform(user)
        return data
    except Exception as e:
        print(e)

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve the user from the database using the provided username
        user = Users.query.filter_by(username=username).first()

        # Check if the user exists and verify the password using bcrypt
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # Authentication successful
            session["username"] = request.form.get("username")
            return render_template('dashboard.html')
        else:
            return 'Invalid username or password'

    return render_template('login.html')

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create a new User instance
        new_user = Users(username=username, password=hashed_password, email=email, name=name)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return 'Registration successful'

    return render_template('register.html')

def logout():
    session["name"] = None
    return render_template('login.html')

