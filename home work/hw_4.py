print("Todo list for 7 days ")
print("Как заполнять:")
print("Сделал-(+), Не сделал-(-)")
for i in range(7):
    first = input("1.Проснуться: ")
    if first  == "-" :
        print("День провален.")
    else:
        print("Выполнено.")
        sescond = input("2.Умыться: ")
        if sescond == "-":
            print("День провален.")
        else:
            print("Выполнено.")
            third = input("3.Покушать: ")
            if third == "-":
                print("День провален.")
            else:
                print("Выполнено.")
                fourth = input("4.Одеться нормально: ")
                if fourth == "-":
                    print("День провален.")
                else:
                    print("Выполнено.")
                    fifth = input("5.Пойти и посидеть на работе: ")
                    if fifth == "-":
                        print("День провален.")
                    else:
                        print("Выполнено.")
                        sixth = input("6.После работы одохнуть или раслабится:")
                        if sixth == "-":
                            print("День провален.")
                        else:
                            print("Выполнено.")
                            seventh = input("7.Вернуться домойю:" )
                            if seventh == "-":
                                print("День провален.")
                            else:
                                print("Выполнено.")









