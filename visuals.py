import PySimpleGUI as sg


file_list_column = [
    [
        sg.Text("Source Folder"),
        sg.In(size=(25,1),enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values= [],enable_events = True,size =(40,20),
            key = "-FILE LIST-"
        )
        
    ],
    
]


image_viewer_column = [
    [sg.Text("Results:")],
    [sg.Text(size = (40,1),key="-TOUT-")],
    [sg.Label(key="-IMAGE-")],
]


layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]


def execute_app():
    pass

window = sg.Window("SRI", layout)


while True:
    event, values = window.read()
    if event=="Exit" or event == sg.WIN_CLOSED:
        break

window.close()