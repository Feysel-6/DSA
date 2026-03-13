n, g = map(int,input().split())
a = list(map(int,input().split()))
l = 0
window_sum = 0
segment = 0
for r in range(n):
    window_sum += a[r]  
    while window_sum > g:
        window_sum -= a[l]
        l += 1  
    segment = max(segment, r-l+1)
print(segment)
