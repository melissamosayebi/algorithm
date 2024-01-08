def type_int():

    while True:
        try:
            x=int(input("give a number: "))
        except ValueError:
            print("the num wasn't int")
        else:
            print(f"your number is {x}")
            continue
type_int()



    