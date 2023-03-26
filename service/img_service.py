import pygame
from const.const import *

def load_player_imgs():
    return [
        pygame.image.load(dir_img_warui + "上1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右3" + png).convert_alpha(),

        pygame.image.load(dir_img_warui + "上移動1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上移動2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上移動3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上移動4" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下移動1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下移動2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下移動3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下移動4" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左移動1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左移動2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左移動3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左移動4" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右移動1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右移動2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右移動3" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右移動4" + png).convert_alpha(),

        pygame.image.load(dir_img_warui + "上攻撃1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "上攻撃2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下攻撃1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "下攻撃2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左攻撃1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "左攻撃2" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右攻撃1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "右攻撃2" + png).convert_alpha(),

        pygame.image.load(dir_img_warui + "ダウン1" + png).convert_alpha(),
        pygame.image.load(dir_img_warui + "ダウン2" + png).convert_alpha(),
        ]

def load_enemy_imgs():
    return [
        pygame.image.load(dir_img_tsukushi + "つくし上" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火上1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火上2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火上3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火上4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火上5" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷上1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷上2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷上3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷上4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷上5" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風上1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風上2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風上3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風上4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風上5" + png).convert_alpha(),

        pygame.image.load(dir_img_tsukushi + "つくし左" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火左1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火左2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火左3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火左4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死火左5" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷左1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷左2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷左3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷左4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死雷左5" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風左1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風左2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風左3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風左4" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "死風左5" + png).convert_alpha(),

        pygame.image.load(dir_img_tsukushi + "キングつくし左1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "キングつくし左2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "キングつくし左3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし左1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし左2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし左3" + png).convert_alpha(),

        pygame.image.load(dir_img_tsukushi + "上消1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "上消2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "上消3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "上消4" + png).convert_alpha(),

        pygame.image.load(dir_img_tsukushi + "キングつくし上1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "キングつくし上2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "キングつくし上3" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし上1" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし上2" + png).convert_alpha(),
        pygame.image.load(dir_img_tsukushi + "ひげつくし上3" + png).convert_alpha(),

    ]

def load_boss_imgs():
    return [
        pygame.image.load(dir_img_boss + "UTD1" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD2" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD3" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD4" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD5" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD死1" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD死2" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD死3" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD死4" + png).convert_alpha(),
        pygame.image.load(dir_img_boss + "UTD死5" + png).convert_alpha(),
    ]

def load_item_imgs():
    return [
        pygame.image.load(dir_img_item + "火メダル" + png).convert_alpha(),
        pygame.image.load(dir_img_item + "雷メダル" + png).convert_alpha(),
        pygame.image.load(dir_img_item + "風メダル" + png).convert_alpha(),
        pygame.image.load(dir_img_item + "おにぎり" + png).convert_alpha(),
        pygame.image.load(dir_img_item + "ふっくらおにぎり" + png).convert_alpha(),
        pygame.image.load(dir_img_item + "焼きおにぎり" + png).convert_alpha(),
    ]

def load_attack_imgs():
    return [
        pygame.image.load(dir_img_magic + "火上1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火上2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火上3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火下1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火下2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火下3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火左1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火左2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火左3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火右1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火右2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "火右3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷上1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷上2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷上3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷下1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷下2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷下3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷左1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷左2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷左3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷右1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷右2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "雷右3" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "風1" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "風2" + png).convert_alpha(),
        pygame.image.load(dir_img_magic + "風3" + png).convert_alpha(),

    ]

def load_title_imgs():
    return [
        pygame.image.load(dir_img_title + "タイトル画面" + png).convert_alpha(),
        pygame.image.load(dir_img_title + "タイトルメッセージ1" + png).convert_alpha(),
    ]

def load_system_imgs():
    return [
        pygame.image.load(dir_img_system + "HPMPバー" + png).convert_alpha(),
        pygame.image.load(dir_img_system + "HPMPバー下地.png").convert_alpha(),
        pygame.image.load(dir_img_system + "HP.png").convert_alpha(),
        pygame.image.load(dir_img_system + "MP.png").convert_alpha(),
        pygame.image.load(dir_img_system + "不足MP.png").convert_alpha(),
        pygame.image.load(dir_img_system + "火.png").convert_alpha(),
        pygame.image.load(dir_img_system + "雷.png").convert_alpha(),
        pygame.image.load(dir_img_system + "風.png").convert_alpha(),
        pygame.image.load(dir_img_system + "覚醒.png").convert_alpha(),
        pygame.image.load(dir_img_system + "覚醒蓋.png").convert_alpha(),

        pygame.image.load(dir_background1_img).convert_alpha(),
    ]

def load_field_imgs():
    return [
        pygame.image.load(dir_field_img).convert_alpha(),
    ]

def load_all_imgs():
    return [
            load_title_imgs(),
            load_player_imgs(),
            load_enemy_imgs(),
            load_item_imgs(),
            load_attack_imgs(),
            load_system_imgs(),
            load_field_imgs(),
            load_boss_imgs(),
        ]