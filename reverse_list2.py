arr=[5,0,9,8,3,1,4,8]
a=-len(arr)/2
a=int(a)
b=-a-1
print(a,b)
j=-1
i=0
while j >= a and i<=b:
    arr[i] , arr[j] = arr[j] , arr[i]
    j-=1
    i+=1
print(arr)


