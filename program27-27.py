print("Which type of phone or tablet would you like")

DeviceFlag = False
while (DeviceFlag==False):
    DeviceCode=str(input("Input the Iteam code"))
    count =0
    while count<10 :
        if DeviceCode ==Itemcode[count]:
            print ("count")

        if count<6:
            Devicetype= ("phone")

        else:
            Devicetype= ("tablet")
    count=count +1
    DeviceFlag= True


print("Your  code does doesn't exist, please try again")
if (devicetype== ("phone")):

        print ("would you like a sim card")
        ans=str(input("yes/no?"))
        if (ans=="no"):
            print("simcard required")
