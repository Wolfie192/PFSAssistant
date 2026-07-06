import streamlit as st


class ReadAloudModel:
    def __init__(self, text: list[str]|str, first_line_indent: bool = True):
        self.first_line_indent = first_line_indent

        if isinstance(text, list):
            self.content = text
        elif isinstance(text, str):
            self.content = [text]

        self.render()


    def render(self):
        with st.container(border=True):
            st.markdown(f":green[{self.content[0]}]")
            if len(self.content) > 1:
                for text in self.content[1:]:
                    if self.first_line_indent:
                        st.markdown(f":green[&emsp;{text}]")
                    else:
                        st.markdown(f":green[{text}]")