name = input()
age = int(input())
hobby = input()

if name == "Ali" and age > 17 and  hobby == " 1% of tiktok":
    print("ТЫ али")
else:
    print("Ты не али, Ты школьник")


if name == "Ali" or age > 17 or hobby == " 1% of tiktok":
    print("Ты либо Али, либо старш 17, либо твое хобби TIktok")
else:
    print("ты вообще не подшодишь под эти условия!")