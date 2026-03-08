"""this module contains functions to calculate the area and perimeter of a rectangle.
   Author: Abdalla Farah
   Date: 03/06/2026
"""
def area(width: float, height: float):
    """this function calculates the area of a rectangle

    Args:
        width (float): number from user input
        height (float): number from user input

    Returns:
        float: area of rectangle
    """    
    area = width * height
    return area

def perimeter(width: float, height: float):
    """this function calculates the perimeter of a rectangle

    Args:
        width (float): number from user input
        height (float): number from user input

    Returns:
        float: perimeter of rectangle
    """
    perimeter = 2 * (width + height)
    return perimeter

