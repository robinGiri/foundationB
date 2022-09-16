#loops in python

#range function in python
#print("This range from 1 to 10 is: {range{1, 10+1}")

# list object
from asyncio import constants


num_list = []

days_in_week = [
  "Sun",
  "Mon",
  "Tues",
  "Wed",
  "Thurs",
  "Frid",
  "Sat"
]


for num in range(1,11):
  print(f"This is the munber in range: ---> {num}")
  num_list.append(num)

print(num_list)

counter = 0
for day in days_in_week:
  counter += 1
  print(f"The {counter} of the day is: {day}")

#enumerate
for position, day in enumerate(days_in_week):
  print(f"The {position + 1} position in day is: --> {day}")

odd_list = []
even_lits = []
def filter_odd_even(user_provided_number):
  for num in range(0, user_provided_number):
    if num % 2 == 0:
      even_lits.append(num)
    else:
      odd_list.append(num)

any_number = int(input(f"Please provide you number: "))
filter_odd_even(any_number)

print(f"Now, the odd list is: {odd_list}")
print(f"Now, the even list is: {even_lits}")
