
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

# ------------- ADVANCED SET OPERATIONS ------------------- #
# WHY SETS ARE USEFUL

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)


numbers = {1, 2, 3}
other_nums = {1, 3, 4}
nums = numbers.difference(other_nums)
plus_nums = other_nums.difference(numbers)
print(nums)
print(plus_nums)


local = {"Rolf"}
away = {"Bob", "Anne"}

chums = local.union(away)
print(chums)


art = {"Bob", "Vincent", "Leo", "Alphonso"}
science = {"Brian", "Leo", "Stephen", "Isaac"}

both = art.intersection(science)
print(both)


set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

both_num = set1.intersection(set2)
print(both_num)

