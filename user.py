class User:
 
    def __init__(self, username="", password="", permissions=[]):
        self.username = username
        self.password = password
        self.permissions = permissions
        print(f"User with name {username}")
        

    def has_permission(self, permission) -> bool:
        return permission in self.permissions