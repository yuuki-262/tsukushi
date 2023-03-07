import pygame
import sys

import random

from const.const import *

from character.player import player as player_c
from item.weapon import weapon
from item.heal_item import heal_item
from service.service import is_hitting, direction_adjast
from service.img_servise import *
from character.tsukushi import tsukushi


def main():
    pygame.init()
    pygame.display.set_caption("つくしの軍勢")
    player = player_c(first_px, first_py)
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
    enemies = []
    items = []

    player_imgs = load_player_imgs()
    enemy_imgs = load_enemy_imgs()
    item_imgs = load_item_imgs()
    warui_magic_imgs = load_attack_imgs()
    index = 0

    alpha = 0

    score = 0
    count = 0

    bg = pygame.image.load(dir_background1_img).convert_alpha()
    rect_bg = bg.get_rect()
    screen.blit(bg, rect_bg)

    # 背景画像の取得
    field = pygame.image.load(dir_field_img).convert_alpha()
    rect_bg = bg.get_rect()
    screen.blit(field, field_position)

    # HP画像の取得
    hp_bar_img = pygame.image.load(dir_hp_bar_img).convert_alpha()
    screen.blit(hp_bar_img, hp_position)
    # HPバーの取得
    hp_img = pygame.image.load(dir_hp_img).convert_alpha()
    screen.blit(hp_img, hp_position)

    # MP画像の取得
    mp_bar_img = pygame.image.load(dir_mp_bar_img).convert_alpha()
    screen.blit(mp_bar_img, mp_position)
    # MPバーの取得
    mp_img = pygame.image.load(dir_mp_img).convert_alpha()
    screen.blit(mp_img, mp_position)

    # プレイヤー画像の取得
    screen.blit(player_imgs[player.get_img()], direction_adjast(player))
    pygame.display.update()

    while True:
        #キャラクター死亡時
        if player.is_death:
            alpha = domn(screen, player, font, alpha, player_imgs)
            clock.tick(60)
            continue

        #通常時
        screen.blit(bg, rect_bg)
        screen.blit(field, field_position)
        pressed_key = pygame.key.get_pressed()
        player.state(pressed_key)

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
            i.state()
            if is_hitting(player, i):
                i.get(player)
            if i.is_del:
                items.remove(i)
                continue
            if i.check_flash():
                screen.blit(item_imgs[i.get_img(player)], direction_adjast(i))

        #敵の追加
        if count % 20 == 0:
            if random.randint(0,1) == 0:
                enemies.append(tsukushi(field_right, random.randint(field_top, field_bottom), direction_left, random.randint(0,2)))
            else:
                enemies.append(tsukushi(random.randint(field_left, field_right), field_bottom, direction_up))

        #敵の処理
        for e in enemies:
            e.move(player)
            if e.x < field_left - (e.img_width / 2) or e.y < field_top + (e.img_height / 2):
                #画面外のつくしを削除
                enemies.remove(e)
                continue

            if e.is_del:
                #死んだつくしの削除
                if random.randint(0,5) < 2 and len(items) < 3:
                    items.append(weapon(e.x, e.y, random.randint(0,2)))
                elif random.randint(0,5) < 2 and len(items) < 3:
                    items.append(heal_item(e.x, e.y, random.randint(0,2)))
                enemies.remove(e)
                continue
            else:
                if is_hitting(player, e) and not e.is_ghost:
                    #敵に当たっている時
                    if player.is_wind:
                        e.damage(p_attack_values[2])
                    elif e.is_death:
                        pass
                    else:
                        player.hit_enemy()
                        enemies.remove(e)
                        continue
            if not e.is_ghost or e.count % 30 // 15 == 0:
                screen.blit(enemy_imgs[e.get_img()], direction_adjast(e))


        #魔法の処理
        for m in player.magics:
            m.attack(enemies, player)
            if not m.is_del:
                screen.blit(warui_magic_imgs[m.get_img()], direction_adjast(m))
            else:
                player.magics.remove(m)


        if not player.check_ghost():
            screen.blit(player_imgs[player.get_img()], direction_adjast(player))

        #hp_text = font.render("HP:" + str(player.hp), True, (0,0,0))
        #screen.blit(hp_text, [600, 0])

        screen.blit(hp_bar_img, hp_position)
        screen.blit(hp_img.subsurface(pygame.Rect(0, 0, hp_width_left + (hp_width_middle * player.hp / player.max_hp), hp_img.get_height())), hp_position)
        screen.blit(mp_bar_img, mp_position)
        screen.blit(mp_img.subsurface(pygame.Rect(0, 0, mp_width_left + (mp_width_middle * player.mp / player.max_hp), mp_img.get_height())), mp_position)

        pygame.display.update()
        count += 1
        clock.tick(60)


def domn(screen, player, font, alpha, player_imgs):
    darken_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    pressed_key = pygame.key.get_pressed()
    player.state(pressed_key)
    # 透明度を徐々に上げる
    if alpha < 125:
        alpha += 1
        darken_surface.fill((0, 0, 0, alpha))
        screen.blit(darken_surface, (0, 0))
        screen.blit(player_imgs[player.get_img()], direction_adjast(player))
    else:
        darken_surface.fill((0, 0, 0, alpha))
        # 画面に透明な黒いサーフェスを描画する
        screen.blit(darken_surface, (0, 0))
        text = font.render("GAME OVER", True, (255,255,255))
        screen.blit(text, [220, 450])
    pygame.display.update()
    return alpha

if __name__ == '__main__':
    main()
