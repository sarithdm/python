#Write a Python program to print the mark list of students using a dictionary (Name, Roll Number, Marks of each subject, Total Marks). Total marks should be calculated from the marks of each subject
num=int(input("Enter the numbers of students"))
mydictionary=0
for i in range(num):
	rollno=int(input("Enter the roll no"))
	name=input("Enter the name")
	mark1=int(input("Enter the mark of first subject"))
	mark2=int(input("Enter the mark of second subject"))
	mark3=int(input("Enter the mark of third subject"))
	totalmarks=mark1+mark2+mark3
	list=[name,totalmarks]
	mydictionary[rollno]=[name,totalmarks]
	mydictionary[rollno]=list
print(mydictionary)
