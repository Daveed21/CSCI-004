# ax^exp + bx + c
#Starting equation I would like to work on

#Need to see about importing any math libraries in order to incorporate the ^2 better. If not we can do the longer way
import math

#Create assignments for each part of the equation and get the inputs
#Also looking at documentation in a quick way to get only an integer input and wondered if I can just put int and the surround the input... Which works nice lol
print("What is the 'a' assignment")
aAssignment = int(input('-->'))

print("What is the 'b' assignment")
bAssignment = int(input('-->'))

print("What is the 'c' assignment")
cAssignment = int(input('-->'))

print("What is the exponent input")
expAssignment = int(input('-->'))

print("What is the 'x' input")
xAssignment = int(input('-->'))


#mTester = aAssignment ** bAssignment   (Leaving this here for reference that the first one is what gets powered)

#Test power multiplier? yeah lets print here
#Found out by luuck in math.exp that putting two ** symbols gets power.. which makes sense since its times itself neat
#print(mTester)

#Now to create our variable in math notation. May be easier to break down each section since it is separated by a '+' symbol

#Part 1   ax^exp
partOne = aAssignment * (xAssignment ** expAssignment)

#Part 2   bx

partTwo = bAssignment * xAssignment

#Part 3   c... kinda easy I guess lol
partThree = cAssignment #lol

#Final add in and print. Also adding a final look before doing the math 

print("This is your equation: ", partOne, partTwo, partThree)

#Final check doing math on phone then inputting final result
