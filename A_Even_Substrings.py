n = int(input())
s = input()
evenS = 0
for i in range(n):
    if not int(s[i]) % 2:
        evenS += i + 1
print(evenS)