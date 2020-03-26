# all python regex funtions are il re module 
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# here d is for digit and \ is escape character 

phone_number = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone no:" +phone_number.group())