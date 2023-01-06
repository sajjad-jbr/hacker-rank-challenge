arr = map(float, input().split())
arr = list(arr)
x = int(input())
sum = 0
for index,p in enumerate(arr):
    sum += ((x) ** (len(arr)-index-1) ) * p

print(sum)