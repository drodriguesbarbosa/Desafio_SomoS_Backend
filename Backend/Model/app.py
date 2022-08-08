from flask import Flask, request
from flask_cors import CORS
from Controller.controllercartas import controllercartas

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': '*'}})

#liberando ç, ^, ~, ´#
app.config['JSON_ASCII'] = False 

@app.route("/")
def root():
    return "<h1>API com Flask</h1>"

app.run(debug=True)

###inserir rotas##

@app.route('insert_card', methods=['POST'])
def insert_carta():

    post_data = request.get_json(silent=True)

    result = controllercartas().insertCards( post_data.get('name', 'hp', 'attack', 'defense', 'special_attack', 'special_Defense', 'speed'))

    if result:
        return jsonify({'Status Code' : '201'})
    else:
        return jsonnify({'status' : 'False'})



if __name__ == '__main__':
    app.run()