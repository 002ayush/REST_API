from flask import Flask,jsonify
app = Flask(__name__)


@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    val = a+b;
    ds = {
        "a":a,
        "b":b,
        "sum" : val,
        "description" : "This is the REST API program",
        "l1" : [12,15,7,8,9,57,65,45]
    }
   
    return  jsonify(ds)
if __name__ == "__main__":
    app.run(debug=True)