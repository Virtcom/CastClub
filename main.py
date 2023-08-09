from modules import game
import time
import socket
import hashlib
import pygame
import _thread
import sys

def start_game():
    print("Autentivizierung korrect")
    print("User wird weitergeleitet")
    walk="left"
    frames=1
    spr=1
    nachricht = "begingame;"
    white = [255, 255, 255]
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Backpackmon")
    spielaktiv = True
    #player = pygame.image.load("gameneeds/p1.png").convert()
    #player.set_colorkey((0, 0, 0))
    #player_big = pygame.transform.scale(player, (60, 60))

    y= 10
    x= 10
    while spielaktiv:
        Owalk=walk
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            x -= 4
            walk="left"
        elif keypressed[pygame.K_RIGHT]:
            x += 4
            walk="right"
        elif keypressed[pygame.K_UP]:
            y -= 4
            walk="up"
        elif keypressed[pygame.K_DOWN]:
            y += 4
            walk="down"
        else:
            walk="stand"
        if Owalk==walk:
            frames+=1
        else:
            frames=1
        if frames<=5:
            spr=1
        elif frames<=10:
            spr=2
        elif frames<=15:
            spr=3
        elif frames<=20:
            spr=4
        else:
            frames=1
            frames=1
        player = pygame.image.load("gameneeds/walk_" + walk + "/" + str(spr) + ".png").convert_alpha()
        #player.set_colorkey((0, 0, 0))
        player_big = pygame.transform.scale(player, (60, 60))
        screen.fill("white")
        screen.blit(player_big, (x, y))
        clock.tick(60)
    pygame.quit()
    sys.exit()


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

