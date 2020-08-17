sum = 0
i = 1
while True:
    if i <= 10000:
        sum = sum + i
        i = i + 1
        answer = str(sum)
        num = str(i-1)
    else:
        break
print("1到"+(num)+"的和是"+(answer))