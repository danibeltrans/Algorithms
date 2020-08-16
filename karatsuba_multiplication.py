import math





def multiplication (a:int, b:int):
    
    if a < 10 or b < 10:
        return a * b

    else:

        n = max(len(str(a)),len(str(b)))

        """
        n = max(int(math.log10(a))+1 , int(math.log10(b))+1)
        """
        if n % 2 != 0:
            n = n + 1
    
        n2 = int(n/2)
        split =int(10**n2)
        xtest = int(a  + b)
        x1 = int(math.floor (a / split))
        x0 = int(math.floor (a % split))

        y1 = int(math.floor (b / split))
        y0 = int(math.floor (b % split))

        r = 10**n
        r2 = 10**n2

        z0 = multiplication(x1, y1)
        z1 = multiplication(x0, y0)
        z3 = multiplication(x0 + x1, y0 + y1) - z0 - z1 

        z0 = z0 * r
        z3 = z3 * r2
        total = z0 + z1 + z3  

    return total      

def case1 ():
    x = 1234
    y = 5678

    result = multiplication (x,y)
    print(format(result , 'f'))

    solution = 7006652

    if solution == result:
        print("Good! :)")
    else:
        print("pssss... something is wrong")

def case2 (): 
    x = 12345
    y = 56789

    result = multiplication (x,y)
    print(format(result , 'f'))

    solution = 701060205

    if solution == result:
        print("Good! :)")
    else:
        print("pssss... something is wrong")

def case3 ():
    x = 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    y = 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

    result = multiplication (x,y)
    print(format(result , 'f'))

    solution = 246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913577777777777775308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308642

    if solution == result:
        print("Good! :)")
    else:
        print("pssss... something is wrong")


case1()