from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.controllercartas import ControllerCartas
from controller.controllerarena import ControllerArena



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
                                               post_data.get ('speed')
                                               ) 

                                         

    if result:
        return jsonify({'status': '200'})
    else:
        return jsonify({'status' : 'False'})


@app.route('/select_all_cards', methods=['GET'])
def select_all_cards():

    result = ControllerCartas().select_all_cards()

    if result:
        return jsonify({'status': '200', 'result': result})
    else:
        return jsonify({'Status Code': '404'})


@app.route('/select_card_by_id/<string:id>', methods=['GET'])
def select_card_by_id(id):

    result = ControllerCartas().select_card_by_id(id)

    if result:
        return jsonify({'status': '200', 'id': result})
    else:
        return jsonify({'status': 'false'})    


@app.route('/update_card/<string:id>', methods = ['POST'])
def update_card(id):

    post_data = request.get_json(silent=True)

    result = ControllerCartas().update_card( post_data.get ('id'),
                                             post_data.get ('name'),
                                             post_data.get ('hp'),
                                             post_data.get ('attack'),
                                             post_data.get ('defense'),
                                             post_data.get ('special_attack'),
                                             post_data.get ('special_defense'),
                                             post_data.get ('speed'))

  

    if result:
        return jsonify({'Status Code' : '200'})
    else:
        return jsonify({'status' : 'False'})


@app.route('/select_cards', methods=['POST'])
def select_cards(id):

    result = ControllerArena().select_cards(id)

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})
#    if result:
#        return jsonify({'winner': '200', 'loser': result, 'details':{'hp': 'hp', 'attack': , 'defense': , 'special_attack': , 'special_defense': , 'speed': }})
#    else:
#        return jsonify({'status': 'false'})



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


