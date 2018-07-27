import pygame, random


class TTile (pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.name = file.rstrip('.png')
        self.image = pygame.image.load('img/' + file).convert()
        self.rect = self.image.get_rect()
        self.clicked = False
        self.layer = 0

    def is_chosen(self):
        return self.clicked

    def on_click(self):
        self.clicked = not self.clicked
        if self.clicked:
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)

    def is_locked(self, tiles):
        left_block = False
        right_block = False

        for tile in tiles:
            if self.rect.y == tile.rect.y:
                if self.rect.x + self.rect.width == tile.rect.x:
                    right_block = True
                if self.rect.x == tile.rect.x + tile.rect.width:
                    left_block = True

        return left_block and right_block

    def swap(self, tile):
        self.name,  tile.name  = tile.name,  self.name
        self.image, tile.image = tile.image, self.image
        self.layer, tile.layer = tile.layer, self.layer


def tiles_setup():
    img_list = [
                 "b1.png", "b2.png", "b3.png", "b4.png", "b5.png", "b6.png", "b7.png", "b8.png", "b9.png",
                 "c1.png", "c2.png", "c3.png", "c4.png", "c5.png", "c6.png", "c7.png", "c8.png", "c9.png",
                 "p1.png", "p2.png", "p3.png", "p4.png", "p5.png", "p6.png", "p7.png", "p8.png", "p9.png",
                 "w1.png", "w2.png", "w3.png", "w4.png", "d1.png", "d2.png", "d3.png",
                 "f1.png", "f2.png", "f3.png", "f4.png", "s1.png", "s2.png", "s3.png", "s4.png"
               ]
    tiles_list = []

    for i in range(len(img_list)):
        for j in range(0, 4):
            tile = TTile(img_list[i])
            tiles_list.append(tile)

    return tiles_list


def shuffle():
    emptyhere = 1
    # shuffling tiles function


def pairs_counting(tiles):
    pairs_dict = {}
    count_pairs = 0
    for tile in tiles:
        if not tile.is_locked(tiles):
            if tile.name not in pairs_dict.keys():
                pairs_dict[tile.name] = 0
            pairs_dict[tile.name] += 1
            if pairs_dict[tile.name] == 2:
                count_pairs += 1

    return count_pairs


def shuffle_board(tiles):
    tiles_iter = iter(tiles)
    for i in range(len(tiles)):
        r_index = random.randrange(len(tiles))
        tile = tiles[r_index]
        tile.swap(next(tiles_iter))






