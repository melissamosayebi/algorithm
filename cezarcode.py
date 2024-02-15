from string import ascii_letters as ac
file=open("[filename.txt]","r")
content=file.read()
st=""
for i in content:
    if i in ac:
        s=ac.index(i)
        st+=ac[(s+2)%52]
    else:
        st+=i
print(st)
