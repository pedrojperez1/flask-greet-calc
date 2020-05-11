from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.add(a, b)}"
    
@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.sub(a, b)}"
    
@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.mult(a, b)}"
    
@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.div(a, b)}"

@app.route('/math/<operation>')
def calculate(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    switcher = {
        'add': f"{operations.add(a, b)}",
        'sub': f"{operations.sub(a, b)}",
        'mult': f"{operations.mult(a, b)}",
        'div': f"{operations.div(a, b)}"
    }
    return switcher[operation]