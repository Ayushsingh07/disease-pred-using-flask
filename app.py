import os
from flask import Flask,jsonify,request
from prediction import NaiveBayes


app = Flask(__name__)
@app.route('/pre',methods=['POST'])
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

if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 17995))
    app.run(host='0.0.0.0', port=port)