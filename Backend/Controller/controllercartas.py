from Model.Connection import Connection

class ControllerCartas():

    def __init__(self):
        self.status = 1 

    def insertCartas(self, name, hp, attack, defense, special_attack, special_Defense, speed):
        try:
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO "POKEMONS".CARTAS (NAME, HP, ATTACK, DEFENSE, SPECIAL_ATACK, SPECIAL_DEFENSE, SPEED)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                                            
            record_to_insert = (name, hp, attack, defense, special_attack, special_Defense, speed,)

            cursos.execute(insert_query, record_to_insert)
            conn_obj.commit()
            count = cursor.rowcount

            print(count, "Record inserted sucessfully into user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True
        
        except Exception as ex:

            print("Error during insertion. Error: {}".format(str(ex)))
