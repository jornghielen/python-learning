# Store information about a pizza being ordered.
pizza = {
    'crust': 'tick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with thte following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")