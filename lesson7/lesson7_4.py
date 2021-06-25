def juicer(fruit):
    if fruit == "banana":
        return "banana juice"
    elif fruit == "apple":
        return "apple juice"
    elif fruit ==  "orange":
        return "orange juice"

def mixer(juice_list):
    fruit_dict = {
        "apple": 0,
        "orange": 0,
        "banana": 0
    }
    for i in juice_list:
        if i =="banana juice":
            fruit_dict['banana'] += 1
            if i == "orange juice":
                fruit_dict['orange'] += 1
                if i =="apple juice":
                    fruit_dict['apple'] += 1

for i in range(3):
    juice = juicer(input())
    print(juice) 