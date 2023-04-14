import math
from character.player import player
from character.base.character import character
from util.game_util import sound_se
from const.const import *
import random

class tsukushi(character):
    def __init__(self, x, y, direction, type=0):
        self.x = x
        self.y = y
        self.angle = 0
        self.knock_back_distance = {"x" : 0, "y" : 0}
        self.spd = random.randint(2,5)
        self.direction = direction
        self.count = 0
        self.type = type
        self.name = tsukushi_types[self.type]
        if self.direction == direction_left or self.direction == direction_right:
            self.img_width = 100
            self.img_height = 50
            self.hit_width = 80
            self.hit_height = 30
        elif self.direction == direction_up or self.direction == direction_down:
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
    def move(self, p: player):
        self.count += 1
        #self.angle += 1
        #self.angle = math.degrees(math.atan2(-1 * (self.y - p.y), (self.x - p.x))) / 2
        if self.is_ghost and not self.is_fadeout:
            self.knock_back(p)
            return
        if self.is_death == True:
            self.count += 1
            if self.count >= 50:
                self.is_del = True

        if self.direction == direction_left:
            self.x -= self.spd
        elif self.direction == direction_up:
            if not self.is_fadeout:
                self.y -= self.spd
                if self.y <= 200:
                    self.is_fadeout = True
                    self.count = 0
            if self.is_fadeout and self.count >= 40:
                self.is_del = True
        elif self.direction == direction_right:
            self.x += self.spd
        elif self.direction == direction_down:
            self.y += self.spd
                #プレイヤーへの追跡
                # if self.x > p.x:
                #     self.x -= 1
                # elif self.x < p.x:
                #     self.x += 1

    def damage(self, pygame, attack_type, p : player):
        if self.is_ghost or self.is_death:
            return
        if self.type == 2 or self.type == 1:
            self.level_down(pygame, p)
            return
        if self.type == 0:
            self.death_type = attack_type
            self.is_death = True
            self.count = 0
            sound_se(pygame, dir_SE + "HitAttack.wav")
            return

    def knock_back(self, p: player):
        if self.count > 40:
            self.is_ghost = False
        self.x += 2 * self.knock_back_distance["x"]
        self.y += 2 * self.knock_back_distance["y"]
        if self.y < field_top:
            self.is_del = True
            self.is_fadeout = True
        # self.x += 2 * math.cos(self.knock_back_angle)
        # self.y += 2 * math.sin(self.knock_back_angle)
        # if p.direction == direction_up:
        #     self.y -= 2
        #     self.spd = 2
        # elif p.direction == direction_down:
        #     self.y += 2
        #     self.spd = 2
        # elif p.direction == direction_left:
        #     self.x -= 2
        #     self.spd = 2
        # elif p.direction == direction_right:
        #     self.x += 2
        #     self.spd = 2

    def level_down(self, pygame, p:player):
        self.type -= 1
        self.name = tsukushi_types[self.type]
        self.is_ghost = True
        self.count = 0

        distance = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        self.knock_back_distance["x"] = (self.x - p.x) / distance
        self.knock_back_distance["y"] = (self.y - p.y) / distance
        sound_se(pygame, dir_SE + "HitAttack.wav")

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
