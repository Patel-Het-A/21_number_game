import random

s=input("Hey ! what is your name:")
print(f"Hii {s}! let's play 21 number game.")
x=input("If you want to take first turn then press 'f',"
" and if you want to take second turn then press 's':")
numbers=[0]
current=1
m=1
if(x == 'f'):
    m=0
while (numbers[-1]<21):
    if(not m):
        print("write now :" ,numbers)
        n=int(input("how many number you want to enter:"))
        while n>0:
            numbers.append(current)
            current=current+1
            n=n-1
        m=1
        if(numbers[-1]>=21):
            print("write now :" ,numbers)
            print("You lost!\nTry again.")
    else:
        n=min(3,4-(numbers[-1]%4))
        while n>0:
            numbers.append(current)
            current=current+1
            n=n-1
            m=0
        if(numbers[-1]>=21):
            print("write now :" ,numbers)
            print("Congratulation You won the game!")
