import streamlit as st


class ReadAloudModel:
    """
    Model for displaying narrative text intended to be read
    aloud by the GM. Presented with a styled box and border
    with dark green text to be visually distinct.
    """
    def __init__(self, content: list[str]):
        self.content = content


    def render(self):
        if not self.content:
            st.info("Empty read aloud module.")
            return

        output = f":green[{self.content[0]}]"

        if len(self.content) > 1:
            for content in self.content[1:]:
                output += "\n\n&emsp;" + f":green[{content}]"

        with st.container(border=True):
            st.markdown(output)