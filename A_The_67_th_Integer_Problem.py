t = int(input())
for _ in range(t):
    x = int(input())
    y = 0
    if x > 0:
        if x == 67:
            y = x
        else:
            y = x + 1
    elif x < 0:
        y = x + 1
    print(y)