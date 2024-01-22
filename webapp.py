import streamlit as st
import random

st.title("Charlie's Todo App")
st.subheader("For all of my organizational needs")

with open("data.txt", "r") as file:
    todos = file.readlines()

for todo in todos:
    st.checkbox(todo)

placeholders = ["Finish creating my web app", "Take the trash out",
                "Learn how to cook Dad's spaghetti", "WOOOOOOOOOOOOO",
                "Organize game night", "Volunteer for my church"]

placeholder = random.choice(placeholders)
st.text_input(label="Enter a Todo", placeholder=placeholder)
