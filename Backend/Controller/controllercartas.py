
from model.connection import Connection

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

    def select_all_cards(self):
        try:

            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """ SELECT * FROM "POKEMONS"."CARTAS" """

            cursor.execute(sql_select_query)
            rows = cursor.fetchall()

            list_cards = []
            for row in rows:
                list_cards.append({
                          'id':                 row[0]
                        , 'name':               row[1]
                        , 'hp':                 row[3]
                        , 'attack':             row[4]
                        , 'defense':            row[5]
                        , 'special_attack':     row[6]
                        , 'special_defense':    row[7]
                        , 'speed':              row[8]})

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return list_cards

        except Exception as ex:

            print("Error during cards selection. Error: {}".format(str(ex)))
            return False

    def select_card_by_id(self, id):
        try:

            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "POKEMONS"."CARTAS" WHERE ID=%s"""
    
            fields_to_select = (id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("Card {} not found!".format(id))
                return False

            card = {
                      'id': record[0]
                    , 'name': record[1]}


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return card

        except Exception as ex:

            print("Error during card selection. Error: {}".format(str(ex)))
            return False

    def update_card(self, id, name = "nan", hp = "nan", attack = "nan", defense = "nan", special_attack = "nan", special_defense = "nan", speed = "nan"):
        try:
            connection = Connection()

            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "POKEMONS"."CARTAS" WHERE ID=%s"""

            fields_to_select = (id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("Card {} not found!".format(id))
                return False
                
            print("Updating card: \n\n" + str(record) + "\n\n") # Use it as a backup in case of issues

            update_query = """ UPDATE "POKEMONS"."CARTAS" 
                            SET                                NAME            = %s
                                                             , HP              = %s
                                                             , ATTACK          = %s
                                                             , DEFENSE         = %s
                                                             , SPECIAL_ATTACK  = %s
                                                             , SPECIAL_DEFENSE = %s
                                                             , SPEED           = %s
                                WHERE ID = %s
                            """

            if name != "nan": 
                treated_card_name = name
            else: 
                treated_card_name = record[1]

            if hp != "nan": 
                treated_card_hp = hp
            else: 
                treated_card_hp = record[2]
                
            if attack != "nan": 
                treated_card_attack = attack
            else: 
                treated_card_attack = record[3]

            if defense != "nan": 
                treated_card_defense = defense
            else: 
                treated_card_defense = record[4]
                    
            if special_attack != "nan": 
                treated_card_special_attack = special_attack
            else: 
                treated_card_special_attack = record[5]

            if special_defense != "nan": 
                treated_card_special_defense = special_defense
            else: 
                treated_card_special_defense = record[6]
                    
            if speed != "nan": 
                treated_card_speed = speed
            else: 
                treated_card_speed = record[7]
                    

            

            fields_to_update = (                                  treated_card_name
                                                                , treated_card_hp
                                                                , treated_card_attack
                                                                , treated_card_defense
                                                                , treated_card_special_attack
                                                                , treated_card_defense
                                                                , treated_card_speed
                                                                , id )
                
            cursor.execute(update_query, fields_to_update)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record updated successfully into card table.")


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during card update. Error: {}".format(str(ex)))
            return False







   

