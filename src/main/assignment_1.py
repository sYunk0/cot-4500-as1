import numpy as np

def absoluteError(x,x_aprox):
    return abs(x-x_aprox)

def relativeError(x,x_aprox):
    if(x==0):
        return 0
    else:
        return absoluteError(x,x_aprox)/abs(x)

def question_1_through_4():
    #number = 0b001110000000001111111111 #Zeros need to be padded behind the number to make it fit in any meaningful way
    number = 3.14703e-5 # As retrieved from the assignment 1 pdf and converted into a floating point number and limited to 5 decimal places
    number_ChoppedAt3Digits = 3.14e-5
    number_RoundedTo3Digits = 3.15e-5

    relativeErrorOfRoundedNumber = relativeError(number,number_RoundedTo3Digits)
    absoluteErrorOfRoundedNumber = absoluteError(number,number_RoundedTo3Digits)

    print(number)
    print()
    print(number_ChoppedAt3Digits)
    print()
    print(number_RoundedTo3Digits)
    print()
    print(absoluteErrorOfRoundedNumber)
    print(relativeErrorOfRoundedNumber)

def question_5():
    def series(x,k:int):
        return ((-1)**k) * ((x**k)/(k**3))
    
    minError = 1e-4
    currentItteration =  1
    while(series(1,currentItteration) < minError):
        currentItteration += 1

    print()
    print(currentItteration)

def BisectionRootFinder_itterationCounter(a,b,minError,f:callable):
    
    left = min(a,b)
    right = max(a,b)

    maxItterations = 200
    currentItterations = 0

    while(abs(left-right) > minError and currentItterations < maxItterations):
        currentItterations += 1
        p = (left+right)/2

        l1 = f(left)
        l2 = f(right)
        lmid = f(p)
        if(l1 < 0 and lmid > 0):
            right = p
        else:
            left = p
    

    return currentItterations

def NewtonRaphsonMethod(initialGuess,minError,f,f_prime):
    maxItterations = 200
    currentItterations = 0

    x_prev = initialGuess

    currentEstimate = f(x_prev)
    while(abs(currentEstimate) > minError and currentItterations < maxItterations):
        currentItterations += 1


        tangent = f_prime()

        if(tangent != 0):
            x_new = x_prev - currentEstimate/tangent

            

def question_6():
    def f(x):
        return x**3 + 4*(x**2) - 10

    minError = 1e-4

    itterationsToConverge_Bisection = BisectionRootFinder_itterationCounter(4,7,minError,f)
    


if __name__ == "__main__":
    question_1_through_4()
    question_5()