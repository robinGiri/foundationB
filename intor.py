# this is single line comment

"""
this is multi line comment 
try using multi line with this """ """
"""

# print("hello world....")
#
# print(2 + 2)
#
#
# # button calling -->
# rec_number = int(input("please provide input: "))
# def activate():
#     print(type(rec_number))
#     if type(rec_number) != int:
#         print("Please enter number")
#         return
#     openDialer(int(rec_number))
#
#
# def dail(phone_number):
#     print(f"{phone_number} \n calling")
#
# def openDialer(key_pad_input):
#     if len(key_pad_input) > 10:
#         print("invalid number")
#         return
#     elif len(key_pad_input) < 10:
#         print("!0 digit number required")
#         return
#     dail(key_pad_input)
#     return
#
# activate()

# input
"""
ask anything from user input
"""

# string formatting
# name = input("Please enter your name: ")
# print(f"hi! {name}, How are you doing?")


# name = input("Please enter your name: ")
# age = input("Please enter your age: ")
#
# print(f"hi!, your name is {name}, and you are {age} yrs old")

name, age, location = input("Enter name and age and location (comma separated): ").split(",")

print(f"hi!, my name is {name}, and I'm {age} yrs old, I'm from {location}")
