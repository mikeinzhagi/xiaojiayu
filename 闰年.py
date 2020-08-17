while True:
    s = input("请输入年份")
    if s.isdigit():
        year = int(s)
        if (year % 4 == 0) and (year % 100 !=0):
            print(year,"是闰年")
            print("game over")
            break
        else:
            print(year, "不是闰年")
    else:
        print("please input a year")