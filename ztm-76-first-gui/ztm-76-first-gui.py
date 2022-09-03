# Exercise
# print 0 as space, 1 as *
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# for loops
# Note that pixel is 0 or 1 so can be used directly as boolean
for row in picture:
  result = ''
  for pixel in row:
    result += '*' if pixel else ' '
  print(result)

print('\n---------\n')

# list comprehension.
for row in picture:
  print(''.join(['*' if pixel else ' ' for pixel in row]))