t = int(input())
phone_book = {}
for _ in range(t):
    entry = input()
    name, number = entry.split()
    phone_book[name] = int(number)
    
while True:
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except EOFError:
        break
