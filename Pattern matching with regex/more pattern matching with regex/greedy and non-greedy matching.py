# Python’s regular expressions are greedy by default, which means that in 
# ambiguous situations they will match the longest string possible. 
# The non-greedy version of the curly brackets, which matches the shortest string 
# possible, has the closing curly bracket followed by a question mark.

import re
greedyHaRegex = re.compile(r'(ha){3,5}')
h1  = greedyHaRegex.search('hahahahaha')
print(h1.group())

nongreedyHaRegex = re.compile(r"(ha){3,5}?")
h2  = nongreedyHaRegex.search('hahahahaha')
print(h2.group())
