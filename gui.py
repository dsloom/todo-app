import functions
import PySimpleGUI as sg

import time
"""we have to create window, textbox, a label
 button
windows is a type (like list)
"""
sg.theme("Black")

clock = sg.Text("", key="time")
label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button =sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                    [label],
                    [input_box, add_button],
                    [listbox, edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:

    event, values = window.read(timeout=200)
    window["time"].update(time.strftime("%b %d , %Y %H:%M:%S"))
    print(event)
    print(values)
    match event :
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(todos)
        case "Edit":
            try:
                todos = functions.get_todos()

                todo_to_edit = values["todos"][0]
                index = todos.index(todo_to_edit)
                new_todo = values["todo"] + "\n"
                todos[index] = new_todo
                functions.write_todos(todos)
# for real time change of items in the list
                window["todos"].update(todos)
            except IndexError:
                print("Please select an Item first")


#whenever we select someting we have to see it on input box.
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todos = functions.get_todos()
                todo_to_remove = values["todos"][0]
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(todos)
# to update input window
                window["todo"].update(value="")
            except IndexError:
                print("Please select an Item first")

        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()