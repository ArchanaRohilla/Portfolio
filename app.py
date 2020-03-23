#import  the dependencies
from flask import Flask, render_template


#code to set up Flask
app = Flask(__name__)



#set up the Flask routes
# 1.flask route for the main HTML page 
@app.route("/")
def index():
    
    return render_template("index.html")


#run the flask app
if __name__ == "__main__":
    app.run()
    





