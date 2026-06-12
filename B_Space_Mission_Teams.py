import math
n,d = map(int,input().split())
p = list(map(int,input().split()))
p.sort()

left, right = 0 , n-1
count = 0

while left <= right:
    curMax = p[right]
    k = math.ceil((d + 1) / curMax)

    if left + (k - 1) <= right:
        count += 1
        left += (k - 1)
        right -= 1
    else:
        break

print(count)