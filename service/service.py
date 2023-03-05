from abstruct.object import object

#接触してる場合にTrueを返す
def is_hitting(c1:object, c2:object):
    if (c1.x - (c1.hit_width / 2)) < (c2.x + (c2.hit_width / 2)) and (c1.x + (c1.hit_width / 2)) > (c2.x - (c2.hit_width / 2)):
        if (c1.y - (c1.hit_height / 2)) < (c2.y + (c2.hit_height / 2)) and (c1.y + (c1.hit_height / 2)) > (c2.y - (c2.hit_height / 2)):
            return True
    return False

def direction_adjast(obj: object):
    return (obj.x - (obj.hit_width / 2), obj.y - (obj.hit_height / 2))



