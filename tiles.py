import pygame


class Tile (pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.name = file.rstrip('.png')
        self.image = pygame.image.load('img/' + file).convert()
        self.rect = self.image.get_rect()
        self.clicked = False

    def is_chosen(self):
        return self.clicked

    def on_click(self):
        self.clicked = not self.clicked

    def is_locked(self, tiles):
        locked = False

        for tile in tiles:
            if self.rect.y == tile.rect.y:
                if (
                    self.rect.x + self.rect.width == tile.rect.x and
                    self.rect.x == tile.rect.x + tile.rect.width
                   ):
                    locked = True

        return locked


def tiles_setup():
    # reading tiles from file here
    tiles_list = []
    return tiles_list

def shuffle():
    # shuffling tiles function

def pairs_counting(tiles):
    pairs_dict = {}
    count_pairs = 0
