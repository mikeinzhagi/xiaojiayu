# print("Hello World1")
# print("Hello World2")
# print("Hello 你好啊")
# import xToolkit
# a = xToolkit.xdatetime.shape(2021-1-1)
# print (a)
# b = xToolkit.xstring.check("6222600260001072444").is_bank_number
# print (b)
# c = xToolkit.xdatetime.get()
# print (c)
# d = xToolkit.xdatetime.get(2020, 0, genre="Y").begin_end
# print (d)
# e = xToolkit.xstring.dispose('中国人民解放军海军工程大学').part(cut_all=False)
# print (e)

import time
from xToolkit import xthreading
# 函数一
def function_1(a, b, c):
    time.sleep(1)
    return a * 2, b * 2, c * 2

# 函数二
def function_2(a, b):
    time.sleep(1)
    return a * 2, b * 2

# 函数三
def function_3(a):
    time.sleep(1)
    return a * 2

# 函数四
def function_4():
    time.sleep(1)
    return 0


st = time.time()
result = xthreading([function_1, 1, 1, 1], [function_2, 2, 2], [function_3, 2], [function_4])
print(result[0])
print(result[1])
print(result[2])
print(result[3])
et = time.time()
print("运行时间：{}".format(et - st))