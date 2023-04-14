import math

from magic.base.magic import magic
from const.const import *
from util.game_util import is_hitting_circle_rect

class wind(magic):
    def __init__(self, x, y, direction):
        self.name = "風"
        self.x = x
        self.y = y
        self.r = wind_hit_circle_r
        self.angle = 0
        self.warui_angle = 0
        self.warui_distance = 100
        self.spd = 3
        self.use_mp = 70
        self.img_width = 75
        self.img_height = 150
        self.hit_width = 75
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
        self.warui_angle += 3
        self.x = player.x + self.warui_distance * math.cos(math.radians(self.warui_angle))
        self.y = player.y + self.warui_distance * math.sin(math.radians(self.warui_angle))
        for e in enemies:
            if e.is_death == False and is_hitting_circle_rect(self, e):
                e.damage(pygame, self.name, player)
        for b in bosses:
            if b.is_death == False and is_hitting_circle_rect(self, b):
                b.damage(pygame, self.name, player)
        if self.count >= 1000:
            self.is_del = True


    def get_img(self):
        return warui_img_wind[self.direction][self.count % 60 // 20]
