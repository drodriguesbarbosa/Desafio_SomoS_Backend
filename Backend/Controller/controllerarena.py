
from model.connection import Connection

class ControllerArena():

    def __init__(self):
        self.status = 1


    def select_cards(self, id):
        try:

            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT id, hp, attack, defense, special_attack, special_defense, speed
                                  FROM "POKEMONS"."CARTAS"
                                  WHERE id IN (%s)"""
            
            playerOneCard = (playerOneCard)
            playerTwoCard = (playerTwoCard)

            cursor.execute(sql_select_query, playerOneCard)
            cursor.execute(sql_select_query, playerTwoCard)
            record = cursor.fetchone()

            if record is None:
                print("Card {} not found!".format(id))
                return False

            selectCards = {
                      'playerOne': record[0][0]
                     ,'playerTwo': record [1][0]
                      }


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return selectCards

        except Exception as ex:

            print("Error during card selection. Error: {}".format(str(ex)))
            return False


    def select_playerTwoCard(self, id):
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

            playerTwoCard = {
                      'playerTwoCard': record[0]
                      }


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return playerTwoCard

        except Exception as ex:

            print("Error during card selection. Error: {}".format(str(ex)))
            return False


    
    def select_cards(self):
        try: 
           cartas = select_playerOneCard, select_playerTwoCard
           
           if cartas is None:
                print("Card {} not add!".format(id))
                return False

        except Exception as ex:

            print("Error during card add. Error: {}".format(str(ex)))
            return False