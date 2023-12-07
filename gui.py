import functions
import PySimpleGUI as sg
"""we have to create window, textbox, a label
 button
windows is a type (like list)
"""
label = sg.Text("Type in a to do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button("Add")
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:

    event, values = window.read()
    print(event)
    print(values["todo"])
    match event :
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()