"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""
import math

def area(r):
    return math.pi * r**2


def circumference(r):
    return math.pi * 2 * r


radius = input("Circle radius: ")

circle_area = area(int(radius))
circumference_lenght = circumference(int(radius))

print('Area: ' + str(circle_area))
print('Circumference: ' + str(circumference_lenght))
