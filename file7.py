lst=[]
try: 
    a=int(input("how many?"))
except NameError and ValueError:
    pass
else:
     for i in range(a):
         lst.append(input("names?").lower())
    
print(lst)