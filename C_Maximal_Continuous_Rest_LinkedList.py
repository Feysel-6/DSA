class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n = int(input())
hours = list(map(int,input().split()))

head = Node(0)
current = head

for hour in hours:
    current.next = Node(hour)
    current = current.next

head = head.next
current.next = head

ans = 0
count = 0
current = head

for _ in range(2 * n):
    if current.val == 1:
        count += 1
    else:
        ans = max(ans,count)
        count = 0
    current = current.next

ans = max(ans, count)  
print(ans)