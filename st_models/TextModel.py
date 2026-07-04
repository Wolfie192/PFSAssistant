import streamlit as st


class TextModel:
    """
    Model for displaying markdown formatted text within
    the scenario.
    """
    def __init__(self, content: list[str]):
        self.content = content


    def render(self):
        if not self.content:
            st.info("Empty read aloud module.")
            return

        output = self.content[0]

        if len(self.content) > 1:
            for content in self.content[1:]:
                output += "\n\n&emsp;" + content

        st.markdown(output)