#the caret symbol ( ^ ) at the start of a regex is used  to indicate that 
# a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ( $ ) at the end of the regex to indicate the string must end
# with this regex pattern.

import re
beginsWithHello = re.compile(r'^Hello')
b = beginsWithHello.search("Hello world")
print(b.group())
print(beginsWithHello.search("He saild Hello "))

endsWithNumber = re.compile(r'\d$')
num = endsWithNumber.search("your number is 42")
print(num.group())
print(endsWithNumber.search('42 is your number'))

#The r'^\d+$' regular expression string matches strings that both begin
# and end with one or more numeric characters.

wholeStringIsNum = re.compile(r'^\d+$')
w = wholeStringIsNum.search('1234567890') 
print(w.group())
nw = wholeStringIsNum.search('123samyak456')
print(nw == None)

print(wholeStringIsNum.search('12 34567890') == None)