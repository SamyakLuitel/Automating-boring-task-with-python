import re
haRegex = re.compile(r'(ha){3}')
h = haRegex.search("hahaha")
print(h.group())

h1 = haRegex.search('ha')
print (h1 == None)