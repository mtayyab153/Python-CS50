name = input("What's your name? ").strip().title()

# Capitalize name
# name = name.strip().title()

# Capitalize each word
# name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"Hello, {first}")