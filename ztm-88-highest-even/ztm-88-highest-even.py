def highest_even(li):
  return (max([x for x in li if not x % 2], default="no even items in list"))

print(highest_even([10,2,3,4,8,11]))
print(highest_even([1,3,11]))
print(highest_even([]))
print(highest_even([25,25,25,25,25,25,25,25,26,26,26,26,27,27,27,27,27]))

# alternative approaches
def highest_even_with_discards(li):
  while True:
    if not li:
      return "no even items in list"
    
    max_value = max(li)    
    if max_value % 2:
      li.remove(max_value)
    else:
      return max_value
print(highest_even_with_discards([10,2,3,4,8,11]))
print(highest_even_with_discards([1,3,11]))
print(highest_even_with_discards([]))
print(highest_even_with_discards([25,25,25,25,25,25,25,25,26,26,26,26,27,27,27,27,27]))

# That could possibly be faster with deduping and the a sort
def highest_even_dedupe_sort(li):
  deduped = sorted(list(set(li)), reverse=True)

  # we can process the list in forward direction, the first item that is 
  # divisible by 2 is the highest even
  for item in deduped:
    if not item % 2:
      return item

  return "no even items in the list"

print(highest_even_dedupe_sort([10,2,3,4,8,11]))
print(highest_even_dedupe_sort([1,3,11]))
print(highest_even_dedupe_sort([]))
print(highest_even_dedupe_sort([25,25,25,25,25,25,25,25,26,26,26,26,27,27,27,27,27]))
  