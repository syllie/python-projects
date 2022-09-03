import re

# Write a regex password checker that checks if a password
# is at least 8 char long
# contains any combination of letters, numbers and $%#@
# has to end with a number

pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d$")
pw = 'n0n0fUrBusine$$m8'

matches = pattern.fullmatch(pw)

if matches:
    print("valid password")
else:
    print("that's not right")

print(matches)
