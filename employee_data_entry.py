#commit 1#

number_of_employees = int(input("Please state the number of employees you want to log:"))
print(f"The number of employees are: {number_of_employees}")

for index in range(number_of_employees):
    first_name = input(f"What is employee {index + 1}'s first name? ")
    last_name = input(f"What is employee {index + 1}'s last name? ")
    age = int(input(f"What is employee {index + 1}'s age? "))




#commit 2#

number_of_employees = int(input("Please state the number of employees you want to log:"))
print(f"The number of employees are: {number_of_employees}")

for index in range(number_of_employees):
    first_name = input(f"What is employee {index + 1}'s first name? ").capitalize()
    while first_name == "":
        first_name = input("Please enter a correct first name: ").capitalize()
    last_name = input(f"What is employee {index + 1}'s last name? ").capitalize()
    while last_name == "":
        last_name = input("Please enter a correct last name: ").capitalize()
    age = int(input(f"What is employee {index + 1}'s age? "))
    while age < 18 or age > 100:
        age = int(input("Please input valid age between 18 and 100: "))
    print(f"Employee {index + 1} details: {first_name} {last_name}, {age}")



#commit 3#

number_of_employees = int(input("Please state the number of employees you want to log:"))
print(f"The number of employees are: {number_of_employees}")
total_age = 0

for index in range(number_of_employees):
    first_name = input(f"What is employee {index + 1}'s first name? ").capitalize()
    while first_name == "":
        first_name = input("Please enter a correct first name: ").capitalize()
    last_name = input(f"What is employee {index + 1}'s last name? ").capitalize()
    while last_name == "":
        last_name = input("Please enter a correct last name: ").capitalize()
    age = int(input(f"What is employee {index + 1}'s age? "))
    while age < 18 or age > 100:
        age = int(input("Please input valid age between 18 and 100: "))
    print(f"Employee {index + 1} details: {first_name} {last_name}, {age}")
    total_age += age #this is so the age accumulates each time from 0

if total_age > 500:
    print(f"Total age is {total_age}")