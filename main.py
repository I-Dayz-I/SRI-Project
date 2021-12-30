import os
import globals
import reader
import trie


Path = os.getcwd()
print("Current Working Direcctory is : "+ Path)
reader.ReadDocuments(Path + "\\Tests")
    
print(globals.CorpusDict)
    
    
    
    