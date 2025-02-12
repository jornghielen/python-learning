motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] # Owned Motorcycles

# Print all owned motorcycles.
print(motorcycles)

# Specify the onces that are to expensive and removing them.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

# Message
print(f"\nA {too_expensive.title()} is too expensive for Joram.")
