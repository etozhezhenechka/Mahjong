from view import *

pygame.init()

SCREEN_RESOLUTION = 1200, 800

DISPLAY = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption('Mahjong')


def main():
    menu_on = True
    menu = Menu()
    tiles_left = 144
    start_time = pygame.time.get_ticks()
    while True:
        DISPLAY.fill(BACKGROUND)
        time_passed = pygame.time.get_ticks() - start_time
        if menu_on:
            start_time = pygame.time.get_ticks()
            menu.draw(DISPLAY)
        else:
            left_str = 'Tiles left: ' + str(tiles_left) + '/144';
            tiles_left_text = Text(left_str, TEXT_COLOR, (1000, 100))
            tiles_left_text.draw(DISPLAY)
            time_text = show_time(time_passed)
            time_text.draw(DISPLAY)
            pairs_str = 'Pairs available: ' + str(1)
            pairs_avail_text = Text(pairs_str, TEXT_COLOR, (1000, 200))
            pairs_avail_text.draw(DISPLAY)
            shuffle_button = Button(MENU_BACKGROUND, 500, 100, 'SHUFFLE', TEXT_COLOR, 42, (1000, 400))
            shuffle_button.draw(DISPLAY)
        for event in pygame.event.get():
            if event.type == 12: #QUIT
                pygame.quit()
                sys.exit()
            elif event.type == 6: #MOUSE_UP
                mouse_pos = event.pos
                if menu_on:
                    menu_on = menu.action(mouse_pos)
        pygame.display.update()


if __name__ == '__main__':
    main()