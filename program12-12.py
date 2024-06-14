#Manjeet Singh


Yourplace=input("Where will you like to travel from ")
Yourdestination=input("Were are you travelling to")
Youremail=input("Your email ?")
Youraddress=input("Your address?")



Discount=0
NumberOfTickets=int(input("How many tickets would you lke to buy?"))

if(NumberOfTickets<10):
    Cost=NumberOfTickets*20
    
                    
if (NumberOfTickets<20):
    Cost= (NumberOfTickets*20*0.9)
    
                
if(NumberOfTickets>20): 
    Cost= (NumberOfTickets*20*0.8)
                    
print ("Your ticket Cost ",Cost)



Pleasepaymoney=print("We only accept paypal")
Paymoneytothisemail=print(" please pay to this email satmanjeetsingh@gmail.com")

print("You have paid money!")

print("Thanks from buying the tickets from us we will deliver your ticket within an hour")
print("Have the safe journey and we will look forward to work with you again")


