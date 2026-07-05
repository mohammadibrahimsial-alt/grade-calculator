a=int(input("enter your grade"))
if a<=100 and a>=91:
    print("you got an A star")
elif a<=90 and a>=81:
    print("you got a B")
elif a<=80 and a>=71:
    print("you got a c")
elif a<=70 and a>=61:
    print("you got a d")
elif a<=60 and a>=51:
    print("you got an e")
elif a<=50 and a>=0:
    print("you failed")
else:
    print("please input marks within 100")