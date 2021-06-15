eng_to_rus ={
    "dog": "собака",
    "cat": "кот",
     "book": "книга",
     "cucumber": 'огурец'
}

print(eng_to_rus["dog"])
print(eng_to_rus["book"])
print(eng_to_rus["cucumber"])


rus_to_eng ={
    "собака": "dog",
     "кот": "cat",
     "книга": "book",
     'огурец': "cucumber"
}

while True:
    lang = input("Язык для перевода: ")
    if lang == "eng":
        word = input("для перевода ")
        try:
         print(eng_to_rus[word])
        except KeyError:
         print("Нет слова в словаре, Хотит добавить?")
         option  = input()
        if option == "y":
            eng_to_rus[word] = input(f"перевод для слова {word} ")




    if lang == "rus":
            word = input("для перевода ")
    try:
        print(rus_to_eng[word])
    except KeyError:
        option = input()
        print("Нет слова в словаре, Хотит добавить?")
        if option == "y":
            rus_to_eng[word] = input(f"перевод для слова  {word} ")

