#Manjeet Singh
TotalHeight=0
TotalWeight=0
NoStudents=int(1000)
StudentName= []
for counter in range(1, NoStudents +1):
    StudentName.append(input("Enter Student Name: "))
    a=True
    while a:
        StudentHeight=float(input("Enter Student Height in Metres: "))
        if (StudentHeight >0.5) and (StudentHeight <1.5):
            TotalHeight=StudentHeight+TotalHeight
            a=false
    a=True
    while a:
        StudentWeight=float(input("Enter Student TotalWeightht in Kilograms: "))
        if (StudentWeight >0) and (StudentWeight < 90):
            TotalWeight=StudentHeight+TotalWeight
            a=false
AverageHeight= TotalHeight/NoStudents
AverageWeight= TotalWeight/NoStudents
print("Average student Height is",AverageHeight)
print("Average student Weight is",AverageWeight)
