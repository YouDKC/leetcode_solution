# n=int(input())
# arr = []
# while n>0:
#     arr.append([int(i) for i in input().strip().split(',')])
#     n-=1
import math
n = 6
arr = [[1,2,3,5,7,6],
     [2,1,4,5,7,4],
     [3,4,5,6,3,6],
     [2,3,1,4,6,8],
     [5,6,1,4,6,2],
     [4,2,4,1,1,6]]
times = math.ceil(n/2)
def find(res,row,col,count):
    if row+1<n and col <n:
        print('row',row,col)
        res1 = find(res + arr[row + 1][col], row + 2, col,count+1)
    else:
        if count < times:
            res1 = 0
        else:
            res1 =res

    if col+1<n and row<n:
        print('col', row, col)
        res2 = find(res + arr[row][col+1], row,  col+2, count+1)
    else:
        if count < times:
            res2 = 0
        else:
            res2 = res

    if res1*res2==0:
        return max(res1,res2)
    else:
        return min(res1,res2)
result = float('inf')
for col in range(n):
    result = min(result,find(0,0,col,1))

print(result)


