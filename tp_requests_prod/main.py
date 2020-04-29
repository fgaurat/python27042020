from pprint import pprint
import requests

if __name__ == "__main__":
   r = requests.get('http://ns349423.ip-94-23-40.eu:54413/todos')
   data_json =r.json()
   pprint(data_json)