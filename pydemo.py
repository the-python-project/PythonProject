import Deck
import random
# print("hello world")
# a = 1+1
# print ("the value of a is " + str(a))
# print (1+1)
# for x in range(1, 10):
#     print(x)
#     if x%2 == 0:
#         print("x minus 1 is: " +str(x-1))
# print("loop is done")
# #this is a comment
# """ this is a docstring comment"""
# b="hi there :)"
# aAndBBool = a is b
# print("is a and b the same type? " + str(aAndBBool))
# print(b[4]) #should be h
# input = input()
# print("this is the input: " +input)
# print("HI May - from Buffy")
# print("HI there")
# print("What is up!!!!")

# this is the main functions:
nineRandomIndexes = []
matchedRandomIndexes =[]
def main():
    deck = Deck.Deck()
    allKeys = list(deck.deckAndClues.keys())
    print(allKeys)

    for i in range(9):
        randomNum = random.randrange(0, 51, 1)
        nineRandomIndexes.append(randomNum)

    print(nineRandomIndexes)

    # 1. make a global variable list to store the card names
    # 2. make a for loop to loop through all the random numbers in nineRandomIndexes
    # 3. for each random number, get the word in allKeys that corresponds to the number/index (use the [x] method), and add
    #this word to the list you made in step 1

    for x in nineRandomIndexes:
        generatedwords=allKeys[x]
        print(x)
        print(allKeys[x])
        matchedRandomIndexes.append(generatedwords)

    print(matchedRandomIndexes)



if __name__ == "__main__":
    main()
