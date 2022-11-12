import random
import pygame
import food
import ui
import time
import math
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
end_screen = pygame.transform.scale(pygame.image.load(
    "data/images/end_screen.png"), (WIDTH, HEIGHT))

# values
score = 0
start_time = time.time()
current_time = math.floor(time.time() - start_time)

# green filling
greening = 0

# shaking
x_map_offset = 0
y_map_offset = 0
shaking = 0

# continent
selected_continent = False
selected_continent_name = "north_america"

# food
current_food = random.choice(list(FOOD_DATA.keys()))
def change_food():
    global current_food
    current_food = random.choice(list(FOOD_DATA.keys()))

falling_food = []


clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not score > 100:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_continent:
                    if current_food in CONTINENT_DATA[selected_continent_name]["food"]:
                        score += random.randint(MIN_SCORE_GAIN, MAX_SCORE_GAIN)
                        greening += 15
                    else:
                        score -= random.randint(MIN_SCORE_GAIN, MAX_SCORE_GAIN)
                        shaking += 15
                    falling_food.append(food.FallingFood(mouse_pos[0], mouse_pos[1], current_food))
                    change_food()
                    pygame.mouse.set_pos(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                    
                    sound = pygame.mixer.Sound(random.choice(SOUNDS["food_drop"]))
                    pygame.mixer.Sound.play(sound)

        # updating and displaying things on screen
    if not score > 100:
        # fix score
        if score < 0:
            score = 0

        # fill screen with background colour
        screen.fill(BACKGROUND_COLOUR)

        # show world map
        if shaking > 0:
            shaking -= 1
            x_map_offset = random.randint(int(SHAKING_VALUE / -1), SHAKING_VALUE)
            y_map_offset = random.randint(int(SHAKING_VALUE / -1), SHAKING_VALUE)

        screen.blit(pygame.transform.scale(map, (MAP_WIDTH, MAP_HEIGHT)), (MAP_X + x_map_offset, MAP_Y + y_map_offset))
        x_map_offset, y_map_offset = (0, 0)

        # draw score bar
        ui.display_bar(screen, SCORE_X, SCORE_Y, SCORE_WIDTH, SCORE_HEIGHT, SCORE_COLOUR, BORDER_COLOUR, BORDER_WIDTH, RECT_ROUNDNESS, score)
        
        # update timer
        current_time = math.floor(time.time() - start_time)

        # display random food
        food_img = pygame.image.load(f"data/images/food/{current_food}.png")
        food_size = (food_img.get_width() * 2, food_img.get_height() * 2)
        food_img = pygame.transform.scale(food_img, food_size)
        screen.blit(food_img, mouse_pos)

        # update continent values
        selected_continent = False
        for continent in CONTINENT_DATA:
            continent_min_x = CONTINENT_DATA[continent]["min_coords"][0] * 4
            continent_min_y = CONTINENT_DATA[continent]["min_coords"][1] * 4

            continent_max_x = CONTINENT_DATA[continent]["max_coords"][0] * 4
            continent_max_y = CONTINENT_DATA[continent]["max_coords"][1] * 4

            continent_width = (CONTINENT_DATA[continent]["max_coords"][0] - CONTINENT_DATA[continent]["min_coords"][0]) * 4
            continent_height = (CONTINENT_DATA[continent]["max_coords"][1] - CONTINENT_DATA[continent]["min_coords"][1]) * 4

            # check if player is selecting a continent
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
                    selected_continent = True
                    selected_continent_name = continent
                    break
            
            # update food
            
            # kill fallen food
        for i in range(len(falling_food) - 1):
            f = falling_food[i]
            if pygame.time.get_ticks() - f.drop_time >= f.falling_time:
                del falling_food[i]
        
        # apply food falling animation
        for f in falling_food:
            f.trans()
            screen.blit(f.image, f.position)
        
            if greening > 0:
                greening -= 1
                green_surf = pygame.Surface((WIDTH, HEIGHT))
                green_surf.set_alpha(75)
                green_surf.fill("green")
                screen.blit(green_surf, (0, 0))
            

    elif score > 100:
        screen.blit(end_screen, (0, 0))
    
    ui.write_time(screen, font, current_time, TEXT_COLOUR)

    clock.tick(60)
    pygame.display.update()

pygame.quit()
quit()
