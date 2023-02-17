# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app =  Flask(__name__)

@app.route('/math/<op>')
def operation(op):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if(op == "add"):
        inter_op = add(a, b)
        return f"<h1>{str(inter_op)}</h1>"

    elif(op == "sub"):
        inter_op = sub(a, b)
        return f"<h1>{str(inter_op)}</h1>"

    elif(op == "mult"):
        inter_op = mult(a, b)
        return f"<h1>{str(inter_op)}</h1>"
        
    elif(op == "div"):
        inter_op = div(a, b)
        return f"<h1>{str(inter_op)}</h1>"
    

