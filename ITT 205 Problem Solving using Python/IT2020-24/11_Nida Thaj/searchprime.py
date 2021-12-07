num=int(input("Enter the length of the list:"))
mylist=[]
mylist1=[]
count=0
for i in range(num):
    element=int(input("Enter the element:"))
    mylist.append(element)
print("List elements are:",mylist)

for  number in mylist:
    count=0
    for i in range(2,(number//2)+1):
        if number%i==0:
            count+=1
            break
    if count==0:
        mylist1.append(number)   
print("Prime numbers found are:",mylist1)
