
#Biblioteca que permite hacer split por varios caracteres
import re
import trie
import globals
from os import close, listdir
from os.path import isfile, join


def ReadDocuments(Path:str)->None:

    onlyfiles = [f for f in listdir(Path) if isfile(join(Path, f))]
    
    for file in onlyfiles:
        openFile = open(Path + "\\" + file,'r')
        documentText = openFile.read()
        openFile.close()
        
        Curate(documentText,file)
        

def Curate(Text:str, File:str )->None:
    curedText = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',Text)
    temptrie = trie.Trie(File)
    for Word in curedText:
        temptrie.InsertWord(Word)
        globals.TrieLis.append(temptrie)
    
    globals.CorpusDict[File] = temptrie
    


