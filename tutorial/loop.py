def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_numbers = []
odd_numbers = []
starting = 0
user_input = int(input("Limit: "))
while starting <= user_input:
    if is_even(starting):
        # print(f"{starting} is even")
        even_numbers.append(starting)
    else:
        # print(f"{starting} is odd")
        odd_numbers.append(starting)

    starting = starting + 1



print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print("Finished While Loop")

# 2 for loop

even_numbers = []
odd_numbers = []

for every_value in range(0, user_input + 1):
    if is_even(every_value):
        even_numbers.append(every_value)
    else:
        odd_numbers.append(every_value)


print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print("Finished For Loop")


# 3 continue and break

grocery = ["rice", "water", "tomato", "ginger"]

for item in grocery:
    if item == "water":
        continue
    print(item)

for item in grocery:
    if item == "tomato":
        break
    print(item)



for i in range(0, 10, 3):
    print("For loop: ",i)


for i in range(0, len(grocery)):
    print(i)