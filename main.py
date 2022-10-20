from dotenv import load_dotenv
import actions.action  as action
from actions.login import Login


import webserver
import user 

if __name__ == "__main__":
    load_dotenv()
    print("GorT v1.0") 
    user = user.User(username="test", password="test", permissions=[])
    print(user.permissions)
    
    webserver.runServer(host_name="localhost", port=1235)


