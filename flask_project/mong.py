from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps

mong = Flask(__name__)
mong.config["MONGO_URI"] = "mongodb+srv://nksharma063:ABoNdU5aCGpxlRyB@cluster0.yemev0v.mongodb.net/sample_mflix?retryWrites=true&w=majority"

mongo = PyMongo(mong)

def clean_docs(cursor):
    """Remove None values and serialize to JSON."""
    docs = []
    for doc in cursor:
        # Recursively drop None values
        def remove_none(d):
            if isinstance(d, dict):
                return {k: remove_none(v) for k, v in d.items() if v is not None}
            elif isinstance(d, list):
                return [remove_none(v) for v in d if v is not None]
            else:
                return d
        docs.append(remove_none(doc))
    return Response(dumps(docs), mimetype="application/json")

@mong.route('/')
def index():
    return "Welcome to the MongoDB Flask mong!"

@mong.route('/users')
def users():
    return clean_docs(mongo.db.users.find().limit(5))

@mong.route('/comments')
def comments():
    return clean_docs(mongo.db.comments.find().limit(5))

@mong.route('/movies')
def movies():
    return clean_docs(mongo.db.movies.find().limit(5))

@mong.route('/theaters')
def theaters():
    return clean_docs(mongo.db.theaters.find().limit(5))

@mong.route('/sessions')
def sessions():
    return clean_docs(mongo.db.sessions.find().limit(5))

@mong.route('/embedded_movies')
def embedded_movies():
    return clean_docs(mongo.db.embedded_movies.find().limit(5))

if __name__ == '__main__':
    mong.run(debug=True)
