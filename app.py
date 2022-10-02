#!flask/bin/python
from flask import Flask, jsonify, json, request
from datalib import garden_tools

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my Garden Wrold"


@app.route('/v1/garden/gettools', methods=['GET'])
def gettools():
    garden_tools_obj = garden_tools.GardenTools()
    tools_json = garden_tools_obj.get_garden_tools_json_data()
    return jsonify(tools_json)


@app.route('/v1/garden/getplantingCalender', methods=['GET'])
def getplantingCalender():
    pass


@app.route('/v1/garden/getrecentposts', methods=['GET'])
def getrecentposts():
    pass


@app.route('/v1/garden/addnewtool', methods=['POST'])
def addnewgardentool():
    record = json.loads(request.data)
    print(record)
    return jsonify({'message': 'record added'})


@app.route('/v1/garden/postmystory', methods=['POST'])
def postmystory():
    pass


if __name__ == '__main__':
    app.run(debug=True)
