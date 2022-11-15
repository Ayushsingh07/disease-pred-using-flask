from flask import Flask,jsonify,request
from prediction import NaiveBayes
import sum

app = Flask(__name__)
@app.route('/pre')
def pre():
    data=request.get_json()
    diseass=list(data.values())
    final_diss=NaiveBayes(diseass)
    result={
        "disease":final_diss
    }


    return jsonify(result)
    
@app.route('/')
def hello_world():
    return 'Hello, 1World!'
