from item.base.item import item
from const.const import *
from character.player import player

class weapon(item):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.type = type
        self.is_del = False

    def get(self):
        pass

    def get_img(self, player :player):
            return dir_img_item + player.attack_values[self.type]  + "メダル" + png
