file = open("./word.text", "a+", encoding="UFT-8")

def translate(dictinory):
    word = input("Слова для перевода")
    try:
        print(f'Слово на {word}: {dictinory[word]}')
    except KeyError:
        print("Слова нет в словаре, хотете добавить")
        option = (input())
        if option == "y":
            dictinory[word] = input(f"Перевод для слова {word}")
            print(f"{word}:{dictinory[word]}")
            file.write(f'{word:{dictinory[word]}}')

while True:
    option = int(input())
    if option == 1:
        translate(dictinory=)
    else:
        break

file.close()


