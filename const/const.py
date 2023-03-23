#画像ディレクトリ
dir_img = "img/"
dir_music = "music/"
dir_SE = dir_music + "SE/"

dir_img_title = "img/title/"
dir_img_player = "img/player/"
dir_img_enemy = "img/enemy/"
dir_img_field = "img/field/"
dir_img_item = "img/item/"
dir_img_system = "img/system/"

dir_img_warui = dir_img_player + "warui/"
dir_img_magic = dir_img_warui + "magic/"

dir_img_tsukushi = dir_img_enemy + "tsukushi/"
dir_img_boss = dir_img_enemy + "boss/"

dir_background1_img = dir_img_field + "背景1.png"
dir_field_img = dir_img_field + "フィールド.png"
dir_hp_bar_img = dir_img_system + "HPバー.png"
dir_hp_img = dir_img_system + "HP.png"
dir_mp_bar_img = dir_img_system + "MPバー.png"
dir_mp_img = dir_img_system + "MP.png"



#方向
direction_up = "上"
direction_down = "下"
direction_left = "左"
direction_right = "右"



#拡張子
png = ".png"

#スクリーン
screen_width = 800
screen_height = 1000
tmp_height = 200

#フィールド
field_width = 800
field_height = 800
field_position = [0, 200]
field_top = 200
field_bottom = 1000
field_left = 0
field_right = 800


#プレイヤー
first_px = 350
first_py = 350

p_invincible_time = 120
p_spd = 7
p_img_width = 75
p_img_height = 150
p_hit_width = 75
p_hit_height = 150

p_fire_use_mp = 10
p_thunder_use_mp = 20
p_wind_use_mp = 60

p_attack_values = ["火", "雷", "風"]

#敵
tsukushi_types = ["つくし", "キング", "ひげ"]

#システム
hp_width = 350
hp_width_left = 20
hp_width_right = 20
hp_width_middle = hp_width - hp_width_left - hp_width_right
hp_height = 100

mp_width = 350
mp_width_left = 20
mp_width_right = 20
mp_width_middle = mp_width - mp_width_left - mp_width_right
mp_height = 100

hp_position = [50, 10]
mp_position = [50, 60]

onigiri_type = ["onigiri", "shine", "baked"]

pad_radius = 120

#ゲームインデックス
title_index = 0
load_index = 1
in_game_index = 2

#全画像インデックス
title_imgs_index = 0
player_imgs_index = 1
enemy_imgs_index = 2
item_imgs_index = 3
attack_imgs_index = 4
system_imgs_index = 5
field_imgs_index = 6
boss_imgs_index = 7

#タイトル画像インデックス
title_img_index_normal = 0
title_text1_img_index = 1

#システム画像インデックス
hp_bar_img_index = 0
hp_img_index = 1
mp_bar_img_index = 2
mp_img_index = 3
bg_img_index_normal = 4

#プレイヤー画像インデックス
p_img_index_up = list(range(0,3))
p_img_index_down = list(range(3,6))
p_img_index_left = list(range(6,9))
p_img_index_right = list(range(9,12))
p_img_index_move_up = list(range(12,16))
p_img_index_move_down = list(range(16,20))
p_img_index_move_left = list(range(20,24))
p_img_index_move_right = list(range(24,28))
p_img_index_attack_up = list(range(28,30))
p_img_index_attack_down = list(range(30,32))
p_img_index_attack_left = list(range(32,34))
p_img_index_attack_right = list(range(34,36))
p_img_index_dead = list(range(36,38))

p_img_index_normal = {direction_up:p_img_index_up, direction_down:p_img_index_down, direction_left:p_img_index_left, direction_right:p_img_index_right}
p_img_index_move = {direction_up:p_img_index_move_up, direction_down:p_img_index_move_down, direction_left:p_img_index_move_left, direction_right:p_img_index_move_right}
p_img_index_attack = {direction_up:p_img_index_attack_up, direction_down:p_img_index_attack_down, direction_left:p_img_index_attack_left, direction_right:p_img_index_attack_right}

#敵画像インデックス
e_img_index_up = list(range(0,1))
e_img_index_fire_up = list(range(1,6))
e_img_index_thunder_up = list(range(6,11))
e_img_index_wind_up = list(range(11,16))

e_img_index_left = list(range(16,17))
e_img_index_fire_left = list(range(17,22))
e_img_index_thunder_left = list(range(22,27))
e_img_index_wind_left = list(range(27,32))


e_img_index_normal = {direction_up:e_img_index_up, direction_left:e_img_index_left}
e_img_index_dead = {
    direction_up:{p_attack_values[0]:e_img_index_fire_up,p_attack_values[1]:e_img_index_thunder_up,p_attack_values[2]:e_img_index_wind_up},
    direction_left:{p_attack_values[0]:e_img_index_fire_left,p_attack_values[1]:e_img_index_thunder_left,p_attack_values[2]:e_img_index_wind_left}
    }

e_king_up_index = list(range(42,45))
e_king_left_index = list(range(32,35))
e_king_index = {direction_up:e_king_up_index, direction_left:e_king_left_index}

e_hige_up_index = list(range(45,48)) #ラスト
e_hige_left_index = list(range(35,38))
e_hige_index = {direction_up:e_hige_up_index, direction_left:e_hige_left_index}

e_up_fadeout_index = list(range(38,42))

#ボス画像インデックス
b_img_index_utd = list(range(0,5))
b_img_index_utd_dead = list(range(5,10))

#アイテム画像インデックス
wepon_img_index_up = {p_attack_values[0]:0, p_attack_values[1]:1, p_attack_values[2]:2}
onigiri_index_fire_up = {onigiri_type[0]:3, onigiri_type[1]:4, onigiri_type[2]:5}

#魔法画像インデックス
warui_img_fire_up = list(range(0,3))
warui_img_fire_down = list(range(3,6))
warui_img_fire_left = list(range(6,9))
warui_img_fire_right = list(range(9,12))

warui_img_thunder_up = list(range(12,15))
warui_img_thunder_down = list(range(15,18))
warui_img_thunder_left = list(range(18,21))
warui_img_thunder_right = list(range(21,24))

warui_img_wind_all = list(range(24,27))

warui_img_fire = {direction_up:warui_img_fire_up, direction_down:warui_img_fire_down, direction_left:warui_img_fire_left, direction_right:warui_img_fire_right}
warui_img_thunder = {direction_up:warui_img_thunder_up, direction_down:warui_img_thunder_down, direction_left:warui_img_thunder_left, direction_right:warui_img_thunder_right}
warui_img_wind = {direction_up:warui_img_wind_all, direction_down:warui_img_wind_all, direction_left:warui_img_wind_all, direction_right:warui_img_wind_all}

warui_magic_img_index = {p_attack_values[0]:warui_img_fire, p_attack_values[1]:warui_img_thunder, p_attack_values[2]:warui_img_wind}

#フィールド画像インデックス
field_img_index_normal = 0