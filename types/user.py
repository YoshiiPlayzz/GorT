class User:
    username = ""
    permissions = []
    password =""
    def __init__(self, username, password, permissions=[]) -> None:
        print(f"User with name {username}")
        
    def username(self) -> str:
        return self.username

    def has_permission(self, permission) -> bool:
        return permission in self.permissions