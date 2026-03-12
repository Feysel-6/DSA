n, t = map(int, input().split())
times = list(map(int, input().split()))

window_sum = 0
books = 0
l = 0

for r in range(n):
    window_sum += times[r]

    while window_sum > t:
        window_sum -= times[l]
        l += 1

    books = max(books, r - l + 1)

print(books)
