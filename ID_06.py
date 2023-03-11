n = input()
a = n[0]
b = n[1]
c = n[2]
d = n[3]
s1 = a + b + c + d
s2 = d + c + b + a
s3 = a + c + b + d
s4 = b + a + d + c
S = int(s1) + int(s2) + int(s3) + int(s4)
print(S)
