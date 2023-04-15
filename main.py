import pygame
import sys
import math
import random

from const.const import *
from system.in_game import in_game
from util.game_util import sound_se
from service.img_service import load_all_imgs

from repository.system_repository import system_table_init, get_coin_num, update_coin

class Game:
    def __init__(self):
        self.index = title_index
        self.next_index = in_game_index
        self.count = 0
        self.title_index = title_img_index_normal
        self.bg_index = bg_img_index_normal
        self.bg_text_index = title_text1_img_index
        self.game = in_game()

    def main(self):
        pygame.init()
        pygame.display.set_caption("つくしの軍勢")

        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        imgs = load_all_imgs()

        system_table_init()

        while True:
            if self.index == title_index:
                self.title_screen(imgs, screen, clock)
            elif self.index == load_index:
                self.load_screen(screen, clock)
            elif self.index == in_game_index:
                if self.game.is_game_end:
                    self.change_index(title_index)
                self.game.play_game(screen, imgs)
                clock.tick(60)

    def title_screen(self, imgs, screen, clock):
        title_images = imgs[title_imgs_index]
        self.count += 1
        screen.blit(title_images[self.title_index], title_images[self.title_index].get_rect())
        if self.count % 120 // 60 == 0:
            screen.blit(title_images[self.bg_text_index], title_images[self.title_index].get_rect())
        target_number_font = pygame.font.Font("JKG-L_3.ttf", 50)
        #text = target_number_font.render("コイン：" + str(get_coin_num()) + "枚", True, (255,255,255))
        #screen.blit(text, [400, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and self.count > 120:
                self.change_index(in_game_index)
                self.count = 0
                sound_se(pygame, dir_SE + "GameStart.wav")
        pygame.display.update()
        clock.tick(60)

    def load_screen(self, screen, clock):
        self.count += 1
        darken_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        darken_surface.fill((0, 0, 0, 30))
        screen.blit(darken_surface, (0, 0))
        pygame.display.update()
        if self.count > 40:
            self.index = self.next_index
            self.count = 0
            if self.index == in_game_index:
                self.game = in_game()
        clock.tick(60)

    def change_index(self, next):
        self.count = 0
        self.next_index = next
        self.index = load_index


if __name__ == '__main__':
    game = Game()
    game.main()
