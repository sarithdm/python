def searchword(word):
    if word in sentence:
        print (word,"is present in the sentence")
    else:
        print(word," is  not present in the sentence")
        
sentence=input('Enter the sentence:')
word=input('Enter the word to be searched:')
searchword(word)
