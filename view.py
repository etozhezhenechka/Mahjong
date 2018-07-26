import pygame

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