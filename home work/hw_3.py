print("Калькулятор")
number_1 = int(input("Первое число:   "))
number_2 = int(input("Второе число:   "))
print("Выбирите действие:")
print("1.Сложение")
print("2.Вычитание")
print("3.Деление")
print("4.Умножение")
selet = int(input())
if selet == 1:
    print(number_1 + number_2)
if selet == 2:
    print(number_1 - number_2)
if selet == 3:
    print(number_1 / number_2)
if selet == 4:
    print(number_1 * number_2)
if selet  > 4:
    print("Не верное действие")