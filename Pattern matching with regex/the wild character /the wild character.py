# The . (or dot) character in a regular expression is called a wildcard and will
# match any character except for a newline
import re
atRegex = re.compile(r'.at')
at = atRegex.findall('The cat in the hat sat on the flat mat.')
print(at)