from main import Mathcalc
from reqparser import Myrequest
from flask_restful import Resource

class MainMath(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            inputs = Myrequest()
            inputz = inputs.get_input()
            val = Mathcalc()
            result = val.calc(inputz)
        except Exception as e:
            print(e)
        else:
            return result
