import socket

loginuser="""
print("Username:")
username = input("==> ")
nachricht = "loggin;" + username
s.send(nachricht.encode())
"""

logginpasswort="""
print("Username Correct")
print("Password:")
password = input("==> ")
nachricht = "checkpass;" + username + ";" + hashlib.md5(bytes(password, "utf-8")).hexdigest()
#print(str(nachricht))
s.send(nachricht.encode())
"""

entering_game="""
s.close()
start_game()
"""