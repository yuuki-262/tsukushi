import math
from abstruct.object import object

#長方形同士接触してる場合にTrueを返す
def is_hitting(c1:object, c2:object):
    if (c1.x - (c1.hit_width / 2)) < (c2.x + (c2.hit_width / 2)) and (c1.x + (c1.hit_width / 2)) > (c2.x - (c2.hit_width / 2)):
        if (c1.y - (c1.hit_height / 2)) < (c2.y + (c2.hit_height / 2)) and (c1.y + (c1.hit_height / 2)) > (c2.y - (c2.hit_height / 2)):
            return True
    return False

#円と長方形が接触してる場合にTrueを返す
def is_hitting_circle_rect(c1:object, c2:object):
    return is_circle_rotated_rect_collision(c1.x, c1.y, c1.r, c2.x, c2.y, c2.hit_width, c2.hit_height, c2.angle)

#円同士の当たり判定
def is_hitting_circle_circle(c1:object, c2:object):
    return circles_collision(c1.x, c1.y, c1.r, c2.x, c2.y, c2.r)

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

#円同士の当たり判定
def circles_collision(circle1_x, circle1_y, circle1_radius, circle2_x, circle2_y, circle2_radius):
    # 中心間の距離を計算
    distance_squared = (circle1_x - circle2_x) ** 2 + (circle1_y - circle2_y) ** 2

    # 半径の和を計算
    radius_sum = circle1_radius + circle2_radius

    # 中心間の距離が半径の和より小さいか等しい場合、衝突している
    return distance_squared <= radius_sum ** 2


def direction_adjust(obj: object):
    width = (obj.img_height * math.fabs(math.sin(math.radians(obj.angle)))) + (obj.img_width * math.fabs(math.cos(math.radians(obj.angle))))
    hight = (obj.img_width * math.fabs(math.sin(math.radians(obj.angle)))) + (obj.img_height * math.fabs(math.cos(math.radians(obj.angle))))
    return (obj.x - (width / 2), obj.y - (hight / 2))

def sound_se(pygame, se_name):
    pygame.mixer.music.load(se_name)
    pygame.mixer.music.play()

def draw_object(pygame, screen, obj: object, img):
    #original_rect = img.get_rect()
    blit_img = pygame.transform.rotate(img, obj.angle)
    #blit_img_rect = blit_img.get_rect()
    #original_rect = img.get_rect()
    #blit_img_rect.center = original_rect.center
    screen.blit(blit_img, direction_adjust(obj))
