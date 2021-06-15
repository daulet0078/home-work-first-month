def main():
    print("Игра началась!")
    while True:
        try:
            num = int(input())
            if num < 8 or num > 15:
                print("Холодно")
            else:
                print("Горячо")
                if num == 12:
                    print("Ты выйграл!")
                    break
        except Exception:
            pass









while True:
    print("Угадай число")
    print("Если хочешь играть напиши-yes ")
    print("Если нет напиши-no")
    select = input("Выбор: ")
    try:
        if select == 'yes':
            main()
            break
    except Exception:
        pass