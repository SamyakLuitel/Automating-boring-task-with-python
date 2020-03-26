# the first 3 digits in phone no is area code 415-555-4242
# here 415 is the area code 
# we can extract the area code only by using grouping with parenthesis
 
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search("My phone no is 415-555-4242.")

print("area code" ,mo.group(1))
print("main number", mo.group(2))
print("full phone no", mo.group(0))
print('groups', mo.groups()) #mo.groups returns a tuple of multple group 