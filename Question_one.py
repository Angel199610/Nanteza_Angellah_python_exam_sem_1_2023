# Import the 'pi' constant from the 'math' module to calculate the area of a circle
from math import pi

# Prompt the user to input the radius of the circle
r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2

# Display the result, including the radius and calculated area
print("The area of the circle with radius " + str(r) + " is: " + str(area))


#A recrusive function to calculate the sum of natural numbers
# Returns sum of first n natural numbers 
def recurSum(n): 
    if n <= 1: 
        return n 
    return n + recurSum(n - 1) 
  
n = 4
print(recurSum(n))


#Removing the element in the index 
numbers = [1,3,5,7,9]
numbers.pop(2)
print(numbers)

numbers = [1,3,5,7,9] #Inserting value 10
numbers.insert(2, 10) 
print(numbers)


# Python program to print Even Numbers in a List
 

list1 = [2,70,15,20,4,6,8,10,] # list of numbers 

for num in list1: # iterating each number in list
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")


#A dictionary to update the value of "age to 25"
my_dict = { "name": "Alice", "age": 20, "Grade": "A" }

my_dict["age"] = 25 # Update the value associated with the "age" key

print(my_dict)# The dictionary now contains the updated value


#Dictionary comprehension to create a new dictionary
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}

new_dict = {k: v for (k, v) in original_dict.items() if v % 5 > 0}
print(new_dict)


