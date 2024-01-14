def sahih(x):
    if x==0:
        print(0,end=" ") 
    else:
        print(x,end=" ")
        sahih(x+1)
        print(-x,end=" ")
sahih(-3)