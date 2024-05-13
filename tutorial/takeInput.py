def yourName(name):
    print(f"Your name is {name}");

userName = input("Your name: ");
yourName(userName);

def add_two_values(first, second):
    return first + second;

number_1 = 10
number_2 = 3
sum = add_two_values(number_1, number_2)

print(f"{number_1} + {number_2} = {sum}")

def evenOrOddNumber(number):
    if int(number) == 0 or not number.isdigit():
        print(f"{number} this is zero or not number")
    elif int(number) % 2 == 0:
        print(f"{number} this is even numebr.")
    else:
        print(f"{number} this is odd number")
    
evenOrOddNumber(input("Please insert a number: "))