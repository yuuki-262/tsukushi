from item.base.item import item
from const.const import *
from character.player import player

class weapon(item):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.img_width = 50
        self.img_height = 50
        self.hit_width = 50
        self.hit_height = 50
        self.count = 0
        self.type = type
        self.is_del = False

    def get(self, player):
        if player.attack_values[self.type] == "火":
            #player.mp = 100
            player.attack_type = 0
        elif player.attack_values[self.type] == "雷":
            #player.mp = 100
            player.attack_type = 1
        elif player.attack_values[self.type] == "風":
            #player.mp = 100
            player.attack_type = 2
        self.is_del = True

    def get_img(self, player :player):
        return wepon_img_index_up[player.attack_values[self.type]]

    def state(self):
        self.count += 1
        if self.count > 600:
            self.is_del = True

    def check_flash(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (self.count < 420 or self.count % 20 // 10 == 0)