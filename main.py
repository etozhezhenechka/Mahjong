from view import *
from tiles import *

import random


pygame.init()
BackGround = TBackground('img/background.png', [0, 0])

SCREEN_RESOLUTION = 1200, 700

game_started = False
DISPLAY = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption('Mahjong')
tiles_list = tiles_setup()
tiles_left = 0


def main():
    tiles = create_gamefield()

    tiles_clicked_list = []
    menu_on = True
    menu = TMenu()
    start_time = pygame.time.get_ticks()
    while True:
        DISPLAY.fill([255, 255, 255])
        DISPLAY.blit(BackGround.image, BackGround.rect)
        mouse_pos = 0, 0
        time_passed = pygame.time.get_ticks() - start_time
        shuffle_button = TButton(MENU_BACKGROUND_COLOR, 500, 100, 'SHUFFLE', TEXT_COLOR, 42, (1000, 400))
        if menu_on:
            menu.draw(DISPLAY)
        else:
            draw_tiles(tiles, DISPLAY)
            draw_info(time_passed, tiles)
            shuffle_button.draw(DISPLAY)
        for event in pygame.event.get():
            if event.type == 12:
                # QUIT
                pygame.quit()
                sys.exit()
            elif event.type == 6:
                # MOUSE_UP
                mouse_pos = event.pos
                if menu_on:
                    menu_on = menu.action(mouse_pos)

        if not menu_on and shuffle_button.rect.collidepoint(mouse_pos):
            shuffle_board(tiles)

        is_tile_clicked(mouse_pos, tiles, tiles_clicked_list)
        if len(tiles_clicked_list) == 2:
            if tiles_comparison(tiles_clicked_list[0], tiles_clicked_list[1], tiles):
                global tiles_left
                tiles_left -= 2
            tiles_clicked_list = []
        pygame.display.update()


def is_tile_clicked(mouse_pos, tiles, tiles_clicked_list):
    global game_started
    for tile in tiles:
        if tile.rect.collidepoint(mouse_pos):
            if not tile.is_locked(tiles):
                tile.on_click()
                pygame.mixer.music.load('sound/click.wav')
                pygame.mixer.music.play()
                game_started = True
                if tile.is_chosen():
                    tiles_clicked_list.append(tile)
                else:
                    if tile in tiles_clicked_list:
                        tiles_clicked_list.remove(tile)
            else:
                if game_started:
                    pygame.mixer.music.load('sound/wrong.wav')
                    pygame.mixer.music.play()


def tiles_comparison(t1, t2, tiles):
    if t1.name == t2.name:
        pygame.mixer.music.load('sound/match.wav')
        pygame.mixer.music.play()
        tiles.remove(t1)
        tiles.remove(t2)
        return True
    else:
        t1.on_click()
        t2.on_click()


def draw_tiles(tiles, surface):
    for tile in tiles:
        surface.blit(tile.image, tile.rect)


def create_gamefield():
    local_tiles = []
    global tiles_list
    global tiles_left

    for i in range(0, 8):
        for j in range(0, 15):
            r_index = random.randrange(len(tiles_list))
            tile = tiles_list.pop(r_index)

            tile.rect.x = tile.rect.width + j * tile.rect.width
            tile.rect.y = tile.rect.height + i * tile.rect.height
            local_tiles.append(tile)

            tiles_left += 1

    for i in range(0, 4):
        for j in range(0, 6):
            r_index = random.randrange(len(tiles_list))
            tile = tiles_list.pop(r_index)
            tile.layer = 1

            tile.rect.x = (tile.rect.width * 5 + 3) + j * tile.rect.width
            tile.rect.y = (tile.rect.height * 3 + 5) + i * tile.rect.height
            local_tiles.append(tile)

            tiles_left += 1
    return local_tiles


def draw_info(time_passed, tiles):
    global tiles_left
    left_str = 'Tiles left: ' + str(tiles_left) + '/144'
    tiles_left_text = TText(left_str, TEXT_COLOR, (1000, 100))
    tiles_left_text.draw(DISPLAY)
    timer = TTime(time_passed)
    timer_text = timer.time_text()
    timer_text.draw(DISPLAY)
    pairs_str = 'Pairs available: ' + str(pairs_counting(tiles))
    pairs_avail_text = TText(pairs_str, TEXT_COLOR, (1000, 200))
    pairs_avail_text.draw(DISPLAY)


if __name__ == '__main__':
    main()
