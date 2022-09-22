numbers = [1, 3, 5]

doubled = []

# Normal way but longer way #
for num in numbers:
    doubled.append(num * 2)

print(doubled)

#   LIST COMPREHENSION  #

dbl_lst = [x * 2 for x in numbers]
print(dbl_lst)

friends = ["Rolf", "Sam", "Samantha", "Sauron", "Jen", "Reginald", "Ruppert"]
starts_s = []

# for loop way #
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

# LIST COMPREHENSION WAY #
starts_r = [x for x in friends if x.startswith("R")]
print(starts_r)


print("Friends: ", id(friends), "\n" "starts_r: ", id(starts_r))