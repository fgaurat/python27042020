from pprint import pprint
import requests
from Todo import Todo
if __name__ == "__main__":
   todos = []
   r = requests.get('http://ns349423.ip-94-23-40.eu:54413/todos')
   data_json =r.json()

   for value in data_json:
      if 'userId' in value:
         del value['userId']
      t = Todo(**value)
      todos.append({"k":t.id,"todo":t})
   


   for todo in todos:
      t = str(todo)
      print(t)