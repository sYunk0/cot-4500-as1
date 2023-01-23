#Author: Samuel Yunker

def absoluteError(x,x_aprox):
    return abs(x-x_aprox)

def relativeError(x,x_aprox):
    if(x==0):
        return 0
    else:
        return absoluteError(x,x_aprox)/abs(x)

def question_1_through_4():
    #number = 0b01000000 01111110 10111001 00000000 00000000 00000000 00000000 00000000 #Zeros needed to be padded behind the number to make it fit in any meaningful way
    number = 491.5625 # As retrieved from the assignment 1 pdf and converted into a floating point number
    number_ChoppedAt3Digits = 491.0000
    number_RoundedTo3Digits = 492.0000

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
    while(abs(series(1,currentItteration)) > minError):
        #print(series(1,currentItteration))
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

        #print(currentItterations,p)
    

    return currentItterations

def NewtonRaphsonMethod(initialGuess,minError,f,f_prime):
    maxItterations = 200
    currentItterations = 0

    x_prev = initialGuess
    x_next = x_prev
    while(currentItterations < maxItterations):
        if(f_prime(x_prev) != 0):

            x_next = x_prev - f(x_prev)/f_prime(x_prev)

            if(abs(x_prev - x_next) < minError):
                return currentItterations
            
            x_prev = x_next
            currentItterations += 1
        else:
            return -1
    return -2

def question_6():
    def f(x):
        return x**3 + 4*(x**2) - 10
    def f_prime(x):
        return 3*(x**2) + 8*x

    minError = 1e-4
    a = -4
    b = 7

    itterationsToConverge_Bisection = BisectionRootFinder_itterationCounter(a,b,minError,f)
    itterationsToConverge_Newton = NewtonRaphsonMethod(a,minError,f,f_prime)

    print(itterationsToConverge_Bisection)
    print()
    print(itterationsToConverge_Newton)
    


if __name__ == "__main__":
    question_1_through_4()
    question_5()
    print()
    question_6()