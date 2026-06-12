t = int(input())
for _ in range(t):
    s = input()
    a = int(s[0])
    b = int(s[2])

    if a < b:
        print(f"{a}<{b}")
    elif a > b:
        print(f"{a}>{b}")
    else:
        print(f"{a}={b}")