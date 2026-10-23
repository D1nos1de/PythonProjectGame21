def start_game():
    print('Добро пожаловать в игру «21»!')
    print('Выберите действие:')
    print('1 — Начать игру')
    print('2 — Узнать правила')

def show_card(player):
    print(f'Это твои карты {player.hand} а это то сколько они стоят {player.point}.')

def show_card_d(dill):
    print(f'Это карта Диллера {dill.hand} а это то сколько онa стоит {dill.point}.')

def lose():
    print('Поражение это потому что ты человек')

def win():
    print('Победа это потому что ты человек')

def show_rule():
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

def show_menu():
    print()
    print('Если хотите взять еще одну карту напишите - 0')
    print('Если же вам уже хватит то - 1')
    print('Если хотите взять несколько карт напишите сколько - ?')



def result(player,dill,deck):
    dill.calculate_points()
    show_card_d(dill)

    while dill.point < 17:
        dill.hand.append(deck.give_card())
        dill.calculate_points()
        show_card_d(dill)

    if dill.point < player.point < 21:
        win()
    elif player.point < dill.point < 21:
        lose()
    elif player.point > 21:
        lose()