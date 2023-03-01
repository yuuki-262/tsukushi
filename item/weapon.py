from item.base.item import item
from const.const import *
from character.player import player

class weapon(item):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.type = type
        self.is_delete = False

    def get(self):
        pass

    def get_img(self, player :player):
            return dir_img_item + player.attack_values[self.type]  + "メダル" + png
