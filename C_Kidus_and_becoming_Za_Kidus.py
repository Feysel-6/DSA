import math

t = int(input())

for _ in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    deadline = list(map(int, input().split()))

    pairs = list(zip(deadline, health))
    pairs.sort() 

    left, right = 1, max(health)

    while left < right:
        mid = (left + right) // 2

        seconds = 0
        ok = True

        for d, h in pairs:
            seconds += math.ceil(h / mid)
            if seconds > d:  
                ok = False
                break

        if ok:
            right = mid     
        else:
            left = mid + 1  

    print(left)