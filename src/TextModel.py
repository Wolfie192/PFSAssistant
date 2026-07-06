import streamlit as st


class TextModel:
    def __init__(self, text: list[str]|str, first_line_indent: bool = True):
        self.first_line_indent = first_line_indent

        if isinstance(text, list):
            self.content = text
        elif isinstance(text, str):
            self.content = [text]

        self.render()


    def render(self):
        st.markdown(self.content[0])
        if len(self.content) > 1:
            for text in self.content[1:]:
                if self.first_line_indent:
                    st.markdown(f"&emsp;{text}")
                else:
                    st.markdown(text)