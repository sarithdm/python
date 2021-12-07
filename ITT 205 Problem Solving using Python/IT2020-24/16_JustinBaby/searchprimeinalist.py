#Write a python program to search for a prime number in a list
def search(mylist):
  flag=1
  for item in mylist:
    for i in range(2,item):
      if (item%i)==0:
        flag=0
        break
    if flag==0:
      print(item,"is not prime number")
    else:
      print(item,"is prime number")

n=int(input("Enter the no.of elements in the list"))
mylist=[]
for item in range(0,n):
    ele=int(input("Enter the number : "))
    mylist.append(ele)
search(mylist)