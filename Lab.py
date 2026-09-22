import random

currentDice = random.randint(1,6)

sidesOfADie = [1,2,3,4,5,6]

print("There are the sides to a die: ", sidesOfADie)
print("The current die number is: ", currentDice)

anotherWayToChooseInAList = random.choice(sidesOfADie)

print("This came from another way to choose within a list: ", anotherWayToChooseInAList)

import numpy

happyFace = [1,2,3,4]

smily = numpy.array(happyFace)

# Change
happyChar = ['1','b','c','d']
happyChar1 = ["Words", "to", "speak"]
happyBools = [True, False, True]
happyBools2 = [[1,2,3], [True, False, True], ["words"]]

print("Hello World")
print(happyBools2)

print(smily)
