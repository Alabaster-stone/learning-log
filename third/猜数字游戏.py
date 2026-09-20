import random 
x = random.randint(1,10)

while True:
    y = int(input("请输入猜的数字0-10之间："))
    if x == y:
        print("恭喜你猜对了")
        break
    elif x > y:
        print("请再大一点")
    else:
        print("请再小一点")