import math

def isPanDig(x):
    return len(str(x)) == 9 and set(str(x)) == set("123456789")
    
found = False
i = 0
j = 1
nth = 0
phi = 1.6180339887498948482
rt5 = math.sqrt(5)

while not found:
    nth+=1
    
    # normal fib stuff
    k = i
    i = j+i
    j = k
    
    # mod bc we don't care about more then last 9
    i = i % (10 ** 9)
    j = j % (10 ** 9)
    
    if isPanDig(i):
        
        # first 10 tom foolery
        x1 = nth * math.log(phi, 10) - math.log(rt5, 10)
        x2 = math.floor(x1)
        first9 = math.floor((10 ** 8) * (10 ** (x1-x2)))
        
        if(isPanDig(first9)):
            found = True
            print(i)
            print(nth)