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
        mouse_pos = 0, 0
        if menu_on:
            menu.draw(DISPLAY)
        for event in pygame.event.get():
            if event.type == 12:# QUIT
                pygame.quit()
                sys.exit()
            elif event.type == 6: # MOUSE_UP
                mouse_pos = event.pos
                if(menu_on):
                    menu_on = menu.action(mouse_pos)


        pygame.display.update()


if __name__ == '__main__':
    main()