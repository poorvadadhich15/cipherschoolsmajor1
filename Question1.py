def twoSum(arr, target):
        pos = {}
        for i in range(len(arr)):
            if target - arr[i] in pos:
                       return [pos[target - arr[i]],i]
            else:
                       pos[arr[i]]=i 
l = []
n = int(input("Enter no. of elements:"))
print("Enter list elements:\n")
for i in range(0,n):
    ele = int(input())
    l.append(ele)
target = int(input("Enter target:"))
                       
print(twoSum(l,target))
