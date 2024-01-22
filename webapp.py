import streamlit as st
from random import choice
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_to_file(todos)


st.title("Charlie's Todo App")
st.subheader("For all of my organizational needs")

for task in todos:
    st.checkbox(task)

placeholders = ["Finish creating my web app", "Take the trash out",
                "Learn how to cook Dad's spaghetti", "WOOOOOOOOOOOOO",
                "Organize game night", "Volunteer for my church"]

placeholder = choice(placeholders)
st.text_input(label="Enter a Todo", placeholder=placeholder, on_change=add_todo, key="new_todo")


