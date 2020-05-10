#The Collatz Sequence
#The function collatz() takes an integer.
#If the integer is even, it returns the integer divided by 2.
#If the integer is odd, it returns the integer multiplied by 3 plus 1.
#This sequence is repeated until the function ultimately returns the integer 1.

#Define collatz function
def collatz(n):
    while n > 1:
        if n % 2 == 0: #If odd
            n = n/2
            print(str(n))
        else: # If even
            n = n * 3 + 1
            print(str(n))
    return 0

#Get user input
number = input("Input number:\n")

#Call collatz function on inputted number
try:
    collatz(int(number))
except ValueError:
    print("Error. You must enter an integer.")