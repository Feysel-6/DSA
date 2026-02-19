matrix = [list(map(int,input().split())) for _ in range(5)]
locate = []
for r, row in enumerate(matrix):
    if 1 in row:
        c = row.index(1)
        locate.extend([r,c])

x = abs(locate[0] - 2) 
y = abs(locate[1] - 2)

print(x+y)