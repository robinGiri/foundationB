from datetime import date
# add two numbrs
x , y = input("Please enter two numbers for addition (comma seprated):").split(",")
x = int(x)
y = int(y)


def additionFunction(x, y):
  z = x+y
  return z

print(f"The sum is  {additionFunction(x, y)}")

# enter brand name and know you configuration
laptop_name, model_name, price_amount  = input("Please enter your laptop's Brand Name, Model name and Price(comma seprated):").split(",")

def showBrandName(name, model, price):
  available_at = date.today()
  return f"Brand Name: {name} Model Name: {model} Available At: {available_at} @ Nrs.{price}"

print(f"{showBrandName(laptop_name, model_name, price_amount)}")
