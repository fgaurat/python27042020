class Todo:


    def __init__(self,id,title,dueDate,completed):
        self.id = id
        self.title = title
        self.dueDate = dueDate
        self.completed = completed

    def __str__(self):
        return "[{}] {} : {}".format(self.id,self.title,self.completed)
        