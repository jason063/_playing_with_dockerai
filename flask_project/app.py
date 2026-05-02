from flask import Flask
from oop import Rectangle 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/rectangle")
def rectangle():
    rect = Rectangle(5, 3)
    area = rect.area()
    perimeter = rect.perimeter()
    return f"Area: {area}, Perimeter: {perimeter}"

if __name__ == "__main__":
    app.run(debug=True)