def add(x, y):
    return x + y


print(add(5, 7))

ladd = lambda x, y: x + y
print(ladd(7, 7))

print((lambda x, y: x * y)(8, 8))


def double(x):
    return x * 2


sequence = [1, 1, 2, 3, 5, 8, 13]
# list comprehension
doubled = [x * 2 for x in sequence]
print(doubled)
print("\n")
doubled_w_func = [double(x) for x in sequence]
print(doubled_w_func)

# --- using the map function --- #
doubled_w_map = list(map(double, sequence))
print(doubled_w_map)
print("\n")
trebled = [(lambda x: x * 3)(x) for x in sequence]
print(trebled)