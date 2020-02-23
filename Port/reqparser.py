from flask_restful import reqparse
import json

class Myrequest:
    def __init__(self):
        pass

    def get_input(self):
        """Deserialize the JSON object and returns the input"""
        parser = reqparse.RequestParser()
        parser.add_argument('inputs', type=str, required=True)
        args = parser.parse_args()
        inputs = json.loads(args['inputs'])
        return inputs
