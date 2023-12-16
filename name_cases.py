#### Variables
first_name = "jorn "
last_name = " ghielen "
full_name = f"{first_name.rstrip()} {last_name.strip()}"
famous_name = "albert einstein"

#### 2-3 Personal Message:
message = f"Hello {full_name.title()}, would you like to learn some Python today?"
print(message)

#### 2-4 Name Cases:
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

#### 2-5 Famous Qoute:
famous_qoute = f'{famous_name.title()} once said, "A person who never made a mistake never tried anything new."'
print(famous_qoute)

#### 2-6 Stripping Names:
print("People that are smart:\n\tAlbert Einstein\n\tElon Musk\n\tThomas Edison")
