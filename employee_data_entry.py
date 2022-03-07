number_of_employees = int(input("Please state the number of employees you want to log:"))
print(f"The number of employees are: {number_of_employees}")

for index in range(number_of_employees):
    first_name = input(f"What is employee {index + 1}'s first name? ")
    last_name = input(f"What is employee {index + 1}'s last name? ")
    age = int(input(f"What is employee {index + 1}'s age? "))