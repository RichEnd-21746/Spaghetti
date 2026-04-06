with open("Random.txt") as random_file:
    each_line = random_file.readline()

    print("Reading from file Random.txt\n")

    """ This loop prints out all the numbers from Random.txt"""
    for each_line in random_file:
        print(each_line)

    """Reset pointer"""

    random_file.seek(0)

    """ The buffer variable is a cleaner version of random.txt that
    gets rid of trailing whitespaces and \n"""

    buffer = [int(line.strip()) for line in random_file if line.strip()]
    
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