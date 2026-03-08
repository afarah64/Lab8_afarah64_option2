"""this module contains functions to calculate the area and circumference of a circle
Author: Abdalla Farah
Date: 03/06/2026
"""
def area(radius: float):
    """this funtion calculates the area of circle

    Args:
        radius (float): number from user input

    Returns:
        float: area of circle
    """
    area = 3.14 * radius ** 2
    return area
def circumference(radius: float):
    """this function calculates the circumference of a circle

    Args:
        radius (float): number from user input

    Returns:
        float: circumference of circle
    """
    circumference = 2 * 3.14 * radius
    return circumference


    
