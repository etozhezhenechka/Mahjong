from view import *

pygame.init()

SCREEN_RESOLUTION = 1200, 800

DISPLAY = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption('Mahjong')


def main():
    menu_on = True
    menu = Menu()
    while True:
        DISPLAY.fill(BACKGROUND)
        if menu_on:
            menu.draw(DISPLAY)
        pygame.display.update()


if __name__ == '__main__':
    main()