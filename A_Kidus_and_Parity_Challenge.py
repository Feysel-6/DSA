t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int,input().split())
    even = []
    odd = []
    for num in a:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    print(len(even) if len(even) < len(odd) else len(odd))