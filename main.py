from player import Player
from deck import GameDeck
from game import *

deck1 = GameDeck()
deck1.shuffle_card()

diller1 = Player([deck1.give_card()])
diller1.calculate_points()

start_game()

glob_choice = input()
if glob_choice == '1':

    player1 = Player([deck1.give_card(),deck1.give_card()])
    player1.calculate_points()

    show_card(player1)
    show_card_d(diller1)

    diller1.hand.append(deck1.give_card())

    show_menu()

    choice = input()

    if choice == '0':

        player1.hand.append(deck1.give_card())
        player1.calculate_points()
        show_card(player1)

        if player1.point > 21:
            lose()
        else:
            result(player1,diller1,deck1)



    elif choice == '1':
        result(player1,diller1,deck1)

    else:
        for _ in range(int(choice)):
            player1.hand.append(deck1.give_card())
        player1.calculate_points()
        show_card(player1)

        if player1.point > 21:
            lose()
        else:
            result(player1,diller1,deck1)

elif glob_choice == '2':
    show_rule()
else:
    print('Вы ввели не то что нужно попробуйте еще раз')

