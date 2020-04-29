import argparse
import configparser
from pprint import pprint
import mysql.connector
import requests

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
        
        r = requests.get('http://ns349423.ip-94-23-40.eu:54413/todos')
        data_json =r.json()

        for d in data_json:
            completed = 1 if d['completed'] == 'True' else 0
            sql = ("INSERT INTO `paris-form-1200` (`title`, `done`, `due_date`) " 
                    "VALUES ('{}', '{}', '{}')".format(d['title'],completed,int(d['dueDate']/1000)) )
            print(sql)
            cursor.execute(sql)
        cnx.commit()


    # completed == 'True'?1:0



        query = "SELECT * FROM `paris-form-1200`"
        cursor.execute(query)
        for todo in cursor:
            pprint(todo)

        cnx.close()    
    except Exception as e:
        print(e)