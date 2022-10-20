from actions.action import Action

class Login(Action):
    def __init__(self):
        super().__init__(path="/login")
        
    
    def get_action(self) -> str:

        return super().get_action()

    def do_action(self, *args):
        print(f"User '{args[0]}' try to login with password '{args[1]}'")