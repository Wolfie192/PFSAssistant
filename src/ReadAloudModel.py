import streamlit as st


class ReadAloud:
    def __init__(self, text: list[str]|str, indent: str|None = "first_line"):
        self.indent = indent

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
                    if self.indent == "first_line":
                        st.markdown(f":green[&emsp;{text}]")
                    else:
                        st.markdown(f":green[{text}]")