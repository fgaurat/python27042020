import argparse
import configparser
from pprint import pprint
import mysql.connector

if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()
        parser = argparse.ArgumentParser(description='Extract Todos from MySQL.')

        parser.add_argument("--config",metavar='config_file', type=str, help="Configuration file (INI)",required=True)
        args = parser.parse_args()
        # print(args.config)
        config.read(args.config)
        print(config['MySQL']['host'])

        cnx = mysql.connector.connect(**config['MySQL'])
        cursor = cnx.cursor()
        query = "SELECT * FROM `paris-form-1200`"
        cursor.execute(query)
        for todo in cursor:
            pprint(todo)

        cnx.close()    
    except Exception as e:
        print(e)