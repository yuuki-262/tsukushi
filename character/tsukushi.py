from character.base.character import character
from const.const import *

class tsukushi(character):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        #self.no = no
        self.spd = 2
        self.direction = direction
        self.count = 0
        if self.direction == direction_left:
            self.img_width = 80
            self.img_height = 30
            self.hit_width = 80
            self.hit_height = 30
        elif self.direction == direction_up:
            self.img_width = 30
            self.img_height = 80
            self.hit_width = 30
            self.hit_height = 80

        #攻撃の受けたつくしの無効化フラグ
        self.is_death = False
        #死亡エフェクト後にインスタンスを削除する為のフラグ
        self.is_del = False

        self.death_type = ""
        self.img_name = ""
    def move(self, p):
        if self.is_death == True:
            self.count += 1
            if self.count >= 50:
                self.is_del = True
        else:
            if self.direction == direction_left:
                self.x -= self.spd
                #プレイヤーへの追跡
                # if self.y > p.y:
                #     self.y -= 1
                # elif self.y < p.y:
                #     self.y += 1

            elif self.direction == direction_up:
                self.y -= self.spd
                #プレイヤーへの追跡
                # if self.x > p.x:
                #     self.x -= 1
                # elif self.x < p.x:
                #     self.x += 1

    def get_img(self):
        if self.is_death == True and self.death_type != "":
            num = self.count % 50 // 10
            return e_img_index_dead[self.direction][self.death_type][num]
        return e_img_index_nomal[self.direction][0]
