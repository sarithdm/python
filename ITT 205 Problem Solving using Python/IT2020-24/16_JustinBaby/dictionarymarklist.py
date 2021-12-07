# Write a Python program to print the mark list of students using a dictionary (Name, Roll Number, Marks of each subject, Total Marks). Total marks should be calculated from the marks of each subject
num=int(input("Enter the number of students:"))
my_dictionary={}
for i in range(num):
    rollno=int(input("Enter the RollNo:"))
    name=input("Enter the Name:")
    mark1=int(input("Enter the marks of first subject:"))
    mark2=int(input("Enter the marks of second subject:"))
    mark3=int(input("Enter the marks of third subject:"))
    totalmarks=mark1+mark2+mark3
    list=[name,totalmarks]
    my_dictionary[rollno]=[name,totalmarks]
    my_dictionary[rollno]=list
print(my_dictionary)