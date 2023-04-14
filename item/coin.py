from item.base.item import item
from const.const import *
from character.player import player
from util.game_util import sound_se

class coin(item):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 40
        self.value = 1
        self.angle = 0
        self.img_width = 50
        self.img_height = 50
        self.hit_width = 50
        self.hit_height = 50
        self.count = 0
        self.type = None
        self.is_del = False

    def get(self, pygame, player: player):
        player.coin_currency += self.value
        sound_se(pygame, dir_SE + "GetCoin.wav")
        self.is_del = True

    def get_img(self, player: player):
        return coin_img_index[self.count // 20 % 3]

    def state(self):
        self.count += 1
        if self.count > 600:
            self.is_del = True

    def check_flash(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (self.count < 420 or self.count % 20 // 10 == 0)