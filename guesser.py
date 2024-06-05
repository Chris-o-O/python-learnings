import random

try:
    top_range = int(input("Type a number:"))
except ValueError:
     print("a number please")

while True:
    if top_range <= 0:
        print("Please type a number greater than 0")
        top_range = int(input("Type a number:"))
    else:
        break

random_number = random.randint(1,top_range)

print(random_number)