def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mind = len(aStr)//2
    if len(aStr)<=1:
        return char == aStr
    elif(char == aStr[mind]):
        return True
    elif(char > aStr[mind]):
        return isIn(char, aStr[mind:])
    else:
        return isIn(char,aStr[:mind])
        
