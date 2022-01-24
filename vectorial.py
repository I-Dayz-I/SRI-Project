import re
from globals import *
import math

def processQuery(query):
    QueryList  = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',query)

def FillingGlobals():
    
    #Buscando Cantidad de documentos que contienen la palabra:
    for word in QueryList:
        WordDocumentsCount= 0
        WordInDoc = 0
        for file in QueryList.keys():
            if CorpusDict[file].Search(word) != 0:
                WordDocumentsCount+=1
                WordInDoc =CorpusDict[file].Search(word)
                WordCorpusCount[word][file] = WordInDoc
            else:
                WordCorpusCount[word][file] = 0
                
        CorpusInDoc[word] = WordDocumentsCount


    for file in TrieList.keys():
        maxrepetition = 0
        for word in QueryList:
            temp = WordCorpusCount[word][file]
            if temp> maxrepetition:
                maxrepetition = temp
        
        MostRepeatedValue[file] = maxrepetition
    

def ExecutingVectorial():
    
    
    for word in QueryList:
        for file in TrieList.keys():
            
            if MostRepeatedValue[file] != 0:
               Frequency[word][file] =(alphaValue + (1-alphaValue) * (WordCorpusCount[word][file]/MostRepeatedValue[file])) * math.log(len(CorpusDict)/MostRepeatedValue[file])
            else:
                Frequency[word][file] = 0
    
    for file in TrieList.keys():
        totalFrequency = 0
        for word in QueryList:
            totalFrequency += Frequency[word][file]
        if totalFrequency >= returnMinValue:
            addFileInOrder((file,totalFrequency))
            


def addFileInOrder(filetuple):
    inserted = False
    for index in range(len(FinalDocumentList)):
        if filetuple[1] > FinalDocumentList[index][1]:
            inserted =True
            FinalDocumentList.insert(index,filetuple)
    if not inserted:
        FinalDocumentList.append(filetuple)