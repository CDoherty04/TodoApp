import functions
import PySimpleGUI as SimpGUI
import time
import os

if not os.path.exists("data.txt"):
    with open("data.txt", "w"):
        pass

SimpGUI.theme("Reds")

clock = SimpGUI.Text(time.strftime("%H:%M:%S"), key="clock")
label = SimpGUI.Text("Type in a todo: ")
input_box = SimpGUI.Input(tooltip="Enter a Todo here", key="todo")
add_button = SimpGUI.Button("Add")
list_box = SimpGUI.Listbox(values=functions.get_todos(), enable_events=True, size=(45, 10),
                           key="displayed_todos", no_scrollbar=True)
edit_button = SimpGUI.Button("Edit")
complete_button = SimpGUI.Button("Complete", key="complete")
exit_button = SimpGUI.Button("Exit", key="exit")

window = SimpGUI.Window(title="GUI Todo App",
                        font=("Montserrat", 15),
                        layout=[[clock],
                                [label],
                                [input_box, add_button],
                                [list_box, exit_button],
                                [edit_button, complete_button]])

while True:
    todos = functions.get_todos()
    event, values = window.read(timeout=100)  # Updates every 100ms or .1 second
    window["clock"].update(time.strftime("%H:%M:%S"))

    match event:
        case "Add":
            todos.append(values["todo"])
            functions.write_to_file(todos)
            window["displayed_todos"].update(values=todos)

        case "Edit":
            # If the list is empty or no task selected then the user can't edit
            if not values["displayed_todos"]:
                SimpGUI.popup("Select a task to edit")
                continue
            # todo: Only edit selected task, even if there's an identical one before
            todos[todos.index(values["displayed_todos"][0])] = values["todo"]
            functions.write_to_file(todos)
            window["displayed_todos"].update(values=todos)

        case "complete":
            # If the list is empty or no task selected then the user can't edit
            if not values["displayed_todos"]:
                SimpGUI.popup("Select a task to complete")
                continue
            # Remove item from list
            todos.pop(todos.index(values["displayed_todos"][0]))
            functions.write_to_file(todos)
            window["displayed_todos"].update(values=todos)
            # Empty text field
            window["todo"].update(value="")

        case "displayed_todos":
            window["todo"].update(value=values["displayed_todos"][0])

        # Exit conditions
        case SimpGUI.WIN_CLOSED:
            break
        case "exit":
            break

window.close()
