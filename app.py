#!flask/bin/python
from flask import Flask, jsonify
import datalib

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my Garden Wrold"


@app.route('/v1/garden/gettools', methods=['GET'])
def gettools():

    tools_json = [{"toolname": "hand fork", "toolusage": "used for loosening garden soil in small area",
                    "toolsize": "less than 1 feet", "warning": "Sharp edges might cause injury"},
                      {"toolname": "pruner", "toolusage": "used for pruning the leafs or small branches",
                       "toolsize": "6 to 8 inches", "warning": "keep it locked when not in use"}]
    return jsonify(tools_json)


@app.route('/v1/garden/getplantingCalender', methods=['GET'])
def getplantingCalender():
    pass


@app.route('/v1/garden/getrecentposts', methods=['GET'])
def getrecentposts():
    pass


@app.route('/v1/garden/postmystory', methods=['POST'])
def postmystory():
    pass


if __name__ == '__main__':
    app.run(debug=True)
