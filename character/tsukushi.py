from character.base.character import character
from const.const import *

class tsukushi(character):
    def __init__(self, x, y, direction, type=0):
        self.x = x
        self.y = y
        #self.no = no
        self.spd = 2
        self.direction = direction
        self.count = 0
        self.type = type
        self.name = tsukushi_types[self.type]
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

        self.is_ghost = False
        #攻撃の受けたつくしの無効化フラグ
        self.is_death = False
        #死亡エフェクト後にインスタンスを削除する為のフラグ
        self.is_del = False

        self.death_type = ""
        self.img_name = ""
    def move(self, p):
        self.count += 1
        if self.is_ghost:
            if self.count > 60:
                self.is_ghost = False
            self.x += self.spd * 2
            return
        if self.is_death == True:
            self.count += 1
            if self.count >= 50:
                self.is_del = True
                return
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

    def damage(self, attack_type):
        if self.is_ghost or self.is_death:
            return
        if self.type == 2:
            self.type -= 1
            self.name = tsukushi_types[self.type]
            self.is_ghost = True
            self.count = 0
            return
        if self.type == 1:
            self.type -= 1
            self.name = tsukushi_types[self.type]
            self.is_ghost = True
            self.count = 0
            return
        if self.type == 0:
            self.death_type = attack_type
            self.is_death = True
            self.count = 0
            return

    def get_img(self):
        if self.type == 2:
            return e_king_index[self.count % 30 // 10]
        if self.type == 1:
            return e_hige_index[self.count % 30 // 10]
        if self.is_death == True and self.death_type != "":
            return e_img_index_dead[self.direction][self.death_type][self.count % 50 // 10]
        return e_img_index_normal[self.direction][0]
