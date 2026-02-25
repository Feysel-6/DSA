def countSwaps(a):
    numSwaps = 0
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                numSwaps += 1
    print(f"Array is sorted in {numSwaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[n-1]}")
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
