# square
my_list= list(range(1,11))
my_list_squared = list(map(lambda item: item ** 2, my_list))
print(my_list_squared)

# advanced sort - sort the list with tuples based on the second value in the tuple
a = [(0,2), (4,3), (9,9), (10,-1)]

# tuple elements can be accessed using indices
print([item[1] for item in a])

# so we can sort on those using it as a key
a_sorted = sorted(a, key=lambda item: item[1])

print(a_sorted)