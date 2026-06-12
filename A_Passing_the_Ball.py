t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    for char in s:
        if char == 'R':
            count += 1
        else:
            break
    print(count + 1)