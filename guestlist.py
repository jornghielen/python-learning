guest_list = ['kristin', 'hetty', 'mark', 'ires']

print(f"Hello {guest_list[0].title()}, would you like to join me for dinner tonight?")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner tonight?")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner tonight?")
print(f"Hello {guest_list[3].title()}, would you like to join me for dinner tonight?")

guest_declined = 'ires'

guest_list.remove(guest_declined)

print(f"\n{guest_declined.title()} declined the invite.")

guest_list.insert(0, 'oma nel')

print(f"\nHello {guest_list[0].title()}, I have some extra space! Would you like to join me for dinner tonight?")
print(f"Hello {guest_list[1].title()}, would you like to join me for dinner tonight?")
print(f"Hello {guest_list[2].title()}, would you like to join me for dinner tonight?")
print(f"Hello {guest_list[3].title()}, would you like to join me for dinner tonight?")

popped_guest_list = guest_list.pop()
popped_guest_list2 = guest_list.pop(-1)

print("\nHello everyone, here are some updates about our dinner.")
print(f"\nDue to some external influcances I can only host the dinner for 2 people.")
print(f"I'm so sorry {popped_guest_list.title()}! I won't have enough space to have you at dinner, therefor we need to set a new date. ")
print(f"I'm so sorry {popped_guest_list2.title()}! I won't have enough space to have you at dinner, therefor we need to set a new date. ")
print(f"{guest_list[1].title()} you are welcome to join me for dinner.")
print(f"{guest_list[0].title()} you are welcome to join me for dinner.")
print(f"\nAll the best, Jorn")

# Cleaning the list.
del guest_list[0]
del guest_list[0]
print(guest_list)