import streamlit as st


class TextModel():
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

        stripped_content = []
        for content in self.content:
            stripped_content.append(content.strip())

        cleaned_content = '\n&emsp;'.join(stripped_content)

        # TODO Refine the style used for displaying normal text blocks.
        st.markdown(
            f"""
            <div style="
                background-color: #fdf6e3;
                border: 1px solid #dcd3b8;
                border-left: 10px solid #8b4513;
                padding: 20px;
                font-family: 'Georgia', serif;
                color: #2c2420;
                line-height: 1.6;
                box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
                border-radius: 2px;
                margin-bottom: 20px;">
                {cleaned_content}
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    TextModel(["This scenario takes place in the undead nation of Geb on the east coast of Garund in the Inner Sea. The PCs travel to the nation’s capital of Mechitar. To learn more about Mechitar, see Lost Omens: Impossible Lands pages 141–157"]).render()