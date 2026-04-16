total = 0
check = 'y'

while check == 'y':
    num = int(input("Enter the expense: "))

    if num > 0:
        total += num
    else:
        while num <= 0:
            num = int(input("Please enter a positive expense: "))
        total += num

    check = input("Enter 'y' if you want to enter more expenses: ")

print(f"Total expenses: {total}")



