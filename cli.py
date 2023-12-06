"""add date features
#python date time format codes
#strftime("%b-%Y-%d-%H- %M:%s") function in module time-->returns string
#standard modules of python
#dir(time)-->gives all the time modules and variables

#important modules to learn -->csv,shutill,globe,webbrowser

#time module written in python installation directory
#functions is a module
"""
import functions
import time

now = time.strftime("%b %d , %Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        """if we pass a valid file name then the file name path in the main function will replace"""
        todos.append(todo + "\n")
        functions.write_todos(todos)
        """#remoc=ve the file path bcos it is defaultly assigned in main function"""

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        """ #in above file path called argument value"""

        for index, item in enumerate(todos):
            item = item.strip("\n")

            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the new todo : ")

            todos[number] = new_todo + "\n"
            functions.write_todos(todos, "todos.txt")

        except (ValueError, IndexError):
            print("Your command is not valid or there is no item with that number")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            functions.write_todos(todos, "todos.txt")
            print(f"The todo {todo_to_remove} removed")

        except (ValueError, IndexError):
            print("Your command is not valid or there is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye")
