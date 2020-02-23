import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
from vaal import MainMath
app = Flask(__name__)
api = Api(app)

def main(restPort):
    api.add_resource(MainMath, '/calc')
    app.run(host='0.0.0.0', port=restPort)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print()
        print('\tUsage : python src/hci_sizing_engine.py restPort')
        print()
        sys.exit()

    restPort = sys.argv[1]
    if restPort.isdigit():
        restPort = int(restPort)
    else:
        print()
        print('restPort must be an integer')
        print()
        sys.exit()
    main(restPort)
