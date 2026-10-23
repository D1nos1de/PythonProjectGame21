from random import shuffle

class GameDeck:
    def __init__(self):
        self.deck = ['2','3','4','5','6', '7', '8', '9', '10', 'j', 'q', 'k', 'a'] * 4

    def give_card(self):
        return self.deck.pop()

    def shuffle_card(self):
        shuffle(self.deck)

