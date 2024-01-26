a=int(input(": "))
count=0
s=0
while a//2>0:
    b=a%2
    s=(s*0.1)+b
    count+=1
    a//=2
s=(s*0.1)+a
s*=10**count
s=int(s)
print(s)