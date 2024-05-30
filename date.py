import re

txt = "The rain in Spain"
x = re.sub("\s", ":", txt,1)
print(x)