from character.base.character import character
from const.const import *
import random
from system.hp import hp

class UTD(character):
    def __init__(self):
        self.x = field_width-1
        self.y = 500
        self.angle = 0
        #self.no = no
        self.spd = 1
        self.direction = direction_left
        self.count = 0
        self.ghost_count = 0
        self.name = "アルティメットつくしドラゴン"
        self.img_width = 800
        self.img_height = 1000
        self.hit_width = 400
        self.hit_height = 1000

        self.hp = hp(100)

        self.is_fadeout = False
        self.is_ghost = False
        #攻撃の受けたつくしの無効化フラグ
        self.is_death = False
        #死亡エフェクト後にインスタンスを削除する為のフラグ
        self.is_del = False

    def move(self, p):
        self.count += 1
        if self.is_ghost:
            self.ghost_count += 1
        if self.ghost_count > 30:
            self.is_ghost = False
            self.ghost_count = 0
        if self.is_death == True:
            self.count += 1
            if self.count >= 400:
                self.is_del = True
            return
        if self.count % 5 == 0:
            self.x -= self.spd
            # if self.is_fadeout and self.count >= 40:
            #     self.is_del = True

    def damage(self, pygame, type, player):
        if not self.is_ghost and not self.is_death:
            self.hp.change_hp(-20)
            if self.hp.hp == 0:
                self.is_death = True
                self.count = 0
                return
            self.is_ghost = True


    def get_img(self):
        if self.is_death:
            return b_img_index_utd_dead[self.count % 400 // 80]
        if self.count % 90 < 30:
            num = 0
        elif self.count % 90 < 40:
            num = 1
        elif self.count % 90 < 50:
            num = 2
        elif self.count % 90 < 60:
            num = 3
        elif self.count % 90 < 90:
            num = 4
        return b_img_index_utd[num]
