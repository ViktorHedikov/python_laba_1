n = input()
i = 0
sum = 0
while i < 4:
    if int(n) < 0:  # если введённое число отрицательное
        sum = sum + int(n[i + 1])
    else:  # если введённое число положительное
        sum = sum + int(n[i])
    i = i + 1
    # выводим результат
print(sum)