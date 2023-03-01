import pygame

from character.base.character import character
from const.const import *

from item.base.item import item
from magic.fire import fire
from magic.thunder import thunder
from magic.wind import wind

class player(character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spd = 4
        self.width = 75
        self.height = 150
        self.count = 0
        self.direction = direction_down

        self.attack_type = 1
        self.attack_values = ["火", "雷", "風"]
        self.magics = []
        self.motion = ["1", "2", "1", "3", "1", "2"]
        self.is_moving = False
        self.is_attack = False
        self.is_damaging = False

    def move(self, keys):
        self.count += 1
        if self.is_attack == False:
            if keys[pygame.K_LEFT]:
                if self.x - self.spd >= 0 + self.width / 2:
                    self.x = self.x - self.spd
                self.direction = direction_left
                self.is_moving = True
            if keys[pygame.K_RIGHT]:
                if self.x + self.spd <= field_width - self.width / 2:
                    self.x = self.x + self.spd
                self.direction = direction_right
                self.is_moving = True
            if keys[pygame.K_UP]:
                if self.y - self.spd >= 0 + self.height / 2:
                    self.y = self.y - self.spd
                self.direction = direction_up
                self.is_moving = True
            if keys[pygame.K_DOWN]:
                if self.y + self.spd <= field_height - self.height / 2:
                    self.y = self.y + self.spd
                self.direction = direction_down
                self.is_moving = True

    def get_img(self):
        if self.is_attack:
            if self.count < 40:
                return dir_img_warui + self.direction + "攻撃" + str(self.count // 20 + 1) + png
            self.is_attack = False
        if self.is_moving:
            num = self.count % 80 // 20 + 1
            return dir_img_warui + self.direction + "移動" + str(num) + png
        num = self.count % 200 // 50
        if self.count % 200 > 109:
            num += 1
        if self.count % 200 > 139:
            num += 1
        return dir_img_warui + self.direction + self.motion[num] + png

    def attack(self):
        self.is_attack = True
        self.count = 0
        if self.attack_values[self.attack_type] == "火":
            self.magics.append(fire(self.x, self.y, self.direction))
        elif self.attack_values[self.attack_type] == "雷":
            self.magics.append(thunder(self.x, self.y, self.direction))
        elif self.attack_values[self.attack_type] == "風":
            self.magics.append(wind(self.x, self.y, self.direction))

    def get_item(self, i : item):
        if self.attack_values[i.type] == "火":
            self.attack_type = 0
        elif self.attack_values[i.type] == "雷":
            self.attack_type = 1
        elif self.attack_values[i.type] == "風":
            self.attack_type = 2
        i.is_del = True
