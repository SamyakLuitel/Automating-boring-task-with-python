# in Nepal the landline has  3 parts +977-011-663399
# first one is code of Nepal , next is area code within Nepal

import re
landlineNepalRegex = re.compile(r'(\+\d\d\d-)?(\d\d\d-)?\d\d\d\d\d\d')
ph_no1 = landlineNepalRegex.search("Phone number of radio ABC is +977-011-663399")
print(ph_no1.group())

ph_no2 =landlineNepalRegex.search("for any question dial 663399")
print(ph_no2.group())

ph_no3= landlineNepalRegex.search("Kavretime : 011-663049")
print(ph_no3.group())