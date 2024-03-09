'''
Program: Write an Advanced Calculator 
Date: 5/26/2020

Maintenance History:
    5/26/2020 - Create program
'''
'''
Import math library module and choose 3 built-in functions.
Ask user to choose which operation to perform and give appropriate output
'''
#imports math library 
import math
#Create function to add two numbers
def add (num1, num2):
    return num1 + num2

#Create function to subtract two numbers
def subtract (num1, num2):
    return num1 - num2
'''
Program prompts user to add, subtract or quit
Action executed depending on user prompt
'''
#Create code to ask user input and repeat until prompted to end progrma
print("Welcome to the Calculator Program! Please select an option from the menu below.")
print("\nOption Menu:")
print("Type 'add' for addition")
print("Type 'subtract' for subtraction")
print("Type 'log' for log10")
print("Type 'sine' for finding sine")
print("Type 'sqrt' for square root")
print("Type 'quit' to quit program\n")
option = input("Which operation do you want to perform? ")
while option != 'quit':
    try:
        #Execture action based on option input by user
        if option == 'quit':
            break
        elif option == 'add':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(num1, " + ",num2, "= %.3f" % add(num1, num2))
            print() #print blank line
        elif option == 'subtract':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(num1, " - ", num2, "= ", subtract(num1, num2))
            print() #print blank line
        elif option == 'log':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            #calculate input for logarithm of base 10 and format output
            print("Log10(",num1, ") = %.3f" % math.log10(num1))
            print("Log10(",num2, ") = %.3f" % math.log10(num2))
            print() #print blank line
        elif option == 'sine':
            num1 = float(input("Please enter the first number (in degrees): "))
            num2 = float(input("Please enter the second number (in degrees): "))
            #calculate sine of input, given degrees and format output
            print("Sin(",num1, ") = %.3f" % math.sin(num1))
            print("Sin(",num2, ") = %.3f" % math.sin(num2))
            print() #print blank line
        elif option == 'sqrt':
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            #calculate square root of input and format output 
            print("Sqrt(",num1, ") = %.3f" % math.sqrt(num1))
            print("Sqrt(",num2, ") = %.3f" % math.sqrt(num2))
            print() #print blank line 
        else:
            #if option doesn't match, output error message
            print("You entered an invalid option. Please try again.\n")
    except ValueError:
        #if number input doesn't match, output error message 
        print("You did not enter a number. Please try again.\n")
    option = input("Do you want to run the program again?\nPlease select from the option menu. ")
    
print("\nThank you for using the calculator.")

    
    
    
                 
    
