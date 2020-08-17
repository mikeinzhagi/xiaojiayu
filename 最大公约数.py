def cmd(x, y):
    # if x < y:
    #     x, y = y, x
    # # print("从大到小排列是",x,y)
        while x > 0:
            x, y = y % x, x
        return y




print(cmd(63,56))

# def gcd(a, b):
#     while a != 0:
#         a, b = b % a, a
#
#     return b
#
# print(gcd(49,63))