if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    setNew = set(arr)
    arr = list(setNew)
    arr.sort(reverse=True)
    print(arr[1])