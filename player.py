class Player:
    def __init__(self,hand):
        self.point = 0
        self.hand = hand

    def calculate_points(self):
        self.point = 0
        for h in self.hand:
            if h.isdigit():
                self.point += int(h)
            elif h != 'a':
                self.point += 10
            else:
                self.point += 11
        for _ in range(self.hand.count('a')):
             if self.point > 21:
                  self.point -= 10

        return self.point
