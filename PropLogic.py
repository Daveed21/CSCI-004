
print("Hello")

Input_P = bool(input("Please enter a boolean value for P, T/F:"))
Input_Q = bool(input("Please enter a boolean value for Q, T/F:"))
Input_R = bool(input("Please enter a boolean value for R, T/F:"))

if(Input_P and Input_Q):

   # if(Input_R):
        print("True Statement!")

elif Input_P == Input_Q:
    print("maybe")

else:
    print("False statement!")



