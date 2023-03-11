a, b, n = map(int, input().split())
s1 = a * n
s2 = b * n
if s2 >= 100:
    s1 = s1 + s2//100
    s2 = s2 % 100
print(s1, s2)