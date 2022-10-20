from inspect import isclass, issubclass

class Action: 
    def __init__(self, path="/"):
        self.path = path
    
    def get_action(self) -> str:
        return self.path
    
    def do_action(self, *args):
        pass 

def isAction(clazz):
    return type(clazz) is Action

