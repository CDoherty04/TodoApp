FILE_NAME = "data.txt"


def parse(file_name):
    """Separates the lines of a file as a list"""
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines


def print_tasks(file_name=FILE_NAME):
    """Prints the lines from a specified file with a '1) task\n' format"""
    tasks = parse(file_name)
    for index, task in enumerate(tasks):
        print(f"{index+1}) {task.title()}")


def get_todos(file_name=FILE_NAME):
    """Returns the lines from a specified file as a list"""
    return parse(file_name)


def write_to_file(todos, file_name=FILE_NAME):
    """Takes a list and formats it to a file by line"""
    with open(file_name, "w") as file:
        for task in todos:
            file.write(task + "\n")
