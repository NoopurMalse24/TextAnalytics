lass Datacleaning_review(Resource):
    def get(self):
        my_dir = os.path.dirname(__file__)
        file_path = os.path.join(my_dir, "../datacleaning.py")
        file = open(file_path)
        getvalues = {}
        exec(file.read(),getvalues)
        return jsonify({'data':getvalues['review_df'].to_json()})