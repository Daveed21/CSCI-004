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