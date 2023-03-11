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

index = 0
title_index = title_img_index_normal
field_index = field_img_index_normal
bg_index = bg_img_index_normal

def main():
    global index
    pygame.init()
    pygame.display.set_caption("つくしの軍勢")


    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)

    player = player_c(first_px, first_py)
    enemies = []
    items = []
    score = 0
    count = 0

    imgs = load_all_imgs()
    bg = pygame.image.load(dir_background1_img).convert_alpha()
    rect_bg = bg.get_rect()
    #screen.blit(bg, rect_bg)

    # 背景画像の取得
    field = pygame.image.load(dir_field_img).convert_alpha()
    rect_bg = bg.get_rect()
    while True:
        title_images = imgs[title_imgs_index]
        if index == 0:
            player = player_c(first_px, first_py)
            enemies = []
            items = []
            score = 0
            count = 0
            screen.blit(title_images[title_index], title_images[title_index].get_rect())
            text = font.render("- Press any key -", True, (255,0,255))
            screen.blit(text, [200, 930])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        index = 1
            clock.tick(60)
            continue

        if index == 1:
            in_game(screen, font, player, enemies, items, imgs, count)
            count += 1
            clock.tick(60)


def in_game(screen, font, player, enemies, items, imgs, count):
    player_imgs = imgs[player_imgs_index]
    enemy_imgs = imgs[enemy_imgs_index]
    item_imgs = imgs[item_imgs_index]
    warui_magic_imgs = imgs[attack_imgs_index]
    system_imgs = imgs[system_imgs_index]
    field_imgs = imgs[field_imgs_index]
    #キャラクター死亡時
    if player.is_death:
        player.death_count += 1
        down(screen, player, font, player_imgs)
        return


    #通常時
    screen.blit(system_imgs[bg_img_index_normal], system_imgs[bg_img_index_normal].get_rect())
    screen.blit(field_imgs[field_index], field_position)
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

    screen.blit(system_imgs[hp_bar_img_index], hp_position)
    screen.blit(system_imgs[hp_img_index].subsurface(pygame.Rect(0, 0, hp_width_left + (hp_width_middle * player.hp / player.max_hp), system_imgs[hp_img_index].get_height())), hp_position)
    screen.blit(system_imgs[mp_bar_img_index], mp_position)
    screen.blit(system_imgs[mp_img_index].subsurface(pygame.Rect(0, 0, mp_width_left + (mp_width_middle * player.mp / player.max_hp), system_imgs[mp_img_index].get_height())), mp_position)

    pygame.display.update()

def down(screen, player, font, player_imgs):
    global index
    darken_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    pressed_key = pygame.key.get_pressed()
    player.state(pressed_key)
    # 透明度を徐々に上げる
    if player.death_count < 125:
        darken_surface.fill((0, 0, 0, player.death_count))
        screen.blit(darken_surface, (0, 0))
        screen.blit(player_imgs[player.get_img()], direction_adjast(player))
    else:
        darken_surface.fill((0, 0, 0, 125))
        # 画面に透明な黒いサーフェスを描画する
        screen.blit(darken_surface, (0, 0))
        text = font.render("GAME OVER", True, (255,255,255))
        screen.blit(text, [220, 450])
        if player.death_count > 300:
            index = 0
    pygame.display.update()
    return


if __name__ == '__main__':
    main()
