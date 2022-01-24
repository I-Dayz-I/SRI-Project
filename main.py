import os
import globals
import reader
import trie
from visuals import *
import vectorial
import PySimpleGUI as sg



# directory = "./"
# reader.ReadDocuments(directory + "\\Tests")
# query = input()
# globals.QueryList = query


window = sg.Window("SRI", layout,size = (1300,800),resizable = True)

#App Loop
while True:
    event, values = window.read()
    
    #EXITING
    if event=="Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    
    
    if event == "-SUBMIT-":
        #Reseting Everything
        #Diccionario de documentos: key = Filename , value = Trie
        globals.CorpusDict = {}
        globals.WordCorpusCount = {}
        globals.CorpusInDoc = {}
        globals.MostRepeatedValue = {}
        globals.Frequency = {}
        globals.FinalDocumentList = []
        globals.QueryList = []
        
        
        vectorial.processQuery(values["-QUERY-"])
        vectorial.FillingGlobals()
        vectorial.ExecutingVectorial()
        print(values["-QUERY-"])
    
    
    
    #Nor Check Boxes
    if event =="-NLTK-" or  NltkCkeckbox.Value :
        TrieCheckBox.Update(False)
    
    if event == "-TRIE-" or TrieCheckBox.Value:
        NltkCkeckbox.Update(False)   
    
    if event == "-INTCHECK-" and not AlphaCheckbox.Value:
            AlphaCheckbox.Update(False)
    if event == "-INTCHECK-" and AlphaCheckbox.Value:
            AlphaCheckbox.Update(True)

    if event == "-ALPHA INPUT-":
        try:
            temp = float(values["-ALPHA INPUT-"])
            if 0<temp<=1:
                AlphaCheckbox.Update(True)
                AlphaCheckbox.Update(checkbox_color='green')
                globals.alphaValue = temp
            else:
                AlphaCheckbox.Update(False)
                AlphaCheckbox.Update(checkbox_color='red')
                globals.alphaValue = 0.4
                pass
        except:
            pass
                
            
    
    #if a Folder direction was chosen
    elif event== "-FOLDER-":
        
        #window["-FOLDER-"].config(state='normal')
        
        
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
        
        window["-FILE LIST-"].update(file_list)
        
        


print(globals.CorpusDict)
    
    
    
    