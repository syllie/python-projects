# my_file = open('test.txt')
# print(my_file.readlines())
# my_file.close()

with open('test.txt') as my_file:
    print(my_file.readlines())

# open file for write mode
# whenever you open a file, the cursor resets - so it starts writing at pos 0
# and it assumes it is a new file, so all content is wiped and only new text added
# open a file in write mode will create a file if it does not exist yet
with open('test.txt', 'w') as my_file:
    text = my_file.write('hey it\s me!')

# open file for read and write mode
# it overwrites text that exists, as opening the file will place curser at pos 0
# open a file in read/write mode will throw an error if it does not exist yet
# Open for reading and writing. The stream is positioned at the beginning of the file.
with open('test.txt', 'r+') as my_file:
    text = my_file.write(':(')
    print(text)

# open file for append
# it will append given text to the end of the file
with open('test.txt', 'a') as my_file:
    text = my_file.write(':)')
    print(text)
