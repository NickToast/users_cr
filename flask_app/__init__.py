from flask import Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'life' 	#key goes into here