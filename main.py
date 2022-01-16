import os
import globals
import reader
import trie
import visuals
import vectorial



directory = "./"
reader.ReadDocuments(directory + "\\Tests")
query = input()
globals.QueryList = query



print(globals.CorpusDict)
    
    
    
    