import random

currentDice = random.randint(1,6)

sidesOfADie = [1,2,3,4,5,6]

print("There are the sides to a die: ", sidesOfADie)
print("The current die number is: ", currentDice)

anotherWayToChooseInAList = random.choice(sidesOfADie)

print("This came from another way to choose within a list: ", anotherWayToChooseInAList)
