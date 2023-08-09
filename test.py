import pygame
import pytmx

# Farben
white = (255, 255, 255)

# Initialisiere pygame
pygame.init()

# Karten-Setup
# Fenster-Setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scrolling Map Example")
clock = pygame.time.Clock()

player_rect = pygame.Rect(50, 50, 30, 30)  # Spieler-Rechteck
scroll_x = 0
scroll_y = 0

tmx_map = pytmx.load_pygame("test.tmx")
tile_size = tmx_map.tilewidth, tmx_map.tileheight
map_width = tmx_map.width * tile_size[0]
map_height = tmx_map.height * tile_size[1]


def draw_map():
    for layer in tmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_map.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tile_size[0] - scroll_x, y * tile_size[1] - scroll_y))

def check_collision(rect, tiles):
    for tile in tiles:
        if rect.colliderect(tile):
            return True
    return False

def main():
    global scroll_x, scroll_y, player_rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        key_pressed = pygame.key.get_pressed()

        # Bewegung des Spielers verarbeiten
        new_player_rect = player_rect.copy()
        if key_pressed[pygame.K_LEFT]:
            new_player_rect.x -= 5
        elif key_pressed[pygame.K_RIGHT]:
            new_player_rect.x += 5
        elif key_pressed[pygame.K_UP]:
            new_player_rect.y -= 5
        elif key_pressed[pygame.K_DOWN]:
            new_player_rect.y += 5

        # Kollisionsabfrage mit Kacheln
        colliding_tiles = []
        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile_rect = pygame.Rect(x * tile_size[0] - scroll_x, y * tile_size[1] - scroll_y, tile_size[0], tile_size[1])
                    if new_player_rect.colliderect(tile_rect):
                        colliding_tiles.append(tile_rect)

        # Wenn keine Kollision, Spieler bewegen
        if not check_collision(new_player_rect, colliding_tiles):
            player_rect = new_player_rect

        # Scrollen der Karte
        scroll_x = max(0, min(player_rect.x - screen_width // 2, map_width - screen_width))
        scroll_y = max(0, min(player_rect.y - screen_height // 2, map_height - screen_height))

        screen.fill(white)
        draw_map()
        pygame.draw.rect(screen, (255, 0, 0), (player_rect.x - scroll_x, player_rect.y - scroll_y, player_rect.width, player_rect.height))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
