# 1st

def print_numbers():
    # Loop through numbers from 1 to 20
    for i in range(1, 21):
        # Print each number
        print(i)

# Call the function to execute it
print_numbers()


# 2nd

def print_sum():
    # Calculate the sum of numbers from 1 to 20
    total = sum(range(1, 21))
    # Print the total sum
    print(total)

# Call the function to execute it
print_sum()


# 1rd (bonus)

def interpolate_numbers(start, end):
    # Loop through numbers from start to end, inclusive
    for i in range(start, end + 1):
        # Print each number
        print(i)

# Call the function with example values to execute it
interpolate_numbers(5, 15)


# 2th (bonus)

def sum_to_number(end):
    # Calculate the sum of numbers from 0 to end
    total = sum(range(end + 1))
    # Return the total sum
    return total

# Call the function and store the result
result = sum_to_number(10)
# Print the returned result
print(result)







# 1

def sum_of_two_numbers():
    # enter the first num
    num1 = float(input("Enter the first number: "))
    
    # enter the second num
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum of it
    total = num1 + num2
    
    # Print the sum
    print(f"The sum of {num1} and {num2} is {total}")

# execute it with funtction
sum_of_two_numbers()









# 2

def product_of_range():
    # enter the first num
    start = int(input("Enter the first number: "))
    
    # enter the second num
    end = int(input("Enter the second number: "))
    
    # Ensure the start is less than or equal to end
    if start > end:
        start, end = end, start
    
    # Initialize the product to 1 
    product = 1
    
    # Loop through the range from start to end
    for num in range(start, end + 1):
        product *= num  # Multiply each number to the product
    
    # Print the final product
    print(f"The product of all numbers from {start} to {end} is {product}")

# Execute it with function
product_of_range()








# 1 & 2

def calculate_sum(numbers):
    # Initialize the total sum to 0
    total = 0
    
    # Loop through each number
    for number in numbers:
        # Add each number to sum
        total += number
    
    # Return the total sum
    return total

# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = calculate_sum(numbers_list)
# Print the result
print(f"The sum of the list is: {result}")




# 3

def sum_and_multiply_lists(list1, list2):
    # Initialize the sums for both to 0
    sum1 = 0
    sum2 = 0
    
    # Calculate the sum of the first
    for number in list1:
        sum1 += number
    
    # Calculate the sum of the second
    for number in list2:
        sum2 += number
    
    # Multiply the sums of both
    result = sum1 * sum2
    
    # Return the result
    return result

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = sum_and_multiply_lists(list1, list2)
# Print the result
print(f"The result of multiplying the sums of the lists is: {result}")
