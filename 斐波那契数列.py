# a = 0
# b = 1
# while b < 55555:
#     print(b)
#     a, b = b, a+b


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
#
# fib(100000)  # 取值范围可以任意


N = [1]  # 先把第一行给定义好
for i in range(20):  # 打印10行
    # 从这里开始我们就要把list转换为一个剧中的字符串打印出来
    L = N.copy()  # 我们需要吧N复制给L,而不能直接L = N，因为这样L和N会在同一个地址，后续算法就会出错
    for j in range(len(L)):  # 遍历和转化
        temp = str(L[j])
        L[j] = temp
    l = ' '.join(L).center(100)  # 组合和剧中一起写
    print(l)  # 这里就是打印l了
    N.append(0)  # 因为复制之后L是L，N是N，所以我们还是继续在N末尾加0
    N = [N[k] + N[k-1] for k in range(i+2)]
