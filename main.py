import os
import globals
import reader
import trie
from visuals import *
import vectorial
import PySimpleGUI as sg
import time


# directory = "./"
# reader.ReadDocuments(directory + "\\Tests")
# query = input()
# globals.QueryList = query


window = sg.Window("SRI", layout,size = (1600,800),resizable = True)

#App Loop
while True:
    event, values = window.read()
    
    #EXITING
    if event=="Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    
    
    if event == "-SUBMIT-" and values["-QUERY-"] != "":
        globals.wordsNotFound ={}
        globals.wordsNotFounList =[]
        globals.wordsList = []
        window["-LOG-"].write("\n"+"---------------------STARTING SEARCH------------------------")
        start =time.time()
        globals.FinalDocumentList=[]
        reader.processQuery(values["-QUERY-"])
        vectorial.FillingGlobals()
        if values["-TRIE-"] :
            vectorial.ExecutingVectorial()
        else:
            vectorial.ExecutingLinkVectorial()
        print(values["-QUERY-"])
        window["-RESULT LIST-"].update(globals.FinalDocumentList)
        end = time.time()
        window["-TIME-"].update("Time: " + str(end-start))
        
        if len(globals.wordsList) !=0:
            window["-LOG-"].write("\n"+"This word(s) were not found:" + str(globals.wordsList)+"\n"+"Maybe you should try this one(s):" +str(globals.wordsNotFounList))
        


    
    
    #Nor Check Boxes
    if event =="-TRIE-" or  TrieCkeckbox.Value :
        LinkedTrieCheckBox.Update(False)
    
    if event =="-TRIE-" and not LinkedTrieCheckBox.Value:
        TrieCkeckbox.Update(True)   
    
    if event == "-LINKTRIE-" or LinkedTrieCheckBox.Value:
        TrieCkeckbox.Update(False)   
    
    if event == "-LINKTRIE-" and not TrieCkeckbox.Value:
        LinkedTrieCheckBox.Update(True)   
    
    if event == "-INTCHECK-" and not AlphaCheckbox.Value:
            AlphaCheckbox.Update(False)
    if event == "-INTCHECK-" and AlphaCheckbox.Value:
            AlphaCheckbox.Update(True)

    if event == "-ALPHA INPUT-" :
        try:
            temp = float(values["-ALPHA INPUT-"])
            if 0<temp<=1:
                AlphaCheckbox.Update(True)
                AlphaCheckbox.Update(checkbox_color='green')
                globals.alphaValue = temp
                window["-LOG-"].write("\n"+"Alpha value successfully change.")
            else:
                AlphaCheckbox.Update(False)
                AlphaCheckbox.Update(checkbox_color='red')
                globals.alphaValue = 0.4
                pass
        except:
            AlphaCheckbox.Update(False)
            AlphaCheckbox.Update(checkbox_color='red')
            globals.alphaValue = 0.4
            pass
                
    if event == "-SLACKCHECK-" and not SlackCheckbox.Value:
            SlackCheckbox.Update(False)
    if event == "-SLACKCHECK-" and SlackCheckbox.Value:
            SlackCheckbox.Update(True)     
            
    if event == "-SLACK INPUT-":
        try:
            temp = float(values["-SLACK INPUT-"])
            if 0<temp:
                SlackCheckbox.Update(True)
                SlackCheckbox.Update(checkbox_color='green')
                globals.returnMinValue = temp
                window["-LOG-"].write("\n"+"Slack value successfully change.")
            else:
                SlackCheckbox.Update(False)
                SlackCheckbox.Update(checkbox_color='red')
                globals.returnMinValue = 0.1
                pass
        except:
            SlackCheckbox.Update(False)
            SlackCheckbox.Update(checkbox_color='red')
            globals.returnMinValue = 0.1
            pass        
    
    #if a Folder direction was chosen
    if event== "-FOLDER-":
        
        globals.CorpusDict = {}
        globals.WordCorpusCount = {}
        globals.CorpusInDoc = {}
        globals.MostRepeatedValue = {}
        globals.Frequency = {}
        globals.FinalDocumentList = []
        globals.QueryList = []
        globals.TrieList= []
        
        
        dir = values["-FOLDER-"]
        globals.fnamesList = []
        globals.TrieList = []
        globals.CorpusDict = {}
        file_list= globals.fnamesList
        window["-FILE LIST-"].update([])
        currentIntpb = 0
        finalIntpb = 0
        ProgressBarText.Update(value=(str(currentIntpb) + "/" +str(finalIntpb)))
        ProgressBar.Update(current_count=0)
        reader.ReadDocuments(dir)
        window["-LOG-"].write("\n"+"COMPILING DOCUMENTS OF:" +dir)
        
        window["-FILE LIST-"].update(file_list)
        window["-LOG-"].write("\n"+"COMPILING FINISHED" +dir)
        
    if event == "-FILE LIST-":
        try:
            file = globals.filedirection[values["-FILE LIST-"][0]]
            openfile = open(file)
            window["-SHOW-"].update(openfile.read())
            window["-DOCUMENT NAME-"].update("Showing: " + values["-FILE LIST-"][0])
            openfile.close()
        except:
            pass
        
    if event == "-RESULT LIST-":
        try:
            file = globals.filedirection[values["-RESULT LIST-"][0][1]]
            openfile = open(file)
            window["-SHOW-"].update(openfile.read())
            window["-DOCUMENT NAME-"].update("Showing: " + values["-RESULT LIST-"][0][1])
            openfile.close()
        except:
            pass

    if event == "-SKIP-" and not globals.BanWords:
        window["-LOG-"].write("\n"+"Skipping unnecesary words: TRUE")
        globals.BanWords =True
    
    elif event == "-SKIP-" and globals.BanWords:
        window["-LOG-"].write("\n"+"Skipping unnecesary words: FALSE")
        globals.BanWords =False
        


print(globals.CorpusDict)
    
    
    
    