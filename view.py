import pygame
import sys

BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
MENU_BACKGROUND_COLOR = (183, 20, 20)


class TButton:
    def __init__(self, color, width, height, text, textcolor, textsize, coords):
        self.font = pygame.font.SysFont(None, textsize)
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = coords
        self.image = self.font.render(text, 1, textcolor, color)
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect_image)


class TMenu:
    def __init__(self):
        color = MENU_BACKGROUND_COLOR
        width, height = 2000, 90
        textcolor = TEXT_COLOR
        textsize = 70
        self.start_button = TButton(color, width, height, 'Start', textcolor, textsize, (600, 300))
        self.quit_button = TButton(color, width, height, 'Quit', textcolor, textsize, (600, 400))

    def draw(self, surf):
        self.start_button.draw(surf)
        self.quit_button.draw(surf)

    def action(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos):
            return False
        if self.quit_button.rect.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()


class TText:
    def __init__(self, text, color, coords, size=42):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, size)
        self.image = self.font.render(str(self.text), 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class TTime:
    def __init__(self, msec):
        self.seconds = int(msec / 1000)
        self.minutes = int(self.seconds / 60)
        self.hours = int(self.minutes / 60)
        self.seconds %= 60
        self.minutes %= 60
        self.hours %= 24
        if self.seconds < 10:
            self.seconds = '0' + str(self.seconds)
        if self.minutes < 10:
            self.minutes = '0' + str(self.minutes)
        if self.hours < 10:
            self.hours = '0' + str(self.hours)
        self.time = 'Time: ' + str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)

    def time_text(self):
        time_text = TText(self.time, TEXT_COLOR, (1000, 300))
        return time_text
