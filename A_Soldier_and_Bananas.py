k,n,w = map(int, input().split())
total = 0
for i in range(1, w + 1):
    total += k * i
borrow = total - n
print(max(borrow,0))