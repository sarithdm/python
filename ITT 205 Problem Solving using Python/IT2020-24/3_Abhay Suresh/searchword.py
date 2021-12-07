#Write a Python function to search for a word in a sentence
def searchword(sentence,word):
  s=sentence.split(" ")
  for i in s:
	if(i==word):
	   return true
	return false
s=input("Enter the sentence")
word=input("Enter the word")
if(searchword(sentence,word)):
	print("Yes")
else:
	print("No")
