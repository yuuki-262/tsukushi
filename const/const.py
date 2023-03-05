#画像ディレクトリ
dir_img = "img/"
dir_img_player = "img/player/"
dir_img_enemy = "img/enemy/"
dir_img_field = "img/field/"
dir_img_item = "img/item/"
dir_img_system = "img/system/"

dir_img_warui = dir_img_player + "warui/"
dir_img_magic = dir_img_warui + "magic/"

dir_img_tsukushi = dir_img_enemy + "tsukushi/"

dir_background1_img = dir_img_field + "背景1.png"
dir_field_img = dir_img_field + "フィールド.png"
dir_hp_bar_img = dir_img_system + "HPバー.png"
dir_hp_img = dir_img_system + "HP.png"
dir_mp_bar_img = dir_img_system + "MPバー.png"
dir_mp_img = dir_img_system + "MP.png"


#方向
direction_up = "上"
direction_right = "右"
direction_left = "左"
direction_down = "下"

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
first_px = 300
first_py = field_position[1] + 400

p_invincible_time = 120
p_spd = 5
p_img_width = 75
p_img_height = 150
p_hit_width = 75
p_hit_height = 150

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