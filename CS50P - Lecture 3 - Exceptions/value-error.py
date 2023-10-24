# x = int(input("What's x? ")) # types string to see value error
# print(f"x is {x}")

try:
    x = int(input("Whats x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")