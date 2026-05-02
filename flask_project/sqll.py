from flask import Flask, jsonify
import requests, json
from flask_sqlalchemy import SQLAlchemy

sqll = Flask(__name__)

sql_uri='mysql://root:password@localhost:3306/mydatabase'
postgres_uri='postgresql://postgres:password@localhost:5432/mydatabase'

sqll.config['SQLALCHEMY_DATABASE_URI'] = sql_uri
sqll.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sqll.config['SQLALCHEMY_ECHO'] = True
sqll.config['SQLALCHEMY_POOL_SIZE'] = 100
sqll.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
sqll.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
sqll.config['SQLALCHEMY_MAX_OVERFLOW'] = 20

db = SQLAlchemy(sqll)

#sqll.config['POSTGRES_URI'] = postgres_uri

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer,unique=False, nullable=False)



@sqll.route('/')
def hello():
    return "Hello, SQL!"

@sqll.route('/fetch')
def fetchuser():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    jsonvalresults=json.loads(response.text)[results][0]
    user1=User(id=jsonvalresults['id'],fname=jsonvalresults['name']['first'], email=jsonvalresults['email'], age=jsonvalresults['age'])
    db.session.add(user1)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'})
    #print(jsonvalresults['name']['firx`st'])
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    sqll.run(debug=True)