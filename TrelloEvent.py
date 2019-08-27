class TrelloEvent:
    def __init__(self,subject,assignment,dueDate,completed,trelloId):
        self.subject = subject
        self.assignment = assignment
        self.dueDate = dueDate
        self.completed = completed
        self.trelloId = trelloId
        self.__onGoogle = False
    
    def getColor(self):
        if(self.completed):
            return True
        return False
    
    def foundOnGoogle(self):
        self.__onGoogle = True
    
    def isOnGoogle(self):
        return self.__onGoogle