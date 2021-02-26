def Swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def Selection_Sort(N:int, Num:list):
    
    for i in range(N):
        ind = Num.index(min(Num[i:]))
        Swap(Num,ind,i)
        
    return  

Num = [7,3,4,2,5,6,1]
N = len(Num)
Selection_Sort(N, Num)

print(Num)

# 이승현
'''
arr=[]
for _ in range(int(input())):
    arr.append(int(input()))

for i in range(len(arr)):
    tmp = min(arr[i:])
    arr.remove(tmp)
    arr.insert(i,tmp)

print(arr)
'''

# 조민준
'''
arr = [7,3,4,2,5,6,1]

for i in range(len(arr)):
    tmp = arr.index(min(arr[i:len(arr)]))
    arr[i], arr[tmp] = arr[tmp], arr[i]
'''