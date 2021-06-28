# sum = 0
# i = 0
# num = int(input('请输入数字'))
# while True:
#     if i <= num:
#         sum = sum + i
#         i = i + 1
#     else:
#         break
# print("1到", num, "的和是", sum)


sum = 0
num = int(input('请输入数字'))
for i in range(num + 1):
    sum = sum + i
print("1到", num, "的和是", sum)




