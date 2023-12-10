import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app used to increase the productivity")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
print("hello")