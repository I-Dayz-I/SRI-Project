
#Biblioteca que permite hacer split por varios caracteres
import re
import trie
import globals
import os
import visuals


    
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
                Curate(documentText,file)
            except:
                pass
    visuals.ProgressBar.Update(current_count=visuals.progressBarMaxValue)



def Curate(Text:str, File:str )->None:
    curedText = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',Text)
    temptrie = trie.Trie(File)
    for Word in curedText:
        temptrie.InsertWord(Word)
        globals.TrieList.append(temptrie)
    
    globals.CorpusDict[File] = temptrie
    


