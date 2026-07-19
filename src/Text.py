import streamlit as st


def text(content: str, indent: str|None = "first_line"):
    match indent:
        case "first_line":
            st.markdown(f"&emsp;{content}")
        case _:
            st.markdown(content)


def read_aloud(content: list[str]):
    with st.container(border=True):
        for i, paragraph in enumerate(content):
            if i == 0:
                st.markdown(f":green[{paragraph}]")
            else:
                st.markdown(f"&emsp;:green[{paragraph}]")


def section_header(content: str):
    st.markdown(f"## :gray[{content}]")


def subsection_header(content: str):
    st.markdown(f"#### :gray[{content}]")