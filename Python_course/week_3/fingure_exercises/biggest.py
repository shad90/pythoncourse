def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    valueList = []
    for i in aDict.values():
        valueList.append(len(i))
    return list(aDict.keys())[valueList.index(max(valueList))]
