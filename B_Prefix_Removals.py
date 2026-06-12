from collections import Counter, deque
t = int(input())
for _ in range(t):
    a = input()
    count = Counter(a)
    q = deque(a)
    for char in a:
        if count[char] > 1:
            count[char] -= 1
            q.popleft()
        else:
            break
    print(''.join(q))