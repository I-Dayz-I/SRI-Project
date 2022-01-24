
#Biblioteca que permite hacer split por varios caracteres
import re
import trie
import globals
import os
import visuals

def processQuery(query):
    splitquery =  re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', query)
    if not visuals.OmitCheckbox.Value:
        globals.QueryList  = splitquery
    else:
        for word in splitquery:
            if word in globals.Expelled:
                splitquery.remove(word)
        globals.QueryList  = splitquery
        

    
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
            os.path.join(root, subdirectory)
        for file in files:
            visuals.finalIntpb +=1
            
    increments = visuals.progressBarMaxValue/visuals.finalIntpb
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
    curedText = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|\\n|\/',Text)
    temptrie = trie.Trie(File)
    for Word in curedText:
        
        if visuals.OmitCheckbox.Value:
            if Word in globals.Expelled:
                continue
        
        temptrie.InsertWord(Word)
    globals.TrieList.append(temptrie)
    
    globals.CorpusDict[File] = temptrie
    


