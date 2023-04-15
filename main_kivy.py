import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

from const.const import *
from system.in_game import in_game
from util.game_util import sound_se
from service.img_service import load_all_imgs

from repository.system_repository import system_table_init, get_coin_num, update_coin

class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.index = title_index
        self.next_index = in_game_index
        self.count = 0
        self.title_index = title_img_index_normal
        self.bg_index = bg_img_index_normal
        self.bg_text_index = title_text1_img_index
        self.game = in_game()

        self.imgs = load_all_imgs()
        system_table_init()

        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        if self.index == title_index:
            self.title_screen()
        elif self.index == load_index:
            self.load_screen()
        elif self.index == in_game_index:
            if self.game.is_game_end:
                self.change_index(title_index)
            self.game.play_game(self.imgs)

    def title_screen(self):
        title_images = self.imgs[title_imgs_index]
        self.count += 1
        self.canvas.clear()
        with self.canvas:
            kivy.graphics.Rectangle(pos=(0, 0), size=Window.size, source=title_images[self.title_index])

        if self.count % 120 // 60 == 0:
            kivy.graphics.Rectangle(pos=(0, 0), size=Window.size, source=title_images[self.bg_text_index])

        for event in kivy.core.window.Window.event.get():
            if event.type == pygame.KEYDOWN and self.count > 120:
                self.change_index(in_game_index)
                self.count = 0
                sound_se(pygame, dir_SE + "GameStart.wav")

    def load_screen(self):
        self.count += 1
        darken_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        darken_surface.fill((0, 0, 0, 30))
        self.canvas.clear()
        with self.canvas:
            kivy.graphics.Rectangle(pos=(0, 0), size=Window.size, texture=kivy.graphics.texture.Texture.create_from_surface(darken_surface))

        if self.count > 40:
            self.index = self.next_index
            self.count = 0
            if self.index == in_game_index:
                self.game = in_game()

    def change_index(self, next):
        self.count = 0
        self.next_index = next
        self.index = load_index


class GameApp(App):
    def build(self):
        game = Game()
        return game


if __name__ == '__main__':
    GameApp().run()