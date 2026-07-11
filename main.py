import random as rnd


list_deck = [6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'j','j','j','j','l','l','l','l','k','k','k','a','a','a','a']


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.hand = []

    def accept_card(self,card):
        self.hand.append(card)


class Deck:
    def __init__(self,list_card):
        self.list_card = list_card

    def shuffle(self):
        rnd.shuffle(self.list_card)

    def deal(self):
        return self.list_card.pop(-1)


class Game:
    def __init__(self):
        self.deck = Deck(list_deck)
        self.players = []
    def play(self):

        self.deck.shuffle()

        starting = int(input("введите число из перечня\n 1.Начать игру\n"))

        naming = str(input("Введите свое имя: "))
        if naming != '':
            player1 = Player(f'{naming}', 100)
            enemy = Player('Enemy', 100)
            diller = Player('Diller', 100)

            self.players.append(player1)
            self.players.append(diller)
            self.players.append(enemy)

            for player in self.players:
                player.accept_card(self.deck.deal())
                player.accept_card(self.deck.deal())

            print('Это твои карты',player1.hand)

game1 = Game()
game1.play()