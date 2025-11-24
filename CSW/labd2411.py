import re
txt="hello world"
print(txt)
# x = re.findall("he...lo", txt)
# y = re.findall("^he", txt)
y = re.findall("world$", txt)
print(y)
if y:
    print("yes, there is a match")
else:
    print("no match")

# import re

# pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

# s = input('Enter tel. number: ')
# if re.match(pattern, s):
#     print('Number accepted.')
# else:
#     print('Incorrect format.')

    