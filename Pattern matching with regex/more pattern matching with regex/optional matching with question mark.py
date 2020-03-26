# the ? character flags the groups that precedes it as an optional part of the pattern

import re
batRegex = re.compile(r'Bat(wo)?man')

bat1 = batRegex.search("The adventures of Batman")
print(bat1.group())

bat2 = batRegex.search("The adventures of Batwoman")
print(bat2.group())
