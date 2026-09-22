#Week Assignment pt 1
#Thinking of doing the blinker of a car through python. Could be easy ish and set a for loop to go for x amount of times printed(Basically showing the flashes)

#Changeable number of flashes for later
numberOfFlashes = 10

#Getting direction in which user moved wheel
userInput = input()

#Only allows input when userInput is exactly one of the following
if userInput == "right" or userInput == "Right":
    # Was messing around with while and for loops but found a better way to increase the number of times a word is printed by * multiplying the print statement
    #       while i == numberOfFlashes:
    print("Right Flash! " * numberOfFlashes)
#Getting other directional input for the "flashes"    
elif userInput == "Left" or userInput == "left":
    print("Left Flash! " * numberOfFlashes )       

#When no correct input is given user must try again
else:
    print("Please input a valid direction. (Right or Left)")

    
#My check work to make sure input was given outputted correctly
# print(userInput)




#Dont forget assignemt




#Week assignment pt 2 
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

#Part 1   ax^exp             OOpsie I made the parenthesis in the wrong spot hehe pemdas
partOne = (aAssignment * xAssignment) ** expAssignment

#Part 2   bx

partTwo = bAssignment * xAssignment

#Part 3   c... kinda easy I guess lol
partThree = cAssignment #lol

#Final add in and print. Also adding a final look before doing the math 
print("This is your equation: (", aAssignment, "*", xAssignment, ") ^", expAssignment, "+ (", bAssignment, "*", xAssignment, ") + ", cAssignment)

#Final check doing math on phone then inputting final result

print("This is the result: ", partOne + partTwo + partThree)
