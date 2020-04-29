import time
import json
from pprint import pprint
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('http://ns349423.ip-94-23-40.eu:54413/todos') as f:
        data_txt = f.read()
        data = json.loads(data_txt)

        pprint(data)
        print(data[0]['title'])