import re

inputString = """

PART ONE



"""

#CASE 1: The Business of Software 5
#regexPat = re.compile(r'^\n+[\w\s]+\d+$',  re.M)

#CASE 2: 6 The Business of Software
#regPat = re.compile(r'^\n+\d+[\w\s]+\n+$',  re.M)



regPat = re.compile(r'^\n+PART TWO\n+$',  re.M)
finds = re.findall(regPat, inputString)
#newText = re.sub(r'\n\s{8}', '', inputString)
#print(newText) 

print(finds)