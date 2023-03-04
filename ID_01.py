n = int(input())

# получаем вторую справа цифру
if n >= 0:
    dig2R = (n // 10) % 10
else:
    dig2R = (-n // 10) % 10

# выводим результат
print(dig2R)