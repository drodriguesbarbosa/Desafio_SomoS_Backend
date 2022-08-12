from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.ControllerCartas import ControllerCartas


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': '*'}})

#liberando ç, ^, ~, ´#
app.config['JSON_ASCII'] = False 

@app.route('/')
def root():
    return "<h1>API com Flask</h1>"



@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'members': {'did_it_work': 'Yes!'}
    })
###inserir rotas##

@app.route('/inserir_carta', methods=['POST'])
def inserir_carta():

    post_data = request.get_json(silent=True)

    result = ControllerCartas().inserir_carta( post_data.get('name'),
                                               post_data.get ('hp'),
                                               post_data.get ('attack'),
                                               post_data.get ('defense'),
                                               post_data.get ('special_attack'),
                                               post_data.get ('special_defense'),
                                               post_data.get ('speed'))

  

    if result:
        return jsonify({'Status Code' : '201'})
    else:
        return jsonify({'status' : 'False'})


@app.route('/listar_cartas', methods=['GET'])
def listar_cartas():

    result = ControllerCartas().listar_cartas()

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})


@app.route('/consultar_carta/<string:id>', methods=['GET'])
def consultar_carta(id):

    result = ControllerCartas().consultar_carta(id)

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})




if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


