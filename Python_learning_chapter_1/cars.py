cars_owned = ['seat', 'bmw', 'renault',]

for car_owned in cars_owned:
    if car_owned == 'bmw':
        print(car_owned.upper())
    else:
        print(car_owned.title())

print("Here is the orignal list:")
print(cars_owned)

print("\nHere is the sorted list:")
print(sorted(cars_owned))

print("\nHere is the original list again:")
print(cars_owned)

print(len(cars_owned))