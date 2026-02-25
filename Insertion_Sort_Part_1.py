def insertionSort1(n, arr):
    maximum = arr[n-1]
    j = n - 2
    while j >= 0 and arr[j] > maximum:
        arr[j+1] = arr[j]
        print(*arr)
        j -= 1
    
    arr[j+1] = maximum
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)