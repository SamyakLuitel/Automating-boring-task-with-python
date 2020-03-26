# for case insensitive matching we pass  re.IGNORECASE or re.I as a second argument in re.compile()

import re
robocop = re.compile(r'robocop',re.I)
r1 = robocop.search("RoboCop is part man, part machine, all cop.")
print(r1.group())
r2 = robocop.search("ROBOCOP protects the innocent.")
print(r2.group())
r3 = robocop.search('Al, why does your programming book talk about robocop so much?')
print(r3.group())