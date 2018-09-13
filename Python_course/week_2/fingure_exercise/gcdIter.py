def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (a <= b):
        for i in range(a,0,-1):
            if (a%i == 0 and b%i == 0):
                return i
    else:
        for i in range(b,0,-1):
            if (a%i == 0 and b%i == 0):
                return i
            
