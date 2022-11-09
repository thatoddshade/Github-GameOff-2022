import pygame

# settings
WIDTH = 1024
HEIGHT = 640

BACKGROUND_COLOUR = "#131313"
BORDER_COLOUR = "#ffffff"

MAP_WIDTH = WIDTH
MAP_HEIGHT = WIDTH / 2
MAP_X = 0
MAP_Y = HEIGHT / 12

COUNTRY_DATA = {
    "america": {"food": "donut", "min_coords": (11, 13), "max_coords": (87, 68)},
    "europe": {"food": "bread", "min_coords": (121, 18), "max_coords": (152, 35)},
    "africa": {"food": "bread", "min_coords": (113, 38), "max_coords": (163, 87)},
    "asia": {"food": "spaghetti", "min_coords": (160, 16), "max_coords": (245, 55)},
}

# window setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cliché')

# custom mouse pointer
surf = pygame.image.load('data/images/cursor.png').convert_alpha()
cursor = pygame.cursors.Cursor((0, 0), surf)
pygame.mouse.set_cursor(cursor)

# resource loading
map = pygame.image.load("data/images/map.png")

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # displaying things on screen
    screen.fill(BACKGROUND_COLOUR)
    screen.blit(pygame.transform.scale(map, (MAP_WIDTH, MAP_HEIGHT)), (MAP_X, MAP_Y))

    for country in COUNTRY_DATA:
        country_min_x = COUNTRY_DATA[country]["min_coords"][0] * 4
        country_min_y = COUNTRY_DATA[country]["min_coords"][1] * 4

        country_max_x = COUNTRY_DATA[country]["max_coords"][0] * 4
        country_max_y = COUNTRY_DATA[country]["max_coords"][1] * 4

        if mouse_pos[0] - MAP_X > country_min_x and mouse_pos[1] - MAP_Y > country_min_y:
            if mouse_pos[0] - MAP_X < country_max_x and mouse_pos[1] - MAP_Y < country_max_y:
                # draw a rectangle around the selected country
                country_width = (COUNTRY_DATA[country]["max_coords"][0] - COUNTRY_DATA[country]["min_coords"][0]) * 4
                country_height = (COUNTRY_DATA[country]["max_coords"][1] - COUNTRY_DATA[country]["min_coords"][1]) * 4

                border = pygame.Rect(
                    country_min_x + MAP_X,
                    country_min_y + MAP_Y,
                    country_width,
                    country_height
                )
                pygame.draw.rect(screen, BORDER_COLOUR, border, 4, 15)


    pygame.display.update()

pygame.quit()
quit()