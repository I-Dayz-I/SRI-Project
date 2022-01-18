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
    
    
    #Nor Check Boxes
    if event =="-NLTK-" or  NltkCkeckbox.Value :
        TrieCheckBox.Update(False)
    
    if event == "-TRIE-" or TrieCheckBox.Value:
        NltkCkeckbox.Update(False)   
    
    
    
    #if a Folder direction was chosen
    elif event== "-FOLDER-":
        dir = values["-FOLDER-"]
        try:
            file_list = os.listdir(dir)
        except:
            file_list= []
        
        


print(globals.CorpusDict)
    
    
    
    