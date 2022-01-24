import re
import globals
import math


def FillingGlobals():
    
    for word in globals.QueryList:
        globals.WordCorpusCount[word]= {}
    
    #Buscando Cantidad de documentos que contienen la palabra:
    for word in globals.QueryList:
        WordDocumentsCount= 0
        WordInDoc = 0
        for file in globals.CorpusDict.keys():
            if globals.CorpusDict[file].Search(word) != 0 and globals.CorpusDict[file].Search(word) != None:
                WordDocumentsCount+=1
                WordInDoc =globals.CorpusDict[file].Search(word)
                globals.WordCorpusCount[word][file] = WordInDoc
            else:
                globals.WordCorpusCount[word][file] = 0
                
        globals.CorpusInDoc[word] = WordDocumentsCount

    for word in globals.QueryList:
        globals.WordInDocuments[word]= 0 
        for file in  globals.CorpusDict.keys():
            if globals.WordCorpusCount[word][file]> 0:
                globals.WordInDocuments[word] +=1

    for file in globals.CorpusDict.keys():
        print("Counting Max repetition in " + file)
        maxrepetition = 0
        for word in globals.QueryList:
            temp = globals.WordCorpusCount[word][file]
            if temp> maxrepetition:
                maxrepetition = temp
        
        globals.MostRepeatedValue[file] = maxrepetition
    

def ExecutingVectorial():
    
    print("Executing Vectorial")
    for word in globals.QueryList:
        globals.Frequency[word] = {}
        
        for file in globals.CorpusDict.keys():
            
            if globals.MostRepeatedValue[file] != 0 :#and globals.WordCorpusCount[word][file] != 0:
                
                if globals.WordInDocuments[word]!=0 :
                    logXrepeatedVal =math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
                else:
                    logXrepeatedVal = 0
                alphaXfrequency = (1-globals.alphaValue) * (globals.WordCorpusCount[word][file]/globals.MostRepeatedValue[file])
                globals.Frequency[word][file] =(globals.alphaValue + alphaXfrequency) * logXrepeatedVal
                print(globals.Frequency[word][file])
            else:
                globals.Frequency[word][file] = 0
    
    for file in globals.CorpusDict.keys():
        totalFrequency = 0
        for word in globals.QueryList:
            totalFrequency += globals.Frequency[word][file]
        if totalFrequency >= globals.returnMinValue:
            # addFileInOrder((file,totalFrequency))
            globals.FinalDocumentList.append(("Name :",file," Value:",totalFrequency))
            

def ExecutingLinkVectorial():
    
    print("Executing Vectorial")
    for word in globals.QueryList:
        globals.Frequency[word] = {}
        
        for file in globals.CorpusDict.keys():
            
            if globals.MostRepeatedValue[file] != 0 :#and globals.WordCorpusCount[word][file] != 0:
                
                if globals.WordInDocuments[word]!=0 :
                    logXrepeatedVal =math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
                else:
                    logXrepeatedVal = 0
                alphaXfrequency = (1-globals.alphaValue) * (globals.WordCorpusCount[word][file]/globals.MostRepeatedValue[file])
                globals.Frequency[word][file] =(globals.alphaValue + alphaXfrequency) * logXrepeatedVal
                print(globals.Frequency[word][file])
            else:
                globals.Frequency[word][file] = 0
    
    # for file in globals.CorpusDict.keys():
    #     for word in globals.QueryList:
    #         if 
            
    
    for file in globals.CorpusDict.keys():
        totalFrequency = 0
        for word in globals.QueryList:
            totalFrequency += globals.Frequency[word][file]
        if totalFrequency >= globals.returnMinValue:
            # addFileInOrder((file,totalFrequency))
            globals.FinalDocumentList.append(("Name :",file," Value:",totalFrequency))


def addFileInOrder(filetuple):
    print("adding file: "+ filetuple[0])
    inserted = False
    for index in range(len(globals.FinalDocumentList)):
        if filetuple[1] > globals.FinalDocumentList[index][1]:
            inserted =True
            globals.FinalDocumentList.insert(index,filetuple)
    if not inserted:
        globals.FinalDocumentList.append(filetuple)