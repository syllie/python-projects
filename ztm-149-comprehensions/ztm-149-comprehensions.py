print([(num, num * 2) for num in range(0,99) if not num % 3])

my_dict = {
    'name': 'test',
    'state': 'test',
    'score': 'not test'
}

my_new_dict = {key:value+'*' for key,value in my_dict.items() if key == 'score'}

print(my_new_dict)

# repeat the find_duplicates exercise from lesson 78 using comprehension
some_list = ['a','b','c','b','d','m','n','n', 'n']

print(list({char for char in some_list if some_list.count(char) > 1}))