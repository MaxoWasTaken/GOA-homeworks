# For loop

# 1

for i in range(21):
    print(i)

# 2

for i in range(1, 11):
    print(i)

# 3

# Even numbers
print("Even numbers:")
for i in range(0, 101, 2):
    print(i)

# Even numbers
print("Odd numbers:")
for i in range(1, 101, 2):
    print(i)

# 4

number = int(input("Enter a number: "))
sum_total = 0

for i in range(1, number + 1):
    sum_total += i

print(f"The sum of all numbers up to {number} is {sum_total}.")

# 5

for i in range(5, 51, 5):
    print(i)


# While Loop

# 1

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 2

i = 1
sum_total = 0

while i <= 10:
    sum_total += i
    i += 1

print(f"The sum of numbers from 1 to 10 is {sum_total}.")

# 3

correct_number = 7
guess = None

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == correct_number:
        print("Congratulations! You guessed the right number.")
    else:
        print("Try again!")

# 4

numbers = [1, 2, 3, 4, 5]
index = 0
doubled_numbers = []

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print(f"The doubled list is: {doubled_numbers}")

# 5

correct_password = "password123"
user_password = ""

while user_password != correct_password:
    user_password = input("Enter the password: ")
    if user_password == correct_password:
        print("Access granted.")
    else:
        print("Incorrect password. Try again.")
