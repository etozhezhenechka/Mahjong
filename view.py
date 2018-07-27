import pygame
import sys

BACKGROUND = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
MENU_BACKGROUND = (183, 20, 20)


class Button:
    def __init__(self, color, width, height, text, textcolor, textsize, coords):
        self.font = pygame.font.SysFont(None, textsize)
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = coords
        self.image = self.font.render(text, 1, textcolor, color)
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect_image)


class Menu:
    def __init__(self):
        color = MENU_BACKGROUND
        width, height = 2000, 90
        textcolor = TEXT_COLOR
        textsize = 70
        self.start_button = Button(color, width, height, 'Start', textcolor, textsize, (600, 300))
        self.quit_button = Button(color, width, height, 'Quit', textcolor, textsize, (600, 400))

    def draw(self, surf):
        self.start_button.draw(surf)
        self.quit_button.draw(surf)

    def action(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos):
            return False
        if self.quit_button.rect.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()


class Text:
    def __init__(self, text, color, coords, size=42):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, size)
        self.image = self.font.render(str(self.text), 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def show_time(msec):
    seconds = int(msec / 1000)
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    seconds %= 60
    minutes %= 60
    hours %= 24
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    time = 'Time: ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)
    time_text = Text(time, TEXT_COLOR, (1000, 300))
    return time_text