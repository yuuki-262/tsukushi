import pygame
import math

from character.base.character import character
from const.const import *
from service.service import sound_se

from item.base.item import item
from magic.fire import fire
from magic.thunder import thunder
from magic.wind import wind

from system.hp import hp
from system.mp import mp

class player(character):
    def __init__(self, x, y):
        self.x = x
        self.y = field_position[1] + y
        self.r = p_hit_circle_r
        self.angle = 0
        self.spd = p_spd
        self.img_width = p_img_width
        self.img_height = p_img_height
        self.hit_width = 75
        self.hit_height = 75
        self.count = 0
        self.damage_count = 0
        self.direction = direction_down

        self.hp = hp(100)
        self.mp = mp(100)

        self.attack_type = 2
        self.attack_values = p_attack_values
        self.use_attack_mp = [p_fire_use_mp, p_thunder_use_mp, p_wind_use_mp]
        self.magics = []
        self.motion = [0, 1, 0, 2, 0, 1]
        self.is_moving = False
        self.is_attack = False

        self.is_damaging = False
        self.is_mp_heal = True
        self.is_death = False
        self.death_count = 0

    def state(self, angle, keys):
        self.count += 1
        if not self.is_mp_heal and self.count > 60:
            self.is_mp_heal = True
        if not self.is_death:
            self.move(angle, keys)
            if self.is_mp_heal:
                self.auto_mp_heal()
            #ダメージを受けているときは無敵
            if self.is_damaging:
                self.ghost()

    #位置情報の更新
    def move(self, angle=0, keys=None):
        if self.is_moving and not self.is_attack:
            self.check_move(angle)
        if self.is_attack == False:
            if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                self.check_move(math.radians(135))
                self.direction = direction_left
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                self.check_move(math.radians(225))
                self.direction = direction_left
            elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                self.check_move(math.radians(45))
                self.direction = direction_right
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                self.check_move(math.radians(315))
                self.direction = direction_right
            elif keys[pygame.K_LEFT]:
                self.check_move(math.radians(180))
                self.direction = direction_left
            elif keys[pygame.K_RIGHT]:
                self.check_move(math.radians(0))
                self.direction = direction_right
            elif keys[pygame.K_UP]:
                self.check_move(math.radians(90))
                self.direction = direction_up
            elif keys[pygame.K_DOWN]:
                self.check_move(math.radians(270))
                self.direction = direction_down

    def get_img(self):
        if self.is_death:
            return p_img_index_dead[0 if self.death_count < 50 else 1]
            #return dir_img_warui + "ダウン" + str(1 if self.count < 50 else 2) + png
        if self.is_attack:
            if self.count < 10:
                return p_img_index_attack[self.direction][self.count // 5]
            self.is_attack = False
        if self.is_moving:
            return p_img_index_move[self.direction][self.count % 40 // 10]
        num = self.count % 200 // 50
        if self.count % 200 > 109:
            num += 1
        if self.count % 200 > 139:
            num += 1
        return p_img_index_normal[self.direction][self.motion[num]]

    def attack(self, pygame):
        if self.is_attack:
            return
        if self.mp.mp < self.use_attack_mp[self.attack_type]:
            sound_se(pygame, dir_SE + "NoMP.wav")
            return
        self.is_attack = True
        self.count = 0
        self.is_mp_heal = False
        self.mp.change_mp(-1 * self.use_attack_mp[self.attack_type])
        if self.mp.mp <= 0:
            self.mp.mp = 0
        self.add_magic(pygame)

    def hit_enemy(self, pygame):
        if not self.is_damaging:
            self.hp.change_hp(-25)
            sound_se(pygame, dir_SE + "Damage.wav")
            self.is_damaging = True
        if self.hp.hp == 0:
            #死んだときの処理
            self.count = 0
            self.is_death = True
            sound_se(pygame, dir_SE + "Down.wav")

    def ghost(self):
        self.damage_count += 1
        if self.damage_count >= 60:
            self.damage_count = 0
            self.is_damaging = False

    def auto_mp_heal(self):
        if self.count % 10 == 0 and self.mp.mp < 100:
            self.mp.change_mp(1)

    def check_move(self, angle):
        new_x = self.x + math.cos(angle) * self.spd
        new_y = self.y - math.sin(angle) * self.spd
        if new_x > field_left + self.img_width / 2 and new_x < field_right - self.img_width / 2:
            self.x = new_x
        if new_y > field_top and new_y < field_bottom - self.img_height / 2:
            self.y = new_y
        self.is_moving = True
        if angle <= (-3 * math.pi / 4) or angle >= (3 * math.pi / 4):
            self.direction = direction_left
        elif angle <= (-1 * math.pi / 4):
            self.direction = direction_down
        elif angle <= (1 * math.pi / 4):
            self.direction = direction_right
        elif angle <= (3 * math.pi / 4):
            self.direction = direction_up

    def check_ghost(self):
        #ダメージを受けているときは10フレームごとに画像を点滅(True時に画像表示)
        return (not self.is_death and self.is_damaging and self.damage_count % 20 // 10 == 0)

    def add_magic(self, pygame):
        if self.attack_values[self.attack_type] == "火":
            self.magics.append(fire(self.x, self.y, self.direction))
            sound_se(pygame, dir_SE + "Fire.wav")
        elif self.attack_values[self.attack_type] == "雷":
            self.magics.append(thunder(self.x, self.y, self.direction))
            sound_se(pygame, dir_SE + "Thunder.wav")
        elif self.attack_values[self.attack_type] == "風":
            self.magics.append(wind(self.x, self.y, self.direction))
            sound_se(pygame, dir_SE + "Wind.wav")

    def result_move(self, clear_position):
        newPosX = self.x - clear_position["x"] / 20
        newPosY = self.y - clear_position["y"] / 20
        self.x = newPosX
        self.y = newPosY
