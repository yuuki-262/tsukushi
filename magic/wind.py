from magic.base.magic import magic
from const.const import *
from service.service import is_hitting

class wind(magic):
    def __init__(self, x, y, direction):
        self.name = "風"
        self.x = x
        self.y = y
        self.spd = 3
        self.width = 90
        self.height = 130
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


    def attack(self, enemies):
        self.count += 1
        if self.count < 20:
        #つくしのヒット処理
            for e in enemies:
                if e.is_death == False and is_hitting(self, e):
                    e.death_type = self.name
                    e.is_death = True
                    #score += 1
        if self.count >= 40:
            self.is_del = True


    def get_img(self):
        num = self.count % 30 // 10 + 1
        return (dir_img_magic + self.name +  str(num) + png)
