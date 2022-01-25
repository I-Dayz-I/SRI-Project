import PySimpleGUI as sg
import os
sg.theme('DarkAmber')





LinkedTrieCheckBox  = sg.Checkbox(enable_events = True,key =  "-LINKTRIE-",text = "Linked Trie", default  = False)
TrieCkeckbox = sg.Checkbox(enable_events = True,key =  "-TRIE-",text = "Trie", default = True )
AlphaCheckbox = sg.Checkbox(enable_events = True,key =  "-INTCHECK-",text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox = sg.Checkbox(enable_events = True,key =  "-SLACKCHECK-",text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
OmitCheckbox = sg.Checkbox(enable_events = True,key =  "-SKIP-",text = "Skip unnecesary words in the search(pronouns,articles,etc...)", default = False ,  disabled=False)


currentIntpb = 0
finalIntpb = 0
progressBarMaxValue = 20000

ProgressBar = sg.ProgressBar(max_value=progressBarMaxValue,size=(50, 20))
ProgressBarText = sg.Text(str(currentIntpb) + "/" +str(finalIntpb))

file_list_column = [
    [
            sg.Text("Processing Algorithm:",justification="right", )  ,
    ],
    [
        LinkedTrieCheckBox,
        TrieCkeckbox,
    ],
    [
    sg.HSeparator(),
    ],
    [
    
    OmitCheckbox
    ],
    [
    sg.HSeparator(),
    ],
    [
    sg.Text("Slack of Result:",justification="right", )  ,
    sg.In(enable_events=True, key="-SLACK INPUT-",),
    SlackCheckbox,
    sg.Text(" (Default: 0.1 )",justification="right", )  ,
    ],
    # [ sg.VSeparator()],
    [
    sg.Text("         (alpha)α: ",justification="right", )  ,
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
            values= [],enable_events = True,s=(80,100),horizontal_scroll=True,
            key = "-FILE LIST-"
        )
        
    ],

    [
    ],
    
]






view_column = [
    [
    sg.Text("Not Showing:", key = "-DOCUMENT NAME-"),
    ],
    [
    sg.Multiline(s=(60,30),enable_events=True, key="-SHOW-",default_text="Click on a document of the list to show it here.",disabled=True,autoscroll=True)
    ],
    [
    sg.HSeparator()
    ],
    [
    sg.Text("Log:")
    ],
    [
        sg.Multiline(s=(60,30),enable_events=True, key="-LOG-",default_text="Execution Log:",disabled=True,autoscroll=True)
    ],
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
        sg.Multiline(s=(400,20),enable_events=True, key="-QUERY-"),
    ],
    [
        sg.Button(button_text="Submit",enable_events=True, key= "-SUBMIT-"),
        sg.Text("Time: ", key = "-TIME-")   
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
        sg.Column(view_column),
        sg.VSeparator(),
        sg.Column(query_column),
    ]
]


        
        
        