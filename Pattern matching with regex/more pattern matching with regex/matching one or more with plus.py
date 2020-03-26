#the + (or plus) means “match one or more.”
# the group preceding a plus must appear at least once.

import re
batRegex = re.compile(r'Bat(wo)+man')
bat1 = batRegex.search("The adventures of Batwoman")
print(bat1.group())

bat2 = batRegex.search("The adventures of Batwowowoman")
print(bat2.group())
