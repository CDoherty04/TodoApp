import functions
import PySimpleGUI as SGui

label = SGui.Text("Todo: ")
input_box = SGui.Input(tooltip="Enter a Todo here")

window = SGui.Window("GUI Todo App", layout=[[label], [input_box]])
window.read()
window.close()
# Make a change without including \mega other child directories
