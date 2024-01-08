f=[3,6,12,14,7]
h=f[ : ]
i=0
j=0
z=0
av=int(len(f)/2)

for i in range(len(f)):
       f[-(i+1)]=f[i]
       i=i+1

for j in range(len(h)):
       h[j]=h[-(j+1)]
       j=j+1

m= h[0:av]
n= f[av: ]


for z in range(len(n)):
       m.append(n[z])
       z += 1
print(m)
