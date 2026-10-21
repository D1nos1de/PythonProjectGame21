class Player:
    def __init__(self,name,hand):
        self.name = name
        self.point = 0
        self.hand = hand

    def calculate_points(self):
        self.point = 0
        for h in self.hand:
            if h.isdigit():
                self.point += int(h)
            else:
                self.point += 10
        if 'a' in self.hand and self.point > 21:
            self.point -= 10

        return self.point
