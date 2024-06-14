#Manjeet Singh

Country=str(input("Enter the name of the country:"))
H=int(input("Enter hours:"))
M=int(input("Enter minutes:"))

if(Country == "Mexico"):
    H=H-7
    M=M
elif (Country == "India"):
    H=H+4
    M=M+30
elif (Country == "New Zeland"):
    H=H+11
    M=M
print ("The hour is : ",(int((H*60+M)/60)))
print ("The minutes is ", (H*60+M)%60)

