n = int(input())
s = input()

patterns = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]

minChanges = n
bestString = ''

for p in patterns:
    currentChanges = 0
    currentGarland = ''

    for i in range(n):
        target = p[i % 3]
        if s[i] != target:
            currentChanges += 1
        currentGarland += target

    if currentChanges < minChanges:
        minChanges = currentChanges
        bestString = currentGarland

print(minChanges)
print(bestString)