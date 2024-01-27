def limit(a,min,max):
    f=([a[i] for i in range(len(a)) if min<=a[i]<=max ])
    print(f)
limit([2,4,8,6,7,1,0,5],2,8)
