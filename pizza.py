pizzas = ['hawai', 'peperoni', 'salami']
friend_pizzas = pizzas[:]

pizzas.append('4 cheese')
friend_pizzas.append('cappacia')

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print(f"\nMy friends favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())