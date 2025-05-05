from flask import Flask, request


app = Flask(__name__)

#only using the app.py
#no other libraries

#the route for the the app http://localhost:8080/api/calcs/8 (example)
#so that would mean to make it /api/calcs/value(?)

@app.route("/api/calcs/<value>", methods=["GET"]) #the value of the number you want for the http goes into there
def calculate(value): #create a method name "calculate"
    try:
        num = int(value)
        if num <= 0:
            return "Input must be a positive integer", 404
    except ValueError:
        return "Input must be a valid integer", 400
    return {
        "dec": num - 1,
        "hex": hex(num)
    }
