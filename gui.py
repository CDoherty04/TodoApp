import functions
import PySimpleGUI as SimpGUI

label = SimpGUI.Text("Todo: ")
input_box = SimpGUI.Input(tooltip="Enter a Todo here", key="todo")
add_button = SimpGUI.Button("Add")
list_box = SimpGUI.Listbox(values=functions.get_todos(), enable_events=True, size=(45, 10), key="displayed_todos")
edit_button = SimpGUI.Button("Edit")

window = SimpGUI.Window(title="GUI Todo App",
                        layout=[[label],
                                [input_box, add_button],
                                [list_box, edit_button]],
                        font=("Times New Roman", 40))

while True:
    todos = functions.get_todos()
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos.append(values["todo"])
            functions.write_to_file(todos)
            window["displayed_todos"].update(values=todos)
        case "Edit":
            # If the list is empty or no task selected then the user can't edit
            if not values["displayed_todos"]:
                # Get this to print on screen
                print("Select a todo before editing")
                continue
            todos[todos.index(values["displayed_todos"][0])] = values["todo"]
            functions.write_to_file(todos)
            window["displayed_todos"].update(values=todos)
        case "displayed_todos":
            window["todo"].update(value=values["displayed_todos"][0])

        case SimpGUI.WIN_CLOSED:
            break
window.close()
