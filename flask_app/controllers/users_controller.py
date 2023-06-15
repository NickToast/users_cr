from flask import  render_template, redirect, request  # Import Flask to allow us to create our app, if u need render_template

#from user.py file, import the class User
from flask_app.models.users_model import User


# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# app.secret_key = 'life' 	#key goes into here
#this is now in __init__.py but now we must import it from that file
from flask_app import app


@app.route('/')
def index():
    return redirect('/users')

#show
@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users = users)



# #show route
@app.route('/users_new')
def users_new():
    return render_template('add_user.html')



# #action route
@app.route('/user/add', methods=['POST'])
def add():
    #using class method save() here to get the form data inputted by the user and INSERT INTO users table
    User.save(request.form)
    return redirect ('/users')

#EDIT ACTION ROUTE
@app.route('/user/edit', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')



#show one page
@app.route('/users/<int:user_id>')
def show(user_id):
    # data = {
    #     "id" : user_id
    # }
    user = User.get_one({"id":user_id})
    return render_template('show_one.html', user = user)

#edit page
@app.route('/edit/<int:user_id>')
def edit(user_id):
    user = User.get_one({"id":user_id})
    return render_template('edit.html', user = user)

#delete
@app.route('/delete/<int:user_id>')
def delete(user_id):
    User.delete({"id":user_id})
    return redirect('/users')
