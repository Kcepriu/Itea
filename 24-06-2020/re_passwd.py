import re
result = re.match('^\w*((\d[a-z])+|([a-z]\d)+)\w*', 'a11')
#result = re.match('^[a-z0-9]*', '123a4567')

print(result)