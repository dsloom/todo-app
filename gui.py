import functions
import PySimpleGUI as sg
"""we have to create window, textbox, a label
 button
windows is a type (like list)
"""
label = sg.Text("Type in a to do")

input_box = sg.InputText(tooltip = "Enter todo")

add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label],[input_box,add_button]])

window.read()
window.close()