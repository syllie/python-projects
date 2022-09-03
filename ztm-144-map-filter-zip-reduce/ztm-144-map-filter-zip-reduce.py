from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# as an exercise with 'map'
def capitalize_name(name):
    return name.capitalize()

print(list(map(capitalize_name, my_pets)))

# with a lambda function
print(list(map(lambda item: item.capitalize(), my_pets)))

# easiest: list comprehension
print([pet.capitalize() for pet in my_pets])


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

# with filter function
def larger_than(item):
    return item > 50

print(list(filter(larger_than, scores)))

# with a lambda function
print(list(filter(lambda item: item > 50, scores)))

# as list comprehension
print([number for number in scores if number > 50])


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def combine_numbers(acc, item):
    return acc + item

print(reduce(combine_numbers, my_numbers, reduce(combine_numbers,scores) ))
    
# remember that you can combine 2 lists by simply running an addition
print(my_numbers + scores)
print(reduce(combine_numbers, my_numbers + scores))

# with a lambda function
print(reduce(lambda acc, item: acc + item, my_numbers + scores))
