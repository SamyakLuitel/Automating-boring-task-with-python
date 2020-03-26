# the | character is called a pipe 
# we use it to match pne of many expressions

import re

heroRegex =re.compile(r"Batman|Superman|Aquaman|Spiderman")
sup1 = heroRegex.search('Batman versus Superman')
print(sup1.group())

sup2 = heroRegex.search('Superman fears Batman')
print(sup2.group())

batRegex =re.compile(r'Bat(man|mobile|copter|bat)')
batman = batRegex.search("Batmobile is cool")
print(batman.group())
print(batman.group(1))
