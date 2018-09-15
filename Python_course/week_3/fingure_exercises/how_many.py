def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    ans = 0
    for i in aDict.values():
        ans += len (i)
    return ans
