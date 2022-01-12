import os
import globals
import reader
import trie
import visuals


Path = os.getcwd()
print("Current Working Direcctory is : "+ Path)
reader.ReadDocuments(Path + "\\Tests")
    
print(globals.CorpusDict)
    
    
    
    