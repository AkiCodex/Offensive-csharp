
import flask
from flask import *
import json

app = Flask(__name__)   
@app.route("/" , methods=[ "GET" , "POST"])  
def index():
    
    return render_template('index.html')


@app.route("/results" , methods=[ "POST","GET"])
def results():
    name = request.form['username_value']
    return render_template( 'index.html' , name=name )
    
    

if __name__  == '__main__':
    app.run( port=1345 ,debug=True)  
