import math
from abstruct.object import object

#接触してる場合にTrueを返す
def is_hitting(c1:object, c2:object):
    if (c1.x - (c1.hit_width / 2)) < (c2.x + (c2.hit_width / 2)) and (c1.x + (c1.hit_width / 2)) > (c2.x - (c2.hit_width / 2)):
        if (c1.y - (c1.hit_height / 2)) < (c2.y + (c2.hit_height / 2)) and (c1.y + (c1.hit_height / 2)) > (c2.y - (c2.hit_height / 2)):
            return True
    return False

#円と長方形が接触してる場合にTrueを返す
def is_hitting2(c1:object, c2:object):
    return is_circle_rotated_rect_collision(c1.x, c1.y, c1.r, c2.x, c2.y, c2.width, c2.height, c2.angle)

def rotate_point(cx, cy, px, py, angle):
    s = math.sin(angle)
    c = math.cos(angle)
    px -= cx
    py -= cy
    new_x = px * c - py * s
    new_y = px * s + py * c
    px = new_x + cx
    py = new_y + cy
    return px, py

def is_circle_rotated_rect_collision(cx, cy, r, rect_center_x, rect_center_y, rect_width, rect_height, angle):
    # 円の座標を逆方向に回転
    new_cx, new_cy = rotate_point(rect_center_x, rect_center_y, cx, cy, -angle)

    # 軸平行な長方形として衝突判定を行う
    rx1 = rect_center_x - rect_width / 2
    ry1 = rect_center_y - rect_height / 2
    rx2 = rect_center_x + rect_width / 2
    ry2 = rect_center_y + rect_height / 2

    return is_circle_rect_collision(new_cx, new_cy, r, rx1, ry1, rx2, ry2)

def is_circle_rect_collision(cx, cy, r, rx1, ry1, rx2, ry2):
    nearest_x = max(rx1, min(cx, rx2))
    nearest_y = max(ry1, min(cy, ry2))
    distance = math.sqrt((cx - nearest_x)**2 + (cy - nearest_y)**2)
    return distance <= r

def direction_adjast(obj: object):
    return (obj.x - (obj.img_width / 2), obj.y - (obj.img_height / 2))

def sound_se(pygame, se_name):
    pygame.mixer.music.load(se_name)
    pygame.mixer.music.play()

