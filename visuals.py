import PySimpleGUI as sg
import os

file_list_column = [
    [
        sg.HSeparator()],
    [
        sg.Text("Source Folder:"),
        sg.In(size=(25,1),enable_events=True, key="-FOLDER-",default_text="Folder Adress"),
        sg.FolderBrowse(),
    ],
    [sg.Text("List of Files:")],
    [
        sg.Listbox(
            values= [],enable_events = True,size =(40,10),
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
        sg.Multiline(size=(40,10),enable_events=True, key="-QUERY-"),
        
    ],
    [
        sg.Button(button_text="Submit",)   
    ],
    [
          sg.HSeparator()
    ],
        [sg.Text("Results:")],
   
    [sg.Listbox(
            values= [],enable_events = True,size =(40,10),
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

window = sg.Window("SRI", layout)

while True:
    event, values = window.read()
    if event=="Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    elif event== "-FOLDER-":
        dir = values["-FOLDER-"]
        try:
            file_list = os.listdir(dir)
        except:
            file_list= []