#Regular expressions can not only find text patterns but can also substitute
# new text in place of those patterns. The sub() method for Regex objects is
# passed two arguments. The first argument is a string to replace any matches.
# The second is the string for the regular expression. The sub() method returns
# a string with the substitutions applied.


import re

namesRegex = re.compile(r'Agent \w+')
name = namesRegex.sub("CENSORED","Agent Alice gave the secret documents to Agent Bob.")
print(name)


agentNamesRegex = re.compile(r'Agent (\w)\w*')
agent = agentNamesRegex.sub(r'\1*****',"Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(agent)