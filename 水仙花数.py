# for i in range(100,1000):
#     b = str(i)
#     a = list(b)
#     x = int(a[0])
#     y = int(a[1])
#     z = int(a[2])
#     if x**3 + y**3 + z**3 == i:
#         print(i)

for i in range(100,1000):
    x = i // 100
    y = (i - 100*x) // 10
    z = i - 100*x - 10*y
    if x ** 3 + y ** 3 + z ** 3 == i:
        print(i, end=' ')