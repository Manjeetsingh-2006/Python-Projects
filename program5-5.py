#Manjeet Singh
#Satmanjeetsingh@gmail.com
Count=1
GuessNo=80
High=0
Low=0
while(Count<5):
    Number=int(input("Enter a number"))
    if(Number>GuessNo): 
       High=Number
       print("Number is too high")       
    if(Number<GuessNo):
       Low=Number
       print("Number is too low")        
    if(Number==GuessNo):
        print("Congrulation!")
        break
    Count=Count+1
