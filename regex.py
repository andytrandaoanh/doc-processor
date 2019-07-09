import re

inputText = """





Start-up Case Studies 217

soon destroy t
 


"""

#CASE 1: The Business of Software 5
#regexPat = re.compile(r'^\n+[\w\s]+\d+$',  re.M)

#CASE 2: 6 The Business of Software
#regPat = re.compile(r'^\n+\d+[\w\s]+\n+$',  re.M)

regPat = r'^\n+[\w\s,-]+\d+\n+$'
pattern = re.compile(regPat, re.M)
finds = re.findall(pattern, inputText)
#outputText = re.sub(pattern, '', inputText)

#newText = re.sub(r'\n\s{8}', '', inputString)
#print(newText) 

print(finds)