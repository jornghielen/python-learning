squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


# Or do it shorter, aka nicer!
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# Or do it like this.
squares = [value**2 for value in range(1,11)]
print(squares)