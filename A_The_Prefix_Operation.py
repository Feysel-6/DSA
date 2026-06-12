# t = int(input())

# for _ in range(t):
#     n, k = map(int, input().split())
#     s = input()
    
#     bCount = s.count('B')
    
#     if bCount == k:
#         print(0)
#         continue
    
#     print(1)
    
#     if bCount > k:
#         cnt = 0
#         for i in range(n):
#             if s[i] == 'B':
#                 cnt += 1
#             if cnt == k + 1:
#                 print(i + 1, 'A')
#                 break
#     else:
#         cnt = bCount
#         for i in range(n):
#             if s[i] == 'A':
#                 cnt += 1
#             if cnt == k:
#                 print(i + 1, 'B')
#                 break



t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    bCount = s.count('B')
    
    if bCount == k:
        print("0")
        
    elif bCount > k:
        bRemoved = 0
        toRemove = bCount - k
        
        for i in range(n):
            if s[i] == 'B':
                bRemoved += 1
            if bRemoved == toRemove:
                print(f"1\n{i + 1} A")
                break
                
    else:
        bGain = k - bCount
        aChanged = 0
        
        
        for i in range(n):
            if s[i] == 'A':
                aChanged += 1
            if aChanged == bGain:
                print(f"1\n{i + 1} B")
                break