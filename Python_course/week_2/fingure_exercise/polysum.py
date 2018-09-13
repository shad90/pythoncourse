#Importing all math functions from Python's math library
from math import *
# Defining polysum fucntion which calculates the sum of 
# area and square of the perimeter of the regular polygon
def polysum (n,s):
    '''
    n: number of sides of a Polygon
    s: length of each side of a Polygon
    n and s can be int or float
    polysum: sum the area and square of the perimeter of the regular polygon
    '''
    #Calculating perimeter of polygon
    polyPerimeter = n*s
    #Caculating area of polygon
    polyArea = (0.25*n*s**2)/(tan(pi/n))
    #Return the polysum. Rounding it to 4 decimal points.
    return round(polyPerimeter**2 + polyArea,4)
