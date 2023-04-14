import pygame
import sys
import math
import random

from const.const import *
from character.player import player as player_c
from item.weapon import weapon
from item.heal_item import heal_item
from util.game_util import is_hitting_circle_rect, is_hitting_circle_circle, direction_adjust, sound_se, draw_object
from service.img_service import load_all_imgs
from character.enemy.tsukushi import tsukushi
from character.enemy.boss.UTD import UTD
from repository.system_repository import system_table_init, get_coin_num, update_coin

class in_game:
    def __init__(self):
        self.count = 0
        self.clear_count = 0
        self.is_mouse_down = False
        self.is_mouse_play = False
        self.angle = 0
        self.small_position = (pad_radius, screen_height - pad_radius)
        self.score = 0
        self.target_number = 3
        self.field_index = field_img_index_normal
        self.bg_index = bg_img_index_normal
        self.bg_text_index = title_text1_img_index
        self.mouse_position_base = (0, 0)
        self.mouse_down_count = 0
        self.is_game_clear = False
        self.player = player_c(first_px, first_py)
        self.clear_position = {"x" : 0, "y" : 0}
        self.is_game_end = False
        self.enemies = []
        self.bosses = []
        self.items = []

    def play_game(self, screen, imgs):
        self.count += 1
        player_imgs = imgs[player_imgs_index]
        enemy_imgs = imgs[enemy_imgs_index]
        boss_imgs = imgs[boss_imgs_index]
        item_imgs = imgs[item_imgs_index]
        warui_magic_imgs = imgs[attack_imgs_index]
        system_imgs = imgs[system_imgs_index]
        field_imgs = imgs[field_imgs_index]

        if self.player.is_death:
            self.player.death_count += 1
            self.down(screen, imgs)
        elif self.is_game_clear == True:
            self.draw_system(screen, imgs)
            self.game_clear(screen, imgs)
        else:
            self.draw_system(screen, imgs)
            #操作情報取得
            self.handle_input_events()
            # 敵の追加
            if self.count % pop_enemy_span == 0:
                self.spawn_enemy()

            # 円を描く
            circle_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

            #通常時
            pressed_key = pygame.key.get_pressed()
            mouse_position_now = pygame.mouse.get_pos()

            if mouse_position_now == self.mouse_position_base:
                self.player.is_moving = False
            else:
                if self.is_mouse_down:
                    self.mouse_down_count += 1
                    if self.mouse_down_count >= 3:
                        self.player.is_moving = True
                        self.angle = math.atan2((-1 * (mouse_position_now[1] - self.mouse_position_base[1])), (mouse_position_now[0] - self.mouse_position_base[0]))
            self.player.state(self.angle, pressed_key)

            #アイテムの処理
            for i in self.items:
                i.state()
                if is_hitting_circle_circle(self.player, i):
                    i.get(pygame, self.player)
                if i.is_del:
                    self.items.remove(i)
                    continue
                if i.check_flash():
                    draw_object(pygame, screen, i, item_imgs[i.get_img(self.player)])
                    #screen.blit(item_imgs[i.get_img(self.player)], direction_adjust(i))

            #ボスの処理
            for b in self.bosses:
                if b.is_death:
                    self.clear_position["x"]= self.player.x
                    self.clear_position["y"]= self.player.y
                    sound_se(pygame, dir_SE + "Clear.wav")
                    self.is_game_clear = True
                b.move(self.player)
                if b.is_del:
                    #死んだつくしの削除
                    self.bosses.remove(b)
                    self.score += 1
                    continue
                if is_hitting_circle_rect(self.player, b) and not b.is_ghost:
                    #敵に当たっている時
                    self.player.hit_enemy(pygame)
                    #self.bosses.remove(b)
                    #continue
                if not b.is_ghost or b.count % 30 // 15 == 0:
                    draw_object(pygame, screen, b, boss_imgs[b.get_img()])
                    #screen.blit(boss_imgs[b.get_img()], direction_adjust(b))

            #敵の処理
            for e in self.enemies:
                e.move(self.player)
                if e.x < field_left - (e.img_width / 2) or e.y < 0 + (e.img_height / 2) and not e.is_ghost:
                    #画面外のつくしを削除
                    #self.enemies.remove(e)
                    continue

                if e.is_del:
                    #死んだつくしの削除
                    if not e.is_fadeout:
                        self.spawn_item(e)
                        self.score += 1
                    self.enemies.remove(e)
                    continue
                else:
                    if is_hitting_circle_rect(self.player, e) and not e.is_ghost and not e.is_fadeout:
                        #敵に当たっている時
                        if e.is_death:
                            pass
                        else:
                            self.player.hit_enemy(pygame)
                            #self.enemies.remove(e)
                            #continue
                if not e.is_ghost or e.count % 30 // 15 == 0:
                    e_image = pygame.transform.rotate(enemy_imgs[e.get_img()], e.angle)
                    draw_object(pygame, screen, e, e_image)


            #魔法の処理
            for m in self.player.magics:
                m.attack(pygame, self.enemies, self.bosses, self.items, self.player)
                if not m.is_del:
                    draw_object(pygame, screen, m, warui_magic_imgs[m.get_img()])
                    #screen.blit(warui_magic_imgs[m.get_img()], direction_adjust(m))
                else:
                    self.player.magics.remove(m)

            #プレイヤーの描写
            if not self.player.check_ghost():
                #self.player.angle = self.count
                draw_object(pygame, screen, self.player, player_imgs[self.player.get_img()])
                #screen.blit(player_imgs[self.player.get_img()], direction_adjust(self.player))


            # 円の半径
            radius = pad_radius
            radius_small = radius / 4
            if self.count % 5 == 0:
                if self.is_mouse_down:
                    self.small_position = radius + (math.cos(self.angle) * (radius_small * 2)), screen_height - radius - (math.sin(self.angle) * (radius_small * 2))
                elif mouse_position_now != self.mouse_position_base:
                    pass
                else:
                    self.small_position = (radius , screen_height - radius)

            if self.is_mouse_play:
                pygame.draw.circle(circle_surface, (0, 0, 0, 50), (radius, screen_height - radius), radius, pygame.SRCALPHA)
                pygame.draw.circle(circle_surface, (255, 255, 255, 80), self.small_position, radius_small, pygame.SRCALPHA)
                screen.blit(circle_surface, (0, 0))

            self.mouse_position_base = pygame.mouse.get_pos()

        pygame.display.update()

    def down(self, screen, imgs):
        player_imgs = imgs[player_imgs_index]
        system_imgs = imgs[system_imgs_index]
        darken_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        pressed_key = pygame.key.get_pressed()
        self.player.state(0, pressed_key)
        # 透明度を徐々に上げる
        if self.player.death_count < 125:
            darken_surface.fill((0, 0, 0, self.player.death_count))
            screen.blit(darken_surface, (0, 0))
            draw_object(pygame, screen, self.player, player_imgs[self.player.get_img()])
            screen.blit(player_imgs[self.player.get_img()], direction_adjust(self.player))
        elif self.player.death_count < 245:
            darken_surface.fill((0, 0, 0))
            # 画面に透明な黒いサーフェスを描画する
            screen.blit(darken_surface, (0, 0))
            font = pygame.font.Font(None, 80)
            text = font.render("GAME OVER", True, (255,255,255))
            screen.blit(text, [220, 450])
        else:
            screen.blit(system_imgs[result_back_img_index], (0,0))
            screen.blit(system_imgs[result_img_index], (0,0))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.is_game_end = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.is_game_end = True
        return

    def game_clear(self, screen, imgs):
        self.clear_count += 1
        self.draw_system(screen, imgs)
        if self.clear_count < 30:
            self.flush(screen, imgs)
            return
        if self.clear_count < 130:
            if self.clear_count == 30:
                sound_se(pygame, dir_SE + "BossDead.wav")
            for b in self.bosses:
                b.move(self.player)
                if b.is_del:
                    #死んだつくしの削除
                    self.bosses.remove(b)
                    self.score += 1
                    continue
                if not b.is_ghost or b.count % 30 // 15 == 0:
                    draw_object(pygame, screen, b, imgs[boss_imgs_index][b.get_img()])
            screen.blit(imgs[player_imgs_index][self.player.get_img()], direction_adjust(self.player))
        else:
            if self.clear_count < 150:
                screen.blit(imgs[system_imgs_index][result_back_img_index], (0,0))
                self.player.result_move(self.clear_position)
                screen.blit(imgs[player_imgs_index][self.player.get_img()], direction_adjust(self.player))
            elif self.clear_count < 160:
                screen.blit(imgs[system_imgs_index][result_back_img_index], (0,0))
                screen.blit(imgs[system_imgs_index][result_img_index], (0,0))
                screen.blit(imgs[system_imgs_index][result_stand_img_index], (0,0))
                draw_object(pygame, screen, self.player, imgs[player_imgs_index][p_img_index_win[0]])
            else:
                screen.blit(imgs[system_imgs_index][result_back_img_index], (0,0))
                screen.blit(imgs[system_imgs_index][result_img_index], (0,0))
                screen.blit(imgs[system_imgs_index][result_stand_img_index], (0,0))
                draw_object(pygame, screen, self.player, imgs[player_imgs_index][p_img_index_win[1]])
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.is_game_end = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.is_game_end = True

        clear_font = pygame.font.Font("JKG-L_3.ttf", 50)
        #text = clear_font.render("ゲームクリア！！" , True, (0,0,0))
        #screen.blit(text, [220, 450])

    def flush(self, screen, imgs):
        if self.clear_count < 10:
            flush_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            flush_surface.fill((255, 255, 255))
            screen.blit(flush_surface, (0, 0))
        elif self.clear_count < 20:
            if self.clear_count == 30:
                sound_se(pygame, dir_SE + "BossDead.wav")
            for b in self.bosses:
                    draw_object(pygame, screen, b, imgs[boss_imgs_index][b.get_img()])
            screen.blit(imgs[player_imgs_index][self.player.get_img()], direction_adjust(self.player))
        elif self.clear_count < 30:
            flush_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            flush_surface.fill((255, 255, 255))
            screen.blit(flush_surface, (0, 0))

    def spawn_enemy(self):
        num = random.randint(0,10)
        if num <= 6:
            num = 0
        elif num <= 9:
            num = 1
        else:
            num = 2
        num2 = random.randint(0,1)
        if num2 == 0:
            if len(self.bosses) == 0 and (self.target_number - self.score) <= 0:
                self.bosses.append(UTD())
            self.enemies.append(tsukushi(field_right, random.randint(field_top, field_bottom), direction_left, num))
        elif num2 == 1:
            self.enemies.append(tsukushi(random.randint(field_left, field_right), field_bottom, direction_up, num))
        elif num2 == 2:
            self.enemies.append(tsukushi(random.randint(field_left, field_right), field_top, direction_down, num))
        elif num2 == 3:
             self.enemies.append(tsukushi(field_left, random.randint(field_top, field_bottom), direction_right, num))

    def spawn_item(self, e):
        if len(self.items) < drop_item:
            item_type = random.randint(0, 1)
            if item_type == 0:
                self.items.append(weapon(e.x, e.y, random.randint(0, 2)))
            elif item_type == 1:
                self.items.append(heal_item(e.x, e.y, random.randint(0, 1)))

    def handle_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.is_mouse_play = False
                if event.key == pygame.K_SPACE:
                    self.player.attack(pygame)
            if event.type == pygame.KEYUP:
                self.player.is_moving = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_mouse_down = True
                self.is_mouse_play = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_mouse_down = False
                self.player.is_moving = False
                if self.mouse_down_count <= 2:
                    self.player.attack(pygame)
                self.mouse_down_count = 0


            if pygame.mouse.get_pos() == self.mouse_position_base:
                self.player.is_moving = False
            else:
                if self.is_mouse_down:
                    self.mouse_down_count += 1
                    if self.mouse_down_count >= 3:
                        self.player.is_moving = True
                        self.angle = math.atan2((-1 * (pygame.mouse.get_pos()[1] - self.mouse_position_base[1])), (pygame.mouse.get_pos()[0] - self.mouse_position_base[0]))

    def draw_system(self, screen, imgs):
        system_imgs = imgs[system_imgs_index]
        field_imgs = imgs[field_imgs_index]
        screen.blit(system_imgs[bg_img_index_normal], system_imgs[bg_img_index_normal].get_rect())
        screen.blit(field_imgs[self.field_index], field_position)
        screen.blit(system_imgs[hpmp_bar_under_img_index], hp_position)
        if self.player.mp.mp < self.player.use_attack_mp[self.player.attack_type]:
            screen.blit(system_imgs[no_mp_img_index].subsurface(pygame.Rect(0, 0, mp_width_left + (mp_width_middle * self.player.mp.mp / self.player.mp.max_mp), system_imgs[mp_img_index].get_height())), hp_position)
        else:
            screen.blit(system_imgs[mp_img_index].subsurface(pygame.Rect(0, 0, mp_width_left + (mp_width_middle * self.player.mp.mp / self.player.mp.max_mp), system_imgs[mp_img_index].get_height())), hp_position)
        screen.blit(system_imgs[bar_warui_magic_img_index[self.player.attack_type]], hp_position)
        screen.blit(system_imgs[awake_cover_index], hp_position)
        screen.blit(system_imgs[hp_img_index].subsurface(pygame.Rect(0, 0, hp_width_left + (hp_width_middle * self.player.hp.hp / self.player.hp.max_hp), system_imgs[hp_img_index].get_height())), hp_position)
        screen.blit(system_imgs[hpmp_bar_img_index], hp_position)
        target_number_font = pygame.font.Font(None, 50)
        if not self.is_game_clear:
            if self.target_number - self.score > 0:
                text = target_number_font.render("あと" + str(self.target_number - self.score) + "体倒せ！！" , True, (0,0,0))
                screen.blit(text, [400, 0])
            else:
                text = target_number_font.render("ボス出現！！" , True, (0,0,0))
                screen.blit(text, [500, 0])
        if len(self.bosses):
            screen.blit(system_imgs[boss_hp_bar_img_index], boss_hp_position)
            screen.blit(system_imgs[boss_hp_img_index].subsurface(pygame.Rect(0, 0, system_imgs[boss_hp_img_index].get_width() * (self.bosses[0].hp.hp / self.bosses[0].hp.max_hp), system_imgs[boss_hp_img_index].get_height())), boss_hp_position)
