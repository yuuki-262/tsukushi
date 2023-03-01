import pygame
import sys

import random

from const.const import *

from character.player import player as player_c
from item.weapon import weapon
from service.service import is_hitting, direction_adjast
from character.tsukushi import tsukushi
from magic.fire import fire
from magic.thunder import thunder
from magic.wind import wind


def main():
    pygame.init()
    pygame.display.set_caption("つくしの軍勢")
    player = player_c(300, 300)
    screen = pygame.display.set_mode((field_width, field_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)
    enemies = []
    items = []

    score = 0
    count = 0

    # 背景画像の取得
    bg = pygame.image.load(dir_field_img).convert_alpha()
    rect_bg = bg.get_rect()
    screen.blit(bg, rect_bg)
    # プレイヤー画像の取得
    p_img = pygame.image.load(player.get_img()).convert_alpha()
    screen.blit(p_img, direction_adjast(player))
    pygame.display.update()

    while True:
        screen.blit(bg, rect_bg)
        pressed_key = pygame.key.get_pressed()
        player.move(pressed_key)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not player.is_attack:
                        player.attack()
            if event.type == pygame.KEYUP:
                player.is_moving = False

        #アイテムの処理
        for i in items:
            if is_hitting(player, i):
                player.get_item(i)
            if i.is_del:
                items.remove(i)
                continue
            i_img = pygame.image.load(i.get_img(player)).convert_alpha()
            screen.blit(i_img, direction_adjast(i))

        #敵の追加
        if count % 30 == 0:
            if random.randint(0,1) == 0:
                enemies.append(tsukushi(800, random.randint(0,800), direction_left))
            else:
                enemies.append(tsukushi(random.randint(0,800), 800, direction_up))

        #敵の処理
        for e in enemies:
            e.move(player)
            if e.x < 0 - (e.width / 2) or e.y < 0 - (e.height / 2):
                enemies.remove(e)
                continue
            if e.is_del:
                if random.randint(0,5) < 2:
                    items.append(weapon(e.x, e.y, random.randint(0,2)))
                enemies.remove(e)
                continue
            else:
                e_img = pygame.image.load(e.get_img()).convert_alpha()
                screen.blit(e_img, direction_adjast(e))

        #魔法の処理
        for m in player.magics:
            m.attack(enemies)
            if not m.is_del:
                m_img = pygame.image.load(m.get_img()).convert_alpha()
                screen.blit(m_img, direction_adjast(m))
            else:
                player.magics.remove(m)


        p_img = pygame.image.load(player.get_img()).convert_alpha()
        screen.blit(p_img, direction_adjast(player))
        pygame.display.update()
        count += 1
        clock.tick(60)

if __name__ == '__main__':
    main()
