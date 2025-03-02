import streamlit as sl

import functions

todo_list = functions.get_todo()

def new_todo():
    add_todo = sl.session_state["todo"] + "\n"
    todo_list.append(add_todo)
    functions.write_todo(todo_list)
    sl.session_state["todo"] = ""

sl.title("Todo Web App")
sl.subheader("My sample web app")

for index, item in enumerate(todo_list):
    checkbox = sl.checkbox(item, key=item)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo(todo_list)
        del sl.session_state[item]
        sl.rerun()


sl.text_input(label="",placeholder="add todo", on_change=new_todo, key="todo")
