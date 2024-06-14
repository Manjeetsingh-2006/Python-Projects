#Manjeet Singh

OverallHighest=0
OverallLowest=100
OverallTotal=0
Students=1

for x in range (1,9):
    SubjectHighest=0
    SubjectLowest=100
    SubjectTotal=0
    if(x==1):
        SubjectName="Maths"
    elif (x==2):
        SubjectName="Biology"
    elif (x==3):
        SubjectName="English"
    elif (x==4):
        SubjectName="ICT"
    elif (x==5):
        SubjectName="Computer Science"
    elif (x==6):
        SubjectName="Physics"
    elif (x==7):
        SubjectName="Business Studies"
    elif (x==8):
        SubjectName="Economics"
    print (SubjectName)
    for y in range(1, Students+1):
        print("Enter Students ",y,"'s mark for",SubjectName)
        Mark= int(input("Enter mark. "))
        if (Mark < OverallLowest):
           OverallLowest=Mark
        if (Mark < SubjectLowest):
            SubjectLowest=Mark
        if (Mark > OverallHighest):
            OverallHighest=Mark
        if (Mark > SubjectHighest):
            SubjectHighest=Mark
        OverallTotal=OverallTotal+Mark
        SubjectTotal=SubjectTotal+Mark
    SubjectAverage=SubjectTotal/Students
    print (SubjectName)
    print("Average is :",SubjectAverage)
    print("Highest mark:",SubjectHighest)
    print("Lowest mark is :",SubjectLowest)

OverallAverage=OverallTotal/16
print("Average is :",OverallAverage) 
print("Highest mark:",OverallHighest)
print("Lowest mark is :",OverallLowest)


print(OverallTotal)
print(SubjectTotal)




