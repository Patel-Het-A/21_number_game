import random

print("Hello !\nLet's play guessing game.")
l=int(input("enter lower limit:"))
h=int(input("enter upper limit:"))

x=random.randint(l,h)
c=int(input("now guess the number:"))
f=0
while True:
    f=f+1
    if(c>x):
        print(f"attemt:{f} too high guess.")
        c=int(input("try again:"))
    elif(c<x):
        print(f"attemt:{f} too low guess.")
        c=int(input("try again:"))
    else:
        print(f"nice you guess correct number:{c}")
        break


