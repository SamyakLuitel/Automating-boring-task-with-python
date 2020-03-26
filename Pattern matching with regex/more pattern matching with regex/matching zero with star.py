#the * (called star or asterisk) means "Maching zero or more"
# the group that precedes the star can occur any number of times in the text.
# It can be completely absent or repeated over and over again.


import re
batRegex = re.compile(r"Bat(wo)*man")
bat1 = batRegex.search("The adventures of Batman")
print(bat1.group())

bat2 = batRegex.search("The adventures of Batwoman")
print(bat2.group())
