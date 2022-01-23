import os
import re


tittle = False
author = False
Id = False
Corpus = False
b= False


file = 'cran.all.1400'
#fullpath =  os.path.join(root, file)
openFile = open(file)

pattern = re.compile(r'\.I +(?P<id>\d+) *\n'
                    r'\.T *\n'
                    r'(?P<name>(?:.|\n)*?)'
                    r'\.A *\n'
                    r'(?P<author>(?:.|\n)*?)'
                    r'\.B *\n'
                    r'(?P<bibliography>(?:.|\n)*?)'
                    r'\.W *\n'
                    r'(?P<text>(?:.|\n)*?)'
                    r'(?=(\.I)|$)')

documentMatches = re.finditer(pattern,openFile.read())
openFile.close()
for document in documentMatches:
    newfile = open(document['id'],"w+")
    newfile.write(document['text'])
    newfile.close()

print("A")