s = input()
t = input()

if len(s) != len(t):
    print('No')
    exit()

vowels = 'aieou'
possible = True
p1 = 0

while p1 < len(s):
    if s[p1] in vowels and t[p1] in vowels:
        p1 += 1
    elif not s[p1] in vowels and not t[p1] in vowels:
        p1 += 1
    else:
        possible = False
        break
print('Yes' if possible else 'No')