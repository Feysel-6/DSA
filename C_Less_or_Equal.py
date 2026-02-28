n, k = map(int,input().split())
sequence = list(map(int,input().split()))
sequence.sort()
if k == 0:
    if sequence[0] == 1:
        print(-1)
    else:
        print(sequence[0] - 1)
elif k == n:
    print(sequence[n-1])
else:
    if sequence[k-1] == sequence[k]:
        print('-1')
    else:
        print(sequence[k] - 1)
