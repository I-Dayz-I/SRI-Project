import PySimpleGUI as sg
import os
sg.theme('DarkAmber')





TrieCheckBox  = sg.Checkbox(enable_events = True,key =  "-TRIE-",text = "Linked Trie", default  = False)
NltkCkeckbox = sg.Checkbox(enable_events = True,key =  "-NLTK-",text = "nltk Library", default = True )



file_list_column = [
    
        [
            sg.Text("Processing Algorithm:",justification="right", )  ,
        ],
        [
        TrieCheckBox,
        NltkCkeckbox,
        sg.VSeparator(),
    
        ] ,
        
 
    
    [
        sg.HSeparator()],
    [
        sg.Text("Source Folder:"),
        sg.In(enable_events=True, key="-FOLDER-",default_text="Folder Adress",),
        sg.FolderBrowse(),
    ],
    [sg.Text("List of Files:")],
    [
        sg.Listbox(
            values= [],enable_events = True,s=(100,100),
            key = "-FILE LIST-"
        )
        
    ],
    [
          
    ],
    
]



options_column=[
    [
        sg.Text("Options:"),
    ]
    
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
        sg.Button(button_text="Submit",)   
    ],
    [
          sg.HSeparator()
    ],
        [sg.Text("Results:")],
   
    [sg.Listbox(
            values= [],enable_events = True,s=(900,40),
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


        
        
        