import sys

word = sys.stdin.read();
swappedWord = ''
for char in word:
    if char.isupper():
        swappedWord += char.lower()
    else:
        swappedWord += char.upper()
print(swappedWord)
