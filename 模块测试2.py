
import re
list = ['i','am','a','girl','am','a','boy']
# list=[i.start() for i in re.finditer('am', list)]
new_list=list(filter(lambda x: re.match('am.*', x) != None, list))
print(list)
str1 = 'i am a boy am a girl.'
str2='am'
# setences_position = [i for i,x in enumerate(list) if x=='aa']
# for i in setences_position:
# list = [i for i in list if i != 'aa']

print (str1.find(str2))
