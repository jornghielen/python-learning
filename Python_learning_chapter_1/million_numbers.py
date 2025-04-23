numbers = []
for value in range(1, 1000001):
    numbers.append(value)

min_value = min(numbers)
max_value = max(numbers)
sum_value = sum(numbers)

print(f"The lowest value in the list is {min_value}.\n")
print(f"The highest value in the list is {max_value}.\n")
print(f"The sum of all values in the list is {sum_value}.")