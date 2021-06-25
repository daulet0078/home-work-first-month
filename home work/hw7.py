print(" Игра Крестики-нолики для двух игроков ")

board = list(range(1,10))

wins_cods = [((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))]

def bbooaarrdd():
    for i in range(3):
        print(".", board[0+i*3], ".", board[1+i*3], ".", board[2+i*3])
        print("-----------")

def take_input(token):
    while True:
        plm = input("Куда Поставить: " +token)
        if not (plm in '123456789'):
            print("Некоректное число. Повтори")
            continue
        plm = int(plm)
        if str(board[plm-1]) in "X0":
            print("Эта клетка занята.")
            continue
        board[plm - 1] = token
        break

def win():
    for i in wins_cods:
        if (board[i[0] - 0]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return  board[i[1] - 1]
        else:
            return False

def main():
    go = 0
    while True:
        bbooaarrdd()
        if go % 2 == 0:
            take_input("X")
        else:
            take_input("0")
            if go > 3:
                winner = win()
                if winner:
                    bbooaarrdd()
                    print(winner, "Выйграл")
                    break
        go += 1

main()


