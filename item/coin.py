from item.base.item import item
from const.const import *
from character.player import player
from util.game_util import sound_se

class heal_item(item):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.r = 40
        self.angle = 0
        self.img_width = 50
        self.img_height = 50
        self.hit_width = 50
        self.hit_height = 50
        self.count = 0
        self.type = onigiri_type[type]
        self.is_del = False

    def get(self, pygame, player: player):
        if self.type == "onigiri":
            player.hp.change_hp(10)
        elif self.type == "shine":
            player.hp.change_hp(50)
        elif self.type == "baked":
            player.hp.change_hp(20)
            player.is_auto_heal = True
            player.auto_heal_count = 0
            player.auto_heal_limit = 20

        sound_se(pygame, dir_SE + "Heal.wav")
        self.is_del = True

    def get_img(self, player :player):
        return onigiri_img_index[self.type]

    def state(self):
        self.count += 1
        if self.count > 600:
            self.is_del = True

    def check_flash(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (self.count < 420 or self.count % 20 // 10 == 0)