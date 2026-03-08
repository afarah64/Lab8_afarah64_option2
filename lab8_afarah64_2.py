"""Geometry Calculator
   This is the main function that runs the geometry calculator program. 
        It displays a menu to the user and prompts them to enter their choice. 
        Based on the user's choice, it calls the appropriate functions from the regtangle and circle modules 
        to calculate the area and perimeter of a rectangle or the area and circumference of a circle. 
        The program continues to run until the user chooses to exit.
 
   @Author: Abdalla Farah
    Date: 03/06/2026
"""
#importing the regtangle and circle modules to use their functions in the main program
#alias is used to shorten the module names for easier reference in the code.
#alias is good to avoid naming conflicts and make the code more readable.
#As the module has area functions for both circle and rectangle, 
# using alias helps to differentiate between them and avoid confusion when calling the functions in the main program.
import regtangle as r
import circle as c


if __name__ == "__main__":

#loop to display the menu and prompt the user for input until they choose to exit
    done = True
    while done == True: 
        print("\nGeometry Calculator")
        print("---------------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit\n")
        #try-except block to handle invalid input and ensure the program continues to run until the user chooses to exit
        try:
            user_input = input("Enter your choice (1-5): ")
            choice = float (user_input.strip())

            if choice == 5:
                    print("\nGoodbye!")
                    done= False
            else:
            #check if the user's choice is not between 1 and 5, if so, it prints an error message and prompts the user to try again.
                if choice not in range(1,5): 
                    print("Invalid choice. Please try again.")
            #if the user's choice is valid, it checks which option they selected and prompts them for the necessary input to perform the calculation 
            # using the appropriate functions from the regtangle and circle modules.        
                else:
                    if choice == 1:
                        radius = float(input("Enter the radius of the circle: "))
                        print(f"The area of the circle is: {c.area(radius)}")
                    elif choice == 2:
                        radius = float(input("Enter the radius of the circle: "))
                        print(f"The circumference of the circle is: {c.circumference(radius)}")
                    elif choice == 3:
                        
                        width = float(input("Enter the width of the rectangle: "))
                        height = float(input("Enter the height of the rectangle: "))
                        print(f"The area of the rectangle is: {r.area(height, width)}")
                    elif choice == 4:
                        
                        width = float(input("Enter the width of the rectangle: "))
                        height = float(input("Enter the height of the rectangle: "))
                        print(f"The perimeter of the rectangle is: {r.perimeter(height, width)}")
                #it gives pause which allows the user to see results before making another calculation.        
                input("\nPress Enter to continue...")
                
        except ValueError:
            print("Invalid input. Please put a valid number.")

    
            
    


