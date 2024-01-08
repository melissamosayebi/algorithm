import random
import time
user = input("what is your name ?").lower().strip().title()
time.sleep(1)
s=print(user , "keep a num between 1_99 in your mind")
time.sleep(2)
print("my guess is 50")
a=input("is this your num ? (y or n )")
if a == "y" or a == "Y":
    print("your num is" , 50 )
else:
    c = input('your num is bigger or smaller ?(b or s )')
while a != "y" or a != "Y":
    if c=="b":
       javab = random.randint(51,99)
       print('my guess is' , javab)
       a=input('is this your num ? (y or n )')
       c = input('your num is bigger or smaller ?(b or s )')
       while a != "y" or a != "Y":
           if c=="b" :
              javab = javab + 10
              print('my guess is' , javab)
              a=input('is this your num ? (y or n )')
              c = input('your num is bigger or smaller ?(b or s )')
              if c=="b":
                 javab = javab + 5
                 print('my guess is' , javab)
                 a=input('is this your num ? (y or n )')
                 c = input('your num is bigger or smaller ?(b or s )')
                 if c=="b":
                    javab = javab + 2
                    print('my guess is' , javab)
                    a=input('is this your num ? (y or n )')
                    c = input('your num is bigger or smaller ?(b or s )')
                    if c=="b":
                       javab = javab + 1
                       print('my guess is' , javab)
                       a=input('is this your num ? (y or n )')
                       c = input('your num is bigger or smaller ?(b or s )')
                    else:
                       javab = javab - 1
                       print('my guess is' , javab)
                       a=input('is this your num ? (y or n )')
                       c = input('your num is bigger or smaller ?(b or s )')
                 else:
                    javab = javab - 2
                    print('my guess is' , javab)
                    a=input('is this your num ? (y or n )')
                    c = input('your num is bigger or smaller ?(b or s )')
              else:
                 javab = javab - 5
                 print('my guess is' , javab)
                 a=input('is this your num ? (y or n )')
                 c = input('your num is bigger or smaller ?(b or s )')
    elif c=="s":
        javab = random.randint(1,49)
        print('my guess is' , javab)
        a=input('is this your num ? (y or n )')
        c = input('your num is bigger or smaller ?(b or s )')
        while a != "y" or a != "Y":
           if c=="s" :
              javab = javab - 5
              print('my guess is' , javab)
              a=input('is this your num ? (y or n )')
              c = input('your num is bigger or smaller ?(b or s )')
              if c=="s":
                 javab = javab - 5
                 print('my guess is' , javab)
                 a=input('is this your num ? (y or n )')
                 c = input('your num is bigger or smaller ?(b or s )')
                 if c=="s":
                    javab = javab - 2
                    print('my guess is' , javab)
                    a=input('is this your num ? (y or n )')
                    c = input('your num is bigger or smaller ?(b or s )')
                    if c=="s":
                       javab = javab - 1
                       print('my guess is' , javab)
                       a=input('is this your num ? (y or n )')
                       c = input('your num is bigger or smaller ?(b or s )')
                    else:
                       javab = javab + 1
                       print('my guess is' , javab)
                       a=input('is this your num ? (y or n )')
                       c = input('your num is bigger or smaller ?(b or s )')
                 else:
                    javab = javab + 2
                    print('my guess is' , javab)
                    a=input('is this your num ? (y or n )')
                    c = input('your num is bigger or smaller ?(b or s )')
              else:
                 javab = javab + 5
                 print('my guess is' , javab)
                 a=input('is this your num ? (y or n )')
                 c = input('your num is bigger or smaller ?(b or s )')



print("I won")
       
print('good luck')
