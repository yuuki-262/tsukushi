import pygame
import math

from character.base.character import character
from const.const import *

from item.base.item import item
from magic.fire import fire
from magic.thunder import thunder
from magic.wind import wind

class player(character):
    def __init__(self, x, y):
        self.x = x
        self.y = field_position[1] + y
        self.spd = p_spd
        self.img_width = p_img_width
        self.img_height = p_img_height
        self.hit_width = p_hit_width
        self.hit_height = p_hit_height
        self.count = 0
        self.damage_count = 0
        self.wind_count = 0
        self.direction = direction_down

        self.max_hp = 100
        self.max_mp = 100

        self.hp = 100
        self.mp = 100

        self.attack_type = 0
        self.attack_values = p_attack_values
        self.use_attack_mp = [p_fire_use_mp, p_thunder_use_mp, p_wind_use_mp]
        self.magics = []
        self.motion = [0, 1, 0, 2, 0, 1]
        self.is_moving = False
        self.is_attack = False
        self.is_wind = False
        self.is_damaging = False
        self.is_death = False
        self.death_count = 0

    def state(self, keys):
        self.count += 1
        if self.is_wind:
            self.wind_state()
        if not self.is_death:
            self.move(keys)
            self.auto_me_heal()
            #ダメージを受けているときは無敵
            if self.is_damaging:
                self.ghost()

    #位置情報の更新
    def move(self, keys):
        if self.is_attack == False:
            if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                self.check_move(135)
                self.direction = direction_left
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                self.check_move(225)
                self.direction = direction_left
            elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                self.check_move(45)
                self.direction = direction_right
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                self.check_move(315)
                self.direction = direction_right
            elif keys[pygame.K_LEFT]:
                self.check_move(180)
                self.direction = direction_left
            elif keys[pygame.K_RIGHT]:
                self.check_move(0)
                self.direction = direction_right
            elif keys[pygame.K_UP]:
                self.check_move(90)
                self.direction = direction_up
            elif keys[pygame.K_DOWN]:
                self.check_move(270)
                self.direction = direction_down

    def get_img(self):
        if self.is_death:
            return p_img_index_dead[0 if self.count < 50 else 1]
            #return dir_img_warui + "ダウン" + str(1 if self.count < 50 else 2) + png
        if self.is_attack:
            if self.count < 20:
                return p_img_index_attack[self.direction][self.count // 10]
            self.is_attack = False
        if self.is_moving:
            return p_img_index_move[self.direction][self.count % 80 // 20]
        num = self.count % 200 // 50
        if self.count % 200 > 109:
            num += 1
        if self.count % 200 > 139:
            num += 1
        return p_img_index_normal[self.direction][self.motion[num]]

    def attack(self):
        if self.mp < self.use_attack_mp[self.attack_type]:
            return
        self.is_attack = True
        self.count = 0
        self.mp -= self.use_attack_mp[self.attack_type]
        if self.mp <= 0:
            self.mp = 0
        if self.attack_values[self.attack_type] == "火":
            self.magics.append(fire(self.x, self.y, self.direction))
        elif self.attack_values[self.attack_type] == "雷":
            self.magics.append(thunder(self.x, self.y, self.direction))
        elif self.attack_values[self.attack_type] == "風":
            self.magics.append(wind(self.x, self.y, self.direction))

    def hit_enemy(self):
        if not self.is_damaging:
            self.hp -= 25
            self.is_damaging = True

        if self.hp <= 0:
            #死んだときの処理
            self.hp = 0
            self.count = 0
            self.is_death = True

    def ghost(self):
        self.damage_count += 1

        if self.damage_count >= 120:
            self.damage_count = 0
            self.is_damaging = False

    def auto_me_heal(self):
        if self.count % 60 == 0 and self.mp < 100:
            self.mp += 2

    def check_move(self, angle):
        new_x = self.x + math.cos(math.radians(angle)) * self.spd
        new_y = self.y - math.sin(math.radians(angle)) * self.spd
        if new_x > field_left + self.img_width / 2 and new_x < field_right - self.img_width / 2:
            self.x = new_x
        if new_y > field_top and new_y < field_bottom - self.img_height / 2:
            self.y = new_y
        self.is_moving = True

    def check_ghost(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (not self.is_death and self.is_damaging and self.damage_count % 20 // 10 == 0)

    def wind_state(self):
        self.wind_count += 1
        if self.wind_count > 300:
            self.wind_count = 0
            self.is_wind = False