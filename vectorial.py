import re
import globals
import math
from difflib import SequenceMatcher


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
        globals.ContainsWord[word] = []
        for file in  globals.CorpusDict.keys():
            if globals.WordCorpusCount[word][file]> 0:
                globals.ContainsWord[word].append(file)
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
            
            if globals.WordCorpusCount[word][file] != 0 :#and globals.WordCorpusCount[word][file] != 0:
                
                if globals.WordInDocuments[word]!=0 :
                    logXrepeatedVal =math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
                else:
                    logXrepeatedVal = 0
                Nfrequency = (globals.WordCorpusCount[word][file]/globals.MostRepeatedValue[file])
                globals.Frequency[word][file] =(Nfrequency) * logXrepeatedVal
                print(globals.Frequency[word][file])
            else:
                globals.Frequency[word][file] = 0
    
    maxRepeatedValue = 0
    for word in globals.QueryList:
        temp = 0
        for word2 in globals.QueryList:
            if word == word2:
                temp+=1
        if temp>maxRepeatedValue:
            maxRepeatedValue = temp    
        
    globals.FrequencyQuery = {}
    for word in globals.QueryList:

        if globals.WordInDocuments[word] != 0:
            globals.FrequencyQuery[word] = (globals.alphaValue + (1-globals.alphaValue)*(globals.TrieQuery.Search(word)/ maxRepeatedValue))*math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
        else:
            globals.FrequencyQuery[word] = 0 

    for file in globals.CorpusDict.keys():
        sumMult = 0 
        sumQSq= 0
        sumDocSq=0
        for word in globals.QueryList:
            sumMult+= globals.Frequency[word][file]*globals.FrequencyQuery[word]
            sumDocSq += globals.Frequency[word][file] * globals.Frequency[word][file]
            sumQSq+= globals.FrequencyQuery[word] * globals.FrequencyQuery[word]
        
        sumQSq= math.sqrt(sumQSq)
        sumDocSq= math.sqrt(sumDocSq)
        if sumDocSq !=0:
            similitud = sumMult/(sumQSq*sumDocSq)
        else:
            similitud = 0
        if similitud >= globals.returnMinValue:
            #addFileInOrder(("Name :",file," Value:",similitud))
            globals.FinalDocumentList.append(("Name :",file," Value:",similitud))
    
    globals.FinalDocumentList.sort(key=lambda tup: tup[3],reverse=True)
    
    count =1
    for tuple in range(len(globals.FinalDocumentList)):
        globals.FinalDocumentList[tuple] = ("Rank :",count) +  globals.FinalDocumentList[tuple]
        count+=1
    NotFoundWords()
    
def ExecutingLinkVectorial():
    
    print("Executing Vectorial")
    for word in globals.QueryList:
        globals.Frequency[word] = {}
        
        for file in globals.CorpusDict.keys():
            
            if globals.WordCorpusCount[word][file] != 0 :#and globals.WordCorpusCount[word][file] != 0:
                
                if globals.WordInDocuments[word]!=0 :
                    logXrepeatedVal =math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
                else:
                    logXrepeatedVal = 0
                Nfrequency = (globals.WordCorpusCount[word][file]/globals.MostRepeatedValue[file])
                globals.Frequency[word][file] =(Nfrequency) * logXrepeatedVal
                print(globals.Frequency[word][file])
            else:
                globals.Frequency[word][file] = 0
    
    maxRepeatedValue = 0
    for word in globals.QueryList:
        temp = 0
        for word2 in globals.QueryList:
            if word == word2:
                temp+=1
        if temp>maxRepeatedValue:
            maxRepeatedValue = temp    
        
    globals.FrequencyQuery = {}
    for word in globals.QueryList:

        if globals.WordInDocuments[word] != 0:
            globals.FrequencyQuery[word] = (globals.alphaValue + (1-globals.alphaValue)*(globals.TrieQuery.Search(word)/ maxRepeatedValue))*math.log(len(globals.CorpusDict)/globals.WordInDocuments[word],10)
        else:
            globals.FrequencyQuery[word] = 0 

    for file in globals.CorpusDict.keys():
        sumMult = 0 
        sumQSq= 0
        sumDocSq=0
        for word in globals.QueryList:
            sumMult+= globals.Frequency[word][file]*globals.FrequencyQuery[word]
            sumDocSq += globals.Frequency[word][file] * globals.Frequency[word][file]
            sumQSq+= globals.FrequencyQuery[word] * globals.FrequencyQuery[word]
        
        sumQSq= math.sqrt(sumQSq)
        sumDocSq= math.sqrt(sumDocSq)
        if sumDocSq !=0:
            similitud = sumMult/(sumQSq*sumDocSq)
        else:
            similitud = 0
        if similitud >= globals.returnMinValue:
            #addFileInOrder(("Name :",file," Value:",similitud))
            globals.FinalDocumentList.append(("Name :",file," Value:",similitud))
    
    globals.FinalDocumentList.sort(key=lambda tup: tup[3],reverse=True)
    
    count =1
    for tuple in range(len(globals.FinalDocumentList)):
        globals.FinalDocumentList[tuple] = ("Rank :",count) +  globals.FinalDocumentList[tuple]
        count+=1
    NotFoundWords()
    FindVectorValue()


def FindVectorValue():
    analizedWords = []
    for tuple in range(len(globals.FinalDocumentList)):
        linkcount =0
        file = globals.FinalDocumentList[tuple][3]
        for word1 in globals.QueryList:
            if word1 in analizedWords:
                continue
            analizedWords.append(word1)
            for word2 in globals.QueryList:
                if word1 == word2:
                    continue
                if globals.CorpusDict[file].SearchFinalNode(word1) !=0 and globals.CorpusDict[file].SearchFinalNode(word1) !=None:
                    if globals.CorpusDict[file].SearchFinalNode(word2) in globals.CorpusDict[file].SearchFinalNode(word1).nextWord:
                        linkcount+=1
        globals.FinalDocumentList[tuple] = globals.FinalDocumentList[tuple] + ("Link Value: ",linkcount)
    pass


def NotFoundWords():
    file = 3
    globals.wordsNotFound ={}
    for word in globals.QueryList:
        
        if globals.WordInDocuments[word]==0:
            globals.wordsNotFound[word] = {}
            for tuple in globals.FinalDocumentList:
                doc = tuple[3]
                closeword = globals.CorpusDict[doc].SearchClosestWord(word)
                globals.wordsNotFound[word][doc] = ""
                if globals.wordsNotFound[word][doc] == "" or SequenceMatcher(None, word,globals.wordsNotFound[word][doc]) < SequenceMatcher(None, word, closeword).ratio():
                    globals.wordsNotFound[word][doc] = closeword
        else: pass
        
    globals.wordsNotFounList = []
    for word in globals.QueryList:
        if globals.WordInDocuments[word]==0:
            globals.wordsList.append(word)
        for tuple in globals.FinalDocumentList:
            if globals.WordInDocuments[word]==0:
                doc = tuple[3]
                if globals.wordsNotFound[word][doc]!="" and globals.wordsNotFound[word][doc]!= None:
                    if globals.wordsNotFound[word][doc] not in globals.wordsNotFounList:
                        globals.wordsNotFounList.append(globals.wordsNotFound[word][doc])
                