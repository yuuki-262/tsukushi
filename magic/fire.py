from magic.base.magic import magic
from const.const import *

from util.game_util import is_hitting_circle_rect, is_hitting_circle_circle

class fire(magic):
    def __init__(self, x, y, direction):
        self.name = "火"
        self.x = x
        self.y = y
        self.r = fire_hit_circle_r
        self.angle = 0
        self.spd = 3
        self.use_mp = 10
        self.img_width = 75
        self.img_height = 150
        self.hit_width = 90
        self.hit_height = 150
        self.count = 0
        self.is_del = False
        self.direction = direction
        if self.direction == direction_up:
            self.y = y - 80
        elif self.direction == direction_down:
            self.y = y + 80
        elif self.direction == direction_left:
            self.x = x - 80
        elif self.direction == direction_right:
            self.x = x + 80


    def attack(self, pygame, enemies, bosses, items, player = None):
        self.count += 1
        if self.count < 20:
        #つくしのヒット処理
            for e in enemies:
                if e.is_death == False and is_hitting_circle_rect(self, e):
                    e.damage(pygame, self.name, player)
            for b in bosses:
                if b.is_death == False and is_hitting_circle_rect(self, b):
                    b.damage(pygame, self.name, player)
            for i in items:
                if is_hitting_circle_circle(self, i):
                    self.onigiri_bake(i)
        if self.count >= 30:
            self.is_del = True

    def onigiri_bake(self, item):
        if item.type == "onigiri" or item.type == "shine":
            item.type = "baked"

    def get_img(self):
        num = self.count % 30 // 10
        return warui_img_fire[self.direction][num]
