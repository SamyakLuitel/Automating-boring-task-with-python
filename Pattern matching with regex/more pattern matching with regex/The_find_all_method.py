#In addition to the search() method, Regex objects also have a findall()method. 
# While search() will return a Match object of the first matched text 
# in the searched string, the findall() method will return the strings of every 
# match in the searched string.


import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
ph_no = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print("search method :",ph_no.group())

ph_no2 = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print("findall  method", ph_no2)