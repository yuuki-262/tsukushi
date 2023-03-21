class hp:
    def __init__(self, hp):
        self.max_hp = hp
        self.hp = hp

    def change_hp(self, value: int):
        if (self.hp + value) <= 0:
            self.hp = 0
        elif (self.hp + value) <= self.max_hp:
            self.hp += value
        else:
            self.hp = self.max_hp