import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("GIF-Test")
filelist=["test_gif/1.png", "test_gif/2.png", "test_gif/3.png"]
while True:
    for i in filelist:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player = pygame.image.load(i).convert()
        player.set_colorkey((0, 0, 0))
        player_big = pygame.transform.scale(player, (160, 160))
        screen.fill("white")
        screen.blit(player_big, (20, 20))
        clock.tick(10)
        pygame.display.update()