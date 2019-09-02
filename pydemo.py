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
def main():
    deck = Deck.Deck()
    allKeys = list(deck.deckAndClues.keys())
    print(allKeys)

    for i in range(9):
        randomNum = random.randrange(0, 51, 1)
        nineRandomIndexes.append(randomNum)

    print(nineRandomIndexes)




if __name__ == "__main__":
    main()
