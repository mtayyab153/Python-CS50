# for i in [0, 1, 2]:
#     print("MEOW")


# for i in range(3):
#     print("MEOW")

# for _ in range(3):
#     print("MEOW")


# while True:
#     n = int(input("Wha's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("MEOW")


def main():
    number = get_number()
    meow(number)



def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break

    return n

def meow(n):
    for _ in range(n):
        print("MEOW")

main()