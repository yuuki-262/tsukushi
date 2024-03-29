from magic.base.magic import magic
from const.const import *

from util.game_util import is_hitting_circle_rect

class thunder(magic):
    def __init__(self, x, y, direction):
        self.name = "雷"
        self.x = x
        self.y = y
        self.r = thunder_hit_circle_r
        self.angle = 0
        self.spd = 10
        self.use_mp = 20
        self.direction = direction
        if self.direction == direction_left or self.direction == direction_right:
            self.img_width = 75
            self.img_height = 150
            self.hit_width = 75
            self.hit_height = 150
        elif self.direction == direction_up or self.direction == direction_down:
            self.img_width = 75
            self.img_height = 150
            self.hit_width = 75
            self.hit_height = 150
        self.count = 0
        self.is_del = False
        if self.direction == direction_up:
            self.y = y - 80
        elif self.direction == direction_down:
            self.y = y + 80
        elif self.direction == direction_left:
            self.x = x - 80
        elif self.direction == direction_right:
            self.x = x + 80


    def attack(self, pygame, enemies, bosses, items, player = None):
        self.count += 1
        if self.direction == direction_up:
            self.y = self.y - self.spd
        elif self.direction == direction_down:
            self.y = self.y + self.spd
        elif self.direction == direction_left:
            self.x = self.x - self.spd
        elif self.direction == direction_right:
            self.x = self.x + self.spd

        #つくしのヒット処理s
        for e in enemies:
            if e.is_death == False and is_hitting_circle_rect(self, e):
                # 当たり判定可視化
                # import pygame
                # RED = (200, 0, 0)
                # GREEN = (0, 0, 200)
                # BOX1 = pygame.Rect(self.x - (self.width / 2), self.y - (self.height / 2) , self.width, self.height)
                # BOX2 = pygame.Rect(e.x - (e.width / 2), e.y - (e.height / 2) , e.width, e.height)
                # pygame.draw.rect(screen,RED, BOX1)
                # pygame.draw.rect(screen,GREEN, BOX2)
                e.damage(pygame, self.name, player)
                #score += 1
        #ボスのヒット処理
        for b in bosses:
            if b.is_death == False and is_hitting_circle_rect(self, b):
                b.damage(pygame, self.name, player)
        if (self.x < default_field_left - (self.img_width / 2)
                or self.x > default_field_right + (self.img_width / 2)
                or self.y < default_field_top - (self.img_height / 2)
                or self.y > default_field_bottom + (self.img_height / 2) ):
            self.is_del = True


    def get_img(self):
        num = self.count // 20
        if num > 2:
            num = 2
        return warui_img_thunder[self.direction][num]
