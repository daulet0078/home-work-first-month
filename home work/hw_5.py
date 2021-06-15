eng_to_rus ={
    "dog": "собака",
    "cat": "кот",
     "book": "книга",
     "cucumber": 'огурец'
}




rus_to_eng ={
    "собака": "dog",
     "кот": "cat",
     "книга": "book",
     'огурец': "cucumber"
}

while True:
    lang = input("Язык для перевода: ")
    if lang == "eng":
        word = input("слово для перевода: ")
        try:
         print(eng_to_rus[word])
        except KeyError:
         print("Нет слова в словаре но есть русско англиском: ")
         select = input()
         if select == "y":
             print(rus_to_eng[word])





    if lang == "rus":
        word = input("слово для перевода:  ")
        try:
            print(rus_to_eng[word])
        except KeyError:
            print("Нет слова в словаре но есть англиско русском: ")
            select = input()
            if select == "y":
             print(eng_to_rus[word])