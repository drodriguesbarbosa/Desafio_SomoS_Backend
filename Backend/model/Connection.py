import psycopg2

import json


class Connection():
    

    def __init__(self):

        credentials = json.load(open('database/configs.json'))


        try:

            self.conn = psycopg2.connect( user      = credentials['username']
                                        , password  = credentials['password']
                                        , host      = credentials['host'    ]
                                        , port      = credentials['port'    ]
                                        , database  = credentials['database'])
            print('Conectado')

        except Exception as ex:

            print("Error during DB connection. Error: {}".format(str(ex)))
    

     

    def close_connection(self, cursor, connection):

        cursor.close()

        connection.close()

        print("Connection with database is now closed.")

        return True


