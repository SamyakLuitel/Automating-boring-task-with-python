# You can use the dot-star ( .* ) to stand in for that “anything.” 
# Remember that the dot character means “any single character except the newline,”
#  and the star character means “zero or more of the preceding character.”

import re


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name = nameRegex.search('First Name: Samyak Last Name: Luitel')
print(name.group())
print(name.group(1))
print(name.group(2))


#nongreedy Mode
nongreedyRegex = re.compile(r'<.*?>')
non = nongreedyRegex.search("<To serve man> for dinner.>")
print(non.group())

#greedy 
greedyRegex = re.compile(r'<.*>')
g = greedyRegex.search("<To serve man> for dinner.>")
print(g.group())