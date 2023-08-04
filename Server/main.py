from  modules import login
import time
import socket
import os
import _thread
import hashlib

def Netcheck():
    s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try :
        s.connect(("255.255.255.0", 80))
        ip = s.getsockname()[0]
        s.close()
        global IPadresse
        IPadresse = ip
        print("Online on:")
        print(ip)
    except:
        print("No Internet connection")
    
Netcheck()
users=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 25565))
s.listen(1)
def get_connection(threadnummer):
    print("Thread Nummer {} wird benutzt(Port 25565)".format(str(threadnummer)))
    try:
        while True:
            time.sleep(0.2)
            komm, addr = s.accept()
            nwthnumber=threadnummer + 1
            _thread.start_new_thread(get_connection, (nwthnumber,))
            while True:
                data = komm.recv(4096)
                if not data:
                    komm.close()
                    break
                dat = data.decode().split(";")
                if dat[0] == "checkpass":
                    pfad="Server/users/"+ dat[1] + "/passwort.txt"
                    with open(pfad, "r") as passwordhashdat:
                        passwordhash = passwordhashdat.readlines()
                        #print(str(passwordhash))
                        #print(str(dat[2]))
                        if passwordhash[0] == dat[2]:
                            komm.send(login.entering_game.encode())
                            global users
                            users.append(dat[1])
                if dat[0] == "loggin":
                    checkpath = "Server/users/" + dat[1]
                    exsisting = os.path.exists(checkpath)
                    if exsisting == True:
                        komm.send(login.logginpasswort.encode())
                    else:
                        print("Thread Nummer {} wird geschlossen".format(str(threadnummer)))
                        break
                if dat[0] == "pleaselogin":
                    komm.send(login.loginuser.encode())
                """print("[{}] {}".format(addr[0], data.decode()))
                nachricht= input("Antwort: ")
                komm.send(nachricht.encode())"""
    finally:
        s.close()
i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i.bind(("", 25566))
i.listen(1)
def ingameconnection(threadnummer):
    print("Thread Nummer {} wird benutzt(Port 25566)".format(str(threadnummer)))
    try:
        while True:
            time.sleep(0.2)
            komm, addr = i.accept()
            nwthnumber=threadnummer + 1
            _thread.start_new_thread(ingameconnection, (nwthnumber,))
            while True:
                data = komm.recv(4096)
                if not data:
                    komm.close()
                    break
                dat = data.decode().split(";")
                if dat[0] == "checkpass":
                    pfad="Server/users/"+ dat[1] + "/passwort.txt"
                    with open(pfad, "r") as passwordhashdat:
                        passwordhash = passwordhashdat.readlines()
                        #print(str(passwordhash))
                        #print(str(dat[2]))
                        if passwordhash[0] == dat[2]:
                            komm.send(login.entering_game.encode())
                if dat[0] == "loggin":
                    checkpath = "Server/users/" + dat[1]
                    exsisting = os.path.exists(checkpath)
                    if exsisting == True:
                        komm.send(login.logginpasswort.encode())
                    else:
                        print("Thread Nummer {} wird geschlossen".format(str(threadnummer)))
                        break
                if dat[0] == "pleaselogin":
                    komm.send(login.loginuser.encode())
                """print("[{}] {}".format(addr[0], data.decode()))
                nachricht= input("Antwort: ")
                komm.send(nachricht.encode())"""
    finally:
        i.close()
_thread.start_new_thread(get_connection, (1,))
_thread.start_new_thread(ingameconnection, (1,))
while True:
    pass