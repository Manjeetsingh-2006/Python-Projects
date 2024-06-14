Name=input(str("Enter your name"))
print(Name)           
num=int(input("Guess a number:between 0 to 100"))
GuessNo=68
count=1
while(count<10):
    if (num >GuessNo):
       print("too high!")
       num=int(input("Guess a number:between 0 to 100"))
    if(num<GuessNo):
       print("too low:")
    if(num==GuessNo):
       print("Congratuaions")
    count=count+1      
    
