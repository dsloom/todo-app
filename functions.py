# constants put on the top

filepath = "todos.txt"


def get_todos(file_path=filepath):
    # in above file path is called parameter
    """read a text file and returs the lis of todo items
    """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
    # returns as a list
    # print(help(get_todos))


def write_todos(todos_arg, file_path=filepath):
    """write the to - do items list in the text file"""
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    # the code in the if statement execute only when this program executed directly
