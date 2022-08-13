
from model.connection import Connection

class ControllerArena():

    def __init__(self):
        self.status = 1


    def select_playerOneCard(self, id):
        try:

            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT id, hp, attack, defense, special_attack, special_defense, speed
                                  FROM "POKEMONS"."CARTAS"
                                  WHERE id IN (%s)"""
    
            fields_to_select = (id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("Card {} not found!".format(id))
                return False

            cardPlayerOne = {
                      'playerOneCard': record[0]
                    , 'name': record[1]}


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return cardPlayerOne

        except Exception as ex:

            print("Error during card selection. Error: {}".format(str(ex)))
            return False


ControllerArena.select_playerOneCard