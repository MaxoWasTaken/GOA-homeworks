num1 = int(input("Type number 1: "))

num2 = int(input("Type number 2: "))

num3 = int(input("Type number 3: "))

question = input("Do you want to use +,-, / or * in equation?: ")

if question == ("+"):
    print(num1 + num2 + num3)

elif question == ("-"):
    print(num1 - num2 - num3)

elif question == ("/"):
    print(num1 / num2 / num3)

elif question == ("*"):
    print(num1 * num2 * num3)

else:
    print("pick either +,-, / or * to calculate")