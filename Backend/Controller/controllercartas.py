
from model.Connection import Connection

class ControllerCartas():

    def __init__(self):
        self.status = 1


    def inserir_carta(self, name, hp, attack, defense, special_attack, special_defense, speed):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO "POKEMONS"."CARTAS" (  name, hp, attack, defense, special_attack, special_defense, speed     ) 
                                              VALUES         (    %s, %s,     %s,      %s,             %s,              %s,    %s)
                    """

            record_to_insert = ( name , hp , attack , defense , special_attack , special_defense , speed , )

            cursor.execute(insert_query, record_to_insert)
            conn_obj.commit()
            count = cursor.rowcount
            
            print(count, "Record inserted successfully into cartas table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during carta insertion. Error: {}".format(str(ex)))
            return False
