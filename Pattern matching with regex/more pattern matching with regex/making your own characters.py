import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
v = vowelRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(v)