# Exercise - check for duplicates
some_list = ['a','b','c','b','d','m','n','n', 'n']

# that was easy.. using set.. BUT we are not allowed to use that .. apparently
# for char in set(some_list):
#   some_list.remove(char)

# print(*some_list)

dupes = []
handled = []
for char in some_list:
  if char in handled:  # not safe as it will add further occurences of char
    if char not in dupes: # extra check
      dupes.append(char)
  else:
    handled.append(char)

print(dupes)


# Let's try another approach
duplicates = []
for char in some_list:
  if some_list.count(char) > 1 and char not in duplicates:
    duplicates.append(char)

print(duplicates)