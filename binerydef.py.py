def binery(a):
    count=-1
    s=0
    while a>0:
        b=a%2
        s=(s*0.1)+b
        count+=1
        a//=2
    s*=10**count
    s=int(s)
    print(s)
binery(int(input(": ")))
