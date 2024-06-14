#Exam Grade Checker
#Done by Manjeet Singh



Grade=input("Enter a letter grade:")
if Grade=='A+':
   print("90-100%")
   print("Excellent")
elif Grade=='A':
   print("80-89%")
   print("Good")
elif Grade=='B':
   print("70-79%")
   print("Average")
elif Grade=='C':
   print("60-69%")
   print("Bad")
elif Grade=='D':
   print("Totally Bad")
   print("50-59%")
else:
    print("Improvement is needed")
    print("You got below 49%")

PercentageMark=int(input("Enter a percentage mark: "))
if(PercentageMark<0)or(PercentageMark>100):
   print("Invalid mark")
elif(PercentageMark >49):
   print("Pass")
else:
   print("Failure")
   print("Improvment is needed")
   print("Try to past next time")
   print("Good Luck on your next exam")
 
   
