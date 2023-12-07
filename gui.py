import functions
import PySimpleGUI as sg
"""we have to create window, textbox, a label
 button
windows is a type (like list)
"""
label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",layout=[[label], [input_box, add_button],
                    [listbox, edit_button]], font=("Helvetica", 20))

while True:

    event, values = window.read()
    print(event)
    print(values)
    match event :
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todos = functions.get_todos()
            todo_to_edit = values["todos"][0]
            index = todos.index(todo_to_edit)
            new_todo = values["todo"] + "\n"
            todos[index] = new_todo
            functions.write_todos(todos)
#for real time change of items in the list
            window["todos"].update(todos)
#whenever we select someting we have to see it on input box.
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break
window.close()