from item.base.item import item
from const.const import *
from character.player import player

class heal_item(item):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.img_width = 50
        self.img_height = 50
        self.hit_width = 50
        self.hit_height = 50
        self.count = 0
        self.type = onigiri_type[type]
        self.is_del = False

    def get(self, player: player):
        if self.type == "onigiri":
            player.hp.change_hp(10)
        elif self.type == "shine":
            player.hp.change_hp(50)
        elif self.type == "baked":
            player.hp.change_hp(20)
        self.is_del = True

    def get_img(self, player :player):
        return onigiri_index_fire_up[self.type]

    def state(self):
        self.count += 1
        if self.count > 600:
            self.is_del = True

    def check_flash(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (self.count < 420 or self.count % 20 // 10 == 0)