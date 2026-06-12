from collections import defaultdict
n, k = map(int, input().split())

answers = []
for _ in range(n):
    answers.append(input())

grades = list(map(int, input().split()))

total = 0

for i in range(k):
    count = defaultdict(int)
    
    for j in range(n):
        count[answers[j][i]] += 1

    freq = max(count.values())
    
    total += grades[i] * freq

print(total)