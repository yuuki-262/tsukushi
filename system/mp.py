class mp:
    def __init__(self, mp):
        self.max_mp = mp
        self.mp = mp

    def change_mp(self, value: int):
        if (self.mp + value) <= self.max_mp:
            self.mp += value
        elif (self.mp + value) <= 0:
            self.mp == 0
        else:
            self.mp = self.max_mp