import array
ConstNoStudent=int(5)
StudentMarkTest1=array.array("i",range(ConstNoStudent+1))
StudentMarkTest2=array.array("i",range(ConstNoStudent+1))
StudentName=[]

for Counter in range(1,ConstNoStudent+1):
    StudentName.append(input("Enter a student name :"))

for Counter in range(0,ConstNoStudent):
    print(StudentName[Counter])
    
