t = int(input())

for _ in range(t):
    word = input()
    print(f"{word[0]}{len(word[1:-1])}{word[-1]}" if len(word) > 10 else word)