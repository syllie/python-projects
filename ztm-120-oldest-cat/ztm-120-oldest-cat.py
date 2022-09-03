#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
dax = Cat('Dax', 12)
moogie = Cat('Moogie', 13)
jojo = Cat('JoJo', 8)


# 2 Create a function that finds the oldest cat
def oldest_cat(cats):   
    return max([cat.age for cat in cats])



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
my_cats = [dax, moogie, jojo]    
print(f"The oldest cat is {oldest_cat(my_cats)} years old.")


# -------------- official solution ------------------------

# Find the oldest cat
def get_oldest_cat2(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat2(dax.age, moogie.age, jojo.age)} years old.")