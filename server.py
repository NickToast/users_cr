from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app, if u need render_template

#from user.py file, import the class User
from user import User

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'life' 	#key goes into here



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





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.