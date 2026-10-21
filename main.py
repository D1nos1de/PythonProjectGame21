from player import Player
from deck import GameDeck

deck1 = GameDeck()
deck1.shuffle()

print('Добро пожаловать в игру «21»!')
print('Выберите действие:')
print('1 — Начать игру')
print('2 — Узнать правила')

choice = input('Ваш выбор: ')

if choice == '1':
    print('Отлично! Давайте начнём!')
    print('Введите своё имя:')

    player1 = Player(input(),[deck1.give_card() for _ in range(2)])
    player1.calculate_points()

    print(f'Это твои карты {(player1.hand)} а это то сколько они стоят {player1.point}.')
    if player1.point > 21:
        print('Ебать ты долбаеб как ты проебал')
    elif player1.point == 21:
        print('Красава')

    print('Если тебе нужны еще карты напиши 1')
    count_card_give = int(input())

    if count_card_give == 1:
        for _ in range(10):
            player1.hand += [deck1.give_card()]
            player1.calculate_points()
            print('Если тебе нужны еще карты напиши 1')
            print(f'Это твои карты {(player1.hand)} а это то сколько они стоят {player1.point}.')
            if player1.point > 21:
                print('Ебать ты долбаеб как ты проебал')
                break
            elif player1.point == 21:
                print('Красава')

            print('Если тебе нужны еще карты напиши 1')
            if int(input()) == 1:
                continue
            else:
                break
else:
    print('Правила игры «21»')
    print('''
    Цель игры — набрать как можно больше очков, не превышая 21.

    В начале игры каждому игроку раздаются две карты.
    Числовые карты оцениваются по своему номиналу.
    Валеты, дамы и короли приносят по 10 очков.
    Туз приносит 11 очков, но если сумма очков превышает 21,
    его стоимость может быть уменьшена до 1 очка.

    Если сумма очков игрока превышает 21, он проигрывает.

    Ваша задача — набрать больше очков, чем соперник,
    не превысив при этом 21 очко.

    Удачи в игре!
    ''')
    print('Теперь вы готовы сыграть!')