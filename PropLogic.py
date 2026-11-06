
def propLogic(input_P, input_Q, input_R):

    input_PandQ = input_P and input_Q

    results = input_PandQ == input_R

    print(input_R, input_Q, input_R, results)

print("(P AND Q) <-> R   Bi-Conditional")

propLogic(True, True, True)
propLogic(True, False, True)
propLogic(True, True, False)
propLogic(True, False, False)
propLogic(False, True, True)
propLogic(False, False, True)
propLogic(False, True, False)
propLogic(False, False, False)

print("P --> (Q OR V)")


def extraPropLogic(P_Input, Q_Input, R_Input):

    Qinput_or_R_Input = Q_Input or R_Input

    extraResults = (not P_Input) or Qinput_or_R_Input

    print( P_Input, Q_Input, R_Input, extraResults)


extraPropLogic(True, True, True)
extraPropLogic(True, False, True)
extraPropLogic(True, True, False)
extraPropLogic(True, False, False)
extraPropLogic(False, True, True)
extraPropLogic(False, False, True)
extraPropLogic(False, True, False)
extraPropLogic(False, False, False)