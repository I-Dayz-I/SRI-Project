import re
from globals import *

def processQuery(query):
    QueryList = curedQuery = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',query)

def findingResult():
    
    #Buscando Cantidad de documentos que contienen la palabra:
    for word in QueryList:
        WordDocumentsCount= 0
        for file in QueryList.keys():
            if CorpusDict[file].Search(word) != -1:
                WordDocumentsCount+=1

        for file in CorpusDict.keys():
            tempCount = CorpusDict[file].Search(word)
            
            CorpusSolutionDict[file][word] = (alphaValue + (1- alphaValue)*(tempCount)  )
            
            