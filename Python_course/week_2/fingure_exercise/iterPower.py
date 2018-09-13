#Calculate power by iterative method
def iterPower (base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = 1
    for i in range(exp):
        ans *= base
    return ans
