age = int(input("Please provide your age:"))

# conditional statements
# if block

"""
print("Code started ...")

if age > 18:
    print(f"You can play this game because you are above {age}")
else:
    print("You are too young for this program")

print("Code ended ...")

"""

if age <= 0:
    print("Please enter valid date")
elif 0 < age <= 10:
    print(f"Your age is {age}, and you ticket price is Rs. 100")
elif 10 < age <= 20:
    print(f"Your age is {age} and your movie ticket is Rs. 200")
else:
    print("your movie ticket is Rs. 300")
