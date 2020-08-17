day = 1
while day <= 7:
    answer = input("今天又好好学习吗？")
    if answer != "yes":
        break
    day += 1
else:
    print("very good")