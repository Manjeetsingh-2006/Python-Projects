#Converting denary number to Binary Number in 8 bits register.

x=int(input("Enter a number: "))

D=128
while(D>0.5):
    x=x-D

    if(x<0):
        print(0)
        x=x+D
    else:
        print(1)
    D=D/2
