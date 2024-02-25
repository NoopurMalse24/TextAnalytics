from flask import Flask, jsonify
from flask_restful import Api, Resource
import os, sys
from aiofiles import open as aio_open
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
api = Api(app)

class Datacleaning_descriptive(Resource):
    def get(self):
        my_dir = os.path.dirname(__file__)
        file_path = os.path.join(my_dir, "../datacleaning.py")
        file = open(file_path)
        getvalues = {}
        exec(file.read(),getvalues)
        return jsonify({'data':getvalues['descriptive_df'].to_json()})

class Datacleaning_rating(Resource):
    def get(self):
        my_dir = os.path.dirname(__file__)
        file_path = os.path.join(my_dir, "../datacleaning.py")
        file = open(file_path)
        getvalues = {}
        exec(file.read(),getvalues)
        return jsonify({'data':getvalues['rating_df'].to_json()})

class Datacleaning_review(Resource):
    def get(self):
        my_dir = os.path.dirname(__file__)
        file_path = os.path.join(my_dir, "../datacleaning.py")
        file = open(file_path)
        getvalues = {}
        exec(file.read(),getvalues)
        return jsonify({'data':getvalues['review_df'].to_json()})

api.add_resource(Datacleaning_descriptive, '/descriptivedf')
api.add_resource(Datacleaning_rating, '/ratingdf')
api.add_resource(Datacleaning_review, '/reviewdf')

if __name__ == "__main__":
    app.run(debug=True)