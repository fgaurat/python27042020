import time
import json
from pprint import pprint

if __name__ == "__main__":
    todos = [
        {"id":1,"title":"Todo1","dueDate":int(time.time()),"done":False},
        {"id":2,"title":"Todo2","dueDate":int(time.time()),"done":True},
        {"id":3,"title":"Todo3","dueDate":int(time.time()),"done":False},
    ]

    print(json.dumps(todos))
    with open("todos.json","w") as f:    
        f.write(json.dumps(todos))  

    data =None
    with open("todos.json","r") as f:
        data = json.load(f)
    

    pprint(data[0]["title"])

