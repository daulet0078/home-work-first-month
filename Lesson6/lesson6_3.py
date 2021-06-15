def int_input(text):
    while True:
        age = input(text)
        try:
            age = int(age)
            break
        except Exception:
            pass

    print(age)


int_input("Введие ваш возраст! ")
int_input("dfv ytkmpz")