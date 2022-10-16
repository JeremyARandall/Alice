#!/usr/bin/env python3
import sys


#create a struct to hold the number of AiW words to build a word, and store those words
class AiW:

    def __init__(self, num, words):
        self.attr = {
                        "num": num,
                        "words": words
                    }
        

    def __getitem__(self, var):
        return self.attr[var]

    def __setitem__(self, var, x):
        self.attr[var] = x

    def getnum(self):
        return self.__getitem__("num")

    def getwords(self):
        return self.__getitem__("words")
    
    def setnum(self, newnum):
        self.__setitem__("num", newnum)

    def setwords(self, newwords):
        self.__setitem__("words", newwords)

#create a dict and read lines in, assign arbitrary value as it is only needed to check if the key exists
aDict = {}
try:
    with open("aliceInWonderlandDictionary.txt") as infile:
        for line in infile:
            word = line.strip()
            aDict[word] = 1

except IOError:
    print("Error opening dictionary")
def findWords(word):
    #create an empty list and fill it with a AiW structure for each letter in the test string
    AiWlist = []
    for i in range(0, len(word)):
        AiWlist.append(AiW(-1, ""))
    #for check starting from the beginning to the end, check if each substring A is made of words in the dictionary.
    for i in range(0, len(word)):
         #moving the start of the substring B from the start to the end of the substring A to the end of substring A, check if the substring B is a word in the dictionary
        #moving the start of substring B from the beginning to the end of A ensures that the longest words possible are used instead of shorter possible words
        #eg william will be returned instead of will i am
        for j in range(0,i+1):
            substring = word[j:i+1]
            if j == 0 and substring in aDict: #if the entire substring is in the dictionary, set the number of words to form the substring to 1 and save the substring
                AiWlist[i].setnum(1)
                AiWlist[i].setwords(substring)
                break
            #if the latter part of the substring is in the dictionary, and the former part is already found to be comprised of such words
            #then we will set the count of the whole substring to 1 above the former's count, and add the save all parts of the substring already found
            elif AiWlist[j-1].getnum() != -1 and substring in aDict: 
                AiWlist[i].setnum(1+AiWlist[j-1].getnum())
                temp = AiWlist[j-1].getwords() + ' ' + substring
                AiWlist[i].setwords(temp)
                break 


    if AiWlist[len(word)-1].getnum() == -1:
        print('%s can not be split into AiW words.' % (word))
    elif AiWlist[len(word)-1].getnum() == 1:
        print('%s can be split into 1 AiW word: %s' % (word, AiWlist[len(word)-1].getwords()))
    else:
        print('%s can be split into %d AiW words: %s' % (word, AiWlist[len(word)-1].getnum(), AiWlist[len(word)-1].getwords()))

try:
    with open("input.txt") as infile:
        for line in infile:
            findWords(line.strip())
except IOError:
    print('Error opening input.txt')

    
        
