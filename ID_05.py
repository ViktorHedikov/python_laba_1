n = input()
invN = n[::-1]  # инвертирование строки
m = ""          # определение пустой строки m
for char in invN:
    if char == '0':
        continue
    else:
        m = m + char  # добавление символа к строке m
print(m)
