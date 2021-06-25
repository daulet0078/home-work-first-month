login = input()
password = input()

file = open("./logins.py", 'a+', encoding='UTF-8')

lines = file.readlines()

for i in lines:
    if i[:-1] == f"{login}:{password}":
        print('Вы аторизованы')

file.close()