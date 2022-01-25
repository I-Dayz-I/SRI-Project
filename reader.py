
#Biblioteca que permite hacer split por varios caracteres
import re
import trie
import globals
import os
import visuals

def processQuery(query):
    splitquery =  re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', query)
    while True:
        try:
            splitquery.remove("")
        except:
            break
    if not globals.BanWords:
        globals.QueryList  = splitquery
    else:
        for word in splitquery:
            if word in globals.Expelled or word == "":
                splitquery.remove(word)
        globals.QueryList  = splitquery
    temptrie = trie.Trie("query")
    for word in  globals.QueryList:
        temptrie.InsertWord(word)
    
    globals.TrieQuery =temptrie

    
def ReadDocuments(Path:str)->None:

    # onlyfiles = [f for f in listdir(Path) if isfile(join(Path, f))]
    
    # for file in onlyfiles:
    #     openFile = open(Path + "\\" + file,'r')
    #     documentText = openFile.read()
    #     openFile.close()s
        
    #     Curate(documentText,file)
    directory = Path
    
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            os.path.join(root, subdirectory)
        for file in files:
            visuals.finalIntpb +=1
    try:
        increments = visuals.progressBarMaxValue/visuals.finalIntpb
    except:
        return
    visuals.ProgressBarText.Update(value = (str(visuals.currentIntpb) + "/" +str(visuals.finalIntpb)))
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            os.path.join(root, subdirectory)
        for file in files:
            visuals.currentIntpb+=1
            visuals.ProgressBarText.Update(value = (str(visuals.currentIntpb) + "/" +str(visuals.finalIntpb)))
            visuals.ProgressBar.Update(current_count=visuals.currentIntpb*increments)
            
            try:
                openFile = open(os.path.join(root, file))
                globals.fnamesList.append(file)
                documentText = openFile.read()
                openFile.close()
                globals.filedirection[file] = os.path.join(root, file)
                Curate(documentText,file)
            except:
                pass
    visuals.ProgressBar.Update(current_count=visuals.progressBarMaxValue)



def Curate(Text:str, File:str )->None:
    curedText = re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n',Text)
    temptrie = trie.Trie(File)
    for Word in curedText:
        
        if globals.BanWords:
            if Word in globals.Expelled or Word == "":
                continue
        
        temptrie.InsertWord(Word)
    globals.TrieList.append(temptrie)
    
    globals.CorpusDict[File] = temptrie
    


