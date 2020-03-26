#The dot-star will match everything except a newline. By passing re.DOTALL as
# the second argument to re.compile() , you can make the dot character match
# all characters, including the newline character.
import re

noNewlineRegex = re.compile('.*')
ex1 = noNewlineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print(ex1.group())

NewlineRegex = re.compile('.*', re.DOTALL)
ex2 = NewlineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print(ex2.group())
