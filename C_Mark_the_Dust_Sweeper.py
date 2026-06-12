t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    
    count = 0
    conZeros = 0
    left,right = 0,0

    while right < n - 1:
        if nums[right] == 0:
            conZeros += 1
        else:
            right += 1
            left += 1

        
    print(count)
