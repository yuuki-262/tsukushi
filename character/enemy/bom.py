from character.base.character import character
from service.service import sound_se
from const.const import *
import random

class bom(character):
    def __init__(self, x, y, direction, type=0):
        self.x = x
        self.y = y
        #self.no = no
        self.spd = random.randint(3,6)
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

        self.is_fadeout = False
        self.is_ghost = False
        #攻撃の受けたつくしの無効化フラグ
        self.is_death = False
        #死亡エフェクト後にインスタンスを削除する為のフラグ
        self.is_del = False

        self.death_type = ""
        self.img_name = ""
    def move(self, p):
        self.count += 1
        if self.is_ghost and not self.is_fadeout:
            if self.count > 60:
                self.is_ghost = False
            if self.direction == direction_left:
                self.x += 2
                self.spd = 2
            elif self.direction == direction_up:
                self.y += 2
                self.spd = 2
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
                if not self.is_fadeout:
                    self.y -= self.spd
                    if self.y <= 200:
                        self.is_fadeout = True
                        self.count = 0
                if self.is_fadeout and self.count >= 40:
                    self.is_del = True
                #プレイヤーへの追跡
                # if self.x > p.x:
                #     self.x -= 1
                # elif self.x < p.x:
                #     self.x += 1

    def damage(self, pygame, attack_type):
        if self.is_ghost or self.is_death:
            return
        if self.type == 2:
            self.type -= 1
            self.name = tsukushi_types[self.type]
            self.is_ghost = True
            self.count = 0
            sound_se(pygame, dir_SE + "HitAttack.wav")
            return
        if self.type == 1:
            self.type -= 1
            self.name = tsukushi_types[self.type]
            self.is_ghost = True
            self.count = 0
            sound_se(pygame, dir_SE + "HitAttack.wav")
            return
        if self.type == 0:
            self.death_type = attack_type
            self.is_death = True
            self.count = 0
            sound_se(pygame, dir_SE + "HitAttack.wav")
            return

    def get_img(self):
        if self.is_death and self.death_type != "":
            return e_img_index_dead[self.direction][self.death_type][self.count % 50 // 10]
        if self.is_fadeout and self.direction == direction_up:
            return e_up_fadeout_index[self.count % 40 // 10]
        if self.type == 2:
            return e_king_index[self.direction][self.count % 30 // 10]
        if self.type == 1:
            return e_hige_index[self.direction][self.count % 30 // 10]
        return e_img_index_normal[self.direction][0]
