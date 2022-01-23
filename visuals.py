import PySimpleGUI as sg
import os
sg.theme('DarkAmber')





TrieCheckBox  = sg.Checkbox(enable_events = True,key =  "-TRIE-",text = "Linked Trie", default  = False)
NltkCkeckbox = sg.Checkbox(enable_events = True,key =  "-NLTK-",text = "nltk Library", default = True )
AlphaCheckbox = sg.Checkbox(enable_events = True,key =  "-INTCHECK-",text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)

currentIntpb = 0
finalIntpb = 0
progressBarMaxValue = 20000

ProgressBar = sg.ProgressBar(max_value=progressBarMaxValue,size=(60, 20))
ProgressBarText = sg.Text(str(currentIntpb) + "/" +str(finalIntpb))

file_list_column = [
    [
            sg.Text("Processing Algorithm:",justification="right", )  ,
    ],
    [
        TrieCheckBox,
        NltkCkeckbox,
    ],
      # [ sg.VSeparator()],
    [
    sg.Text("α: ",justification="right", )  ,
    sg.In(enable_events=True, key="-ALPHA INPUT-",),
    AlphaCheckbox,
    sg.Text(" (Default: 0.4 )",justification="right", )  ,
    ],
    
    [
        sg.HSeparator()],
    [
        sg.Text("Source Folder:"),
        sg.In(enable_events=True, key="-FOLDER-",default_text="Folder Adress",),
        sg.FolderBrowse(),
    ],
    [
        #Progress Bar
    ProgressBarText,
    ProgressBar,
    ],
    [sg.Text("List of Files:")],
    [
        sg.Listbox(
            values= [],enable_events = True,s=(100,100),horizontal_scroll=True,
            key = "-FILE LIST-"
        )
        
    ],

    [
    ],
    
]






view_column = [
    
]



# result_column = [
#     [sg.Text("Results:")],
#     [sg.Text(size = (40,1),key="-TOUT-")],
#     [sg.Listbox(
#             values= [],enable_events = True,size =(40,20),
#             key = "-RESULT LIST-"
#         )],
# ]
query_column = [

    [sg.Text("Query:")],
    [
        sg.Multiline(s=(900,20),enable_events=True, key="-QUERY-"),
    ],
    [
        sg.Button(button_text="Submit",enable_events=True, key= "-SUBMIT-")   
    ],
    [
    sg.HSeparator()
    ],
        [sg.Text("Results:")],
    [sg.Listbox(
            values= [],enable_events = True,s=(900,40),horizontal_scroll=True,
            key = "-RESULT LIST-"
        )],
]



layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(query_column),
    ]
]


        
        
        