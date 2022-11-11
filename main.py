import random
import pygame
import ui
from settings import *

# window setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# custom mouse pointer
cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
pygame.mouse.set_cursor(cursor)

# resource loading
font = pygame.font.Font("data/font.ttf", FONT_SIZE)
map = pygame.image.load("data/images/map.png")

# values
score = 0

# continent
selectioned_continent = False
selectioned_continent_name = "north_america"

# food
current_food = random.choice(list(FOOD_DATA.keys()))
def change_food():
    global current_food
    current_food = random.choice(list(FOOD_DATA.keys()))

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                change_food()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selectioned_continent:
                if current_food in CONTINENT_DATA[selectioned_continent_name]["food"]:
                    score += random.randint(MIN_SCORE_GAIN, MAX_SCORE_GAIN)
                else:
                    score -= random.randint(MIN_SCORE_GAIN, MAX_SCORE_GAIN)
                change_food()
                print(f"dropping {current_food.capitalize()} in {selectioned_continent_name.capitalize()} !!!!!!!")

    # updating and displaying things on screen

    # fixing score
    if score < 0:
        score = 0

    # fill screen with background colour
    screen.fill(BACKGROUND_COLOUR)

    # show world map
    screen.blit(pygame.transform.scale(map, (MAP_WIDTH, MAP_HEIGHT)), (MAP_X, MAP_Y))

    # draw score bar
    ui.display_score_bar(screen, SCORE_X, SCORE_Y, SCORE_WIDTH, SCORE_HEIGHT, SCORE_COLOUR, BORDER_COLOUR, BORDER_WIDTH, RECT_ROUNDNESS, score)

    # display random food
    food_img = pygame.image.load(f"data/images/food/{current_food}.png")
    food_size = (food_img.get_width() * 2, food_img.get_height() * 2)
    food_img = pygame.transform.scale(food_img, food_size)
    screen.blit(food_img, mouse_pos)

    selectioned_continent = False
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

                # update variables
                selectioned_continent = True
                selectioned_continent_name = continent
                break


    pygame.display.update()

pygame.quit()
quit()
