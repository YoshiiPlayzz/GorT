from dotenv import load_dotenv
import sys

import user 

if __name__ == "__main__":
    load_dotenv()
    print("GorT v1.0") 
    user = user.User(username="test", password="test", permissions=[])
    print(user.permissions)

