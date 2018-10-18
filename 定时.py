import re
 
string="54446446‘"
print re.findall(r"\d+\.?\d*",string)