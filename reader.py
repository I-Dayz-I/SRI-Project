
#Biblioteca que permite hacer split por varios caracteres
import re
import trie
import globals
import os



    
def ReadDocuments(Path:str)->None:

    # onlyfiles = [f for f in listdir(Path) if isfile(join(Path, f))]
    
    # for file in onlyfiles:
    #     openFile = open(Path + "\\" + file,'r')
    #     documentText = openFile.read()
    #     openFile.close()
        
    #     Curate(documentText,file)
    directory = Path
    
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
        for file in files:
            openFile = open(os.path.join(root, file))
            documentText = openFile.read()
            openFile.close()
            Curate(documentText,file)
            print(os.path.join(root, file))
    
        

def Curate(Text:str, File:str )->None:
    curedText = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',Text)
    temptrie = trie.Trie(File)
    for Word in curedText:
        temptrie.InsertWord(Word)
        globals.TrieLis.append(temptrie)
    
    globals.CorpusDict[File] = temptrie
    


