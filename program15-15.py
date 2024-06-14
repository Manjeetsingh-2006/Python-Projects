#Manjeet Singh

ChocolateTotal=0
ToffeesTotal=0
JelliesTotal=0
OtherTotal=0
f = []
for i in range(5):
    num=int(input("Enter a four-digit code :"))
    f.append(num)
    print(f[i])
    if (f[i]>999)and(f[i]<2000):
        ChocolateTotal=ChocolateTotal + 1
    if (f[i]>2000)and(f[i]<3000):
        ToffeesTotal=ToffeesTotal+1
    if (f[i]>3000)and(f[i]<4000):
        JelliesTotal=JelliesTotal+1
    if (f[i]>4000)and(f[i]<10000):
        OtherTotal=OtherTotal+1
next
print("Chocolate Total is :",ChocolateTotal)
print("Toffees Total is :",ToffeesTotal)
print("Jellies Total is :",JelliesTotal)
print("Other Total is :",OtherTotal)
