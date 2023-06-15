
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# app.secret_key = 'life' 	#key goes into here
#this is now in __init__.py but now we must import it from that file
from flask_app import app

from flask_app.controllers import users_controller

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.