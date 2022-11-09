import pygame, ui

# settings
WIDTH = 1024
HEIGHT = 640
TITLE = "Cliché"

BORDER_WIDTH = 4
RECT_ROUNDNESS = 15

BACKGROUND_COLOUR = "#0e071b"
BORDER_COLOUR = "#ffeb57"
TEXT_COLOUR = "#edab50"
SCORE_COLOUR = "#5ac54f"

MAP_X = 0
MAP_Y = HEIGHT / 12
MAP_WIDTH = WIDTH
MAP_HEIGHT = WIDTH / 2

SCORE_X = MAP_Y * 2
SCORE_Y = MAP_Y / 8
SCORE_WIDTH = WIDTH - MAP_Y * 2
SCORE_HEIGHT = MAP_Y / 1.25

CONTINENT_DATA = {
    "america": {"food": ["donut"], "min_coords": (11, 13), "max_coords": (87, 68)},
    "europe": {"food": ["bread"], "min_coords": (121, 18), "max_coords": (152, 35)},
    "africa": {"food": ["human"], "min_coords": (113, 38), "max_coords": (163, 87)},
    "asia": {"food": ["rice"], "min_coords": (160, 16), "max_coords": (245, 55)},
    "australia": {"food": ["spaghetti"], "min_coords": (202, 71), "max_coords": (239, 94)},
    "antarctica": {"food": ["spaghetti"], "min_coords": (0, 112), "max_coords": (256, 128)}
}

# window setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# custom mouse pointer
surf = pygame.image.load('data/images/cursor.png').convert_alpha()
cursor = pygame.cursors.Cursor((0, 0), surf)
pygame.mouse.set_cursor(cursor)

# resource loading
font = pygame.font.Font("data/font.ttf", 16)
map = pygame.image.load("data/images/map.png")

# values
score = 25

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

    for continent in CONTINENT_DATA:
        continent_min_x = CONTINENT_DATA[continent]["min_coords"][0] * 4
        continent_min_y = CONTINENT_DATA[continent]["min_coords"][1] * 4

        continent_max_x = CONTINENT_DATA[continent]["max_coords"][0] * 4
        continent_max_y = CONTINENT_DATA[continent]["max_coords"][1] * 4

        continent_width = (CONTINENT_DATA[continent]["max_coords"][0] - CONTINENT_DATA[continent]["min_coords"][0]) * 4
        continent_height = (CONTINENT_DATA[continent]["max_coords"][1] - CONTINENT_DATA[continent]["min_coords"][1]) * 4

        # if player is hovering a continent
        if mouse_pos[0] - MAP_X > continent_min_x and mouse_pos[1] - MAP_Y > continent_min_y:
            if mouse_pos[0] - MAP_X < continent_max_x and mouse_pos[1] - MAP_Y < continent_max_y:
                # draw a rectangle around the selected continent

                border = pygame.Rect(
                    continent_min_x + MAP_X,
                    continent_min_y + MAP_Y,
                    continent_width,
                    continent_height
                )
                pygame.draw.rect(screen, BORDER_COLOUR, border, BORDER_WIDTH, RECT_ROUNDNESS)

                # write a text indicating the selected continent name
                ui.write_continent_name(screen, font, continent, TEXT_COLOUR)
                break

    # draw score bar
    ui.display_score_bar(screen, SCORE_X, SCORE_Y, SCORE_WIDTH, SCORE_HEIGHT, SCORE_COLOUR, TEXT_COLOUR, BORDER_WIDTH, RECT_ROUNDNESS, score)

    pygame.display.update()

pygame.quit()
quit()
