import functions
import PySimpleGUI as SimpGUI

label = SimpGUI.Text("Todo: ")
input_box = SimpGUI.Input(tooltip="Enter a Todo here", key="todo")
add_button = SimpGUI.Button("Add")

window = SimpGUI.Window("GUI Todo App",
                        layout=[[label], [input_box, add_button]],
                        font=("Times New Roman", 40))

while True:
    todos = functions.get_todos()
    event, values = window.read()
    match event:
        case "Add":
            print(values["todo"])
            todos.append(values["todo"])
            functions.write_to_file(todos)
        case SimpGUI.WIN_CLOSED:
            break
window.close()
# Make a change without including \mega other child directories
