import random as rnd


list_deck = [6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'jack','jack','jack','jack','lady','lady','lady','lady','king','king','king','ace','ace','ace','ace']


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def accept_card(self,card):
        self.hand.append(card)

    def count_point(self):
        for card in self.hand:
            if card == 'j' or card == 'l' or card == 'k':
                self.points += 11
            elif type(card) == int:
                self.points += int(card)
            else:
                if self.points >= 11:
                    self.points += 1
                else:
                    self.points += 11
        return self.points


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
            player1 = Player(f'{naming}')
            enemy = Player('Enemy')
            diller = Player('Diller')

            self.players.append(player1)
            self.players.append(diller)
            self.players.append(enemy)

            for player in self.players:
                player.accept_card(self.deck.deal())
                player.accept_card(self.deck.deal())

            print('Это твои карты',player1.hand[0],player1.hand[1],'и общее число очков за эти карты',player1.count_point())

game1 = Game()
game1.play()