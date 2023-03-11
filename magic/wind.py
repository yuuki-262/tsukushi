from magic.base.magic import magic
from const.const import *
from service.service import is_hitting

class wind(magic):
    def __init__(self, x, y, direction):
        self.name = "風"
        self.x = x
        self.y = y
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


    def attack(self, enemies, player):
        player.is_wind = True
        self.count += 1
        if self.count % 60 < 20:
            self.x = player.x + 50
            self.y = player.y - 30
        elif self.count % 60 < 40:
            self.x = player.x - 50
            self.y = player.y - 80
        elif self.count % 60 < 60:
            self.x = player.x - 50
            self.y = player.y + 50
        if self.count >= 240:
            self.is_del = True


    def get_img(self):
        num = self.count % 30 // 10
        return warui_img_wind[self.direction][num]
