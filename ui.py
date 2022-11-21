import pygame
from settings import TIME_X, TIME_Y

def display_bar(screen, x, y, width, height, colour, border_colour, border_width, radius=0, score=0):
    # draw score bar
    score_rect = pygame.Rect(
        x,
        y,
        (score / 100) * width,
        height
    )
    pygame.draw.rect(screen, colour, score_rect, border_radius=radius)

    # draw score border
    score_border = pygame.Rect(
        x,
        y,
        width,
        height
    )
    pygame.draw.rect(screen, border_colour, score_border, border_width, radius)

def write_continent_name(screen, font, continent_name, text_colour):
    # write a text indicating the selected continent name
    text = font.render(continent_name.capitalize().replace("_", " "), False, text_colour)
    screen.blit(text, text.get_rect())


def write_time(screen, font, time, text_colour):
    # write a text indicating the selected continent name
    text = font.render("Seconds : " + str(time).capitalize(), False, text_colour)
    screen.blit(text, (TIME_X, TIME_Y, text.get_width(), text.get_height()))
