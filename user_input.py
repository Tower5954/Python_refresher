name = input("Please tell me your name: ")
print(name)

size_input = input("How big is your house? ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(round(square_metres, 2))
print(square_metres)
print(f"{square_feet} square feet is {square_metres:.2f} square metres")