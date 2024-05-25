# favorite = ["kingsman", "code geass", "jojo", "bleach", "hajime no ippo"]

# cars = []

# for i in range(5):
#     car = input("enter car name: ") 

# cars [0] = "bmw"

# print(f"the amount of cars in list is: {count}")



names = ["maxo", "gio", "nika", "luka", "giorgi"]
filtered_names = []

for name in names:
    if len(name) >= 4:
        filtered_names.append(name)

print(filtered_names)