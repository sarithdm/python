#Write a python function to search for a word in a sentance
def search_word(sentence, word):
    s = sentence.split(" ")
 
    for i in s:
        if (i == word):
            return True
    return False

s =input("Enter the sentase : ")
word =input("Enter the word : ")
 
if (search_word(s, word)):
    print("Yes")
else:
    print("No")