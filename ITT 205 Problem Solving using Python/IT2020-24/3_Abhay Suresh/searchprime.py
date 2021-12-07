def search(mylist):
 flag=1
 for item in mylist:
  for i in range(2,item):
	if(item%i)==0:
	  flag=0
	  break
  if flag==0:
  	print(item,"is not a prime number")
  else:
	print(item,"is a prime number")
n=int(input("Enter the number of elements in the list"))
mylist=[]
for item in range(0,n):
  num=int(input("Enter the number"))
  mylist.append(num)
search(mylist)
