
# -- LIST -- #
# lists are mutable
l = ["Bob", "Rolf", "Anne"]

# -- TUPLE -- #
# tuples are not mutable
t = ("Bob", "Rolf", "Anne")

# -- SET -- #
# sets are mutable and can do much of what
# lists and tuples can do. However, sets
# can not have duplicates and will not keep the
# order
s = {"Bob", "Rolf", "Anne"}

# -- ACCESS ELEMENTS -- #
# subscript notation
print(l[0])
print(t[2])

# no subscript notation for sets as they do not keep any order

# -- MODIFYING ELEMENTS IN A LIST -- #
l[0] = "Dave"
print(l[0])
print(l)

# append in a list
l.append("smith")
print(l)

# remove elements in a list
l.remove("Dave")
print(l)

# -- MODIFYING SETS -- #
s.add("Dave")
"""
Notice that its ADD and not APPEND,
when working with sets. That is because,
append means 'add at the end', but sets
dont have an 'end' since they dont have order
"""
print(s)