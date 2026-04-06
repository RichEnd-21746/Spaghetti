# Homework 5: Numeric Processing
# Program By: Esteban
# File Name: H5_Num_Process.py
# Function: This program reads and writes to files
try:
    with open("Random.txt") as random_file:
        print("Reading from file Random.txt\n")
    
        """ The buffer variable is a cleaner version of random.txt that
        gets rid of trailing whitespaces and \n"""

        buffer = [int(line.strip()) for line in random_file if line.strip()]
    
        """ This loop prints out all the numbers from buffer"""

        for each_line in buffer:
            print(each_line)

except FileNotFoundError:
    print("Error: The file 'Random.txt' was not found")
    buffer = []
except ValueError:
    print("Error: The file 'Random.txt' contains characters that aren't numbers")
    buffer = []

    
"""All the simple operations are nested under an if-statement in the 
case that buffer does not exist"""
if buffer:
    number_of_numbers = len(buffer)
    sum_of_all_numbers = sum(buffer)
    average_of_all_numbers = sum(buffer) / len(buffer)
    print(f"There are {number_of_numbers} numbers within the file")
    print(f"The sum of all numbers in the file is {sum_of_all_numbers}")
    print(f"The average of all numbers in the file is {average_of_all_numbers}")

    results = f"Number of numbers: {number_of_numbers}\nSum of all numbers {sum_of_all_numbers}\nAverage of all numbers {average_of_all_numbers}\n"

    if results:
        with open("Results.txt", "a") as results_file:
            results_file.write(results)