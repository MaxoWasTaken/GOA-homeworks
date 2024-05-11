number = 0
total_sum = 0

while number <= 20:
    if number % 2 == 0:
        total_sum += number
    
    number += 1

print("The sum of even numbers from 0 to 20 is:", total_sum)