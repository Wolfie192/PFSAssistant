import streamlit as st
import html


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

        cleaned_segments = [html.escape(c.strip()) for c in self.content]

        paragraphs = "".join([f"<p>{s}</p>" for s in cleaned_segments])

        st.markdown(
            f"""
            <style>
                .custom-box p {{
                    margin: 0;
                    padding-bottom: 5px;
                    line-height: 1.4;
                }}
                .custom-box p:not(:first-child) {{
                    text-indent: 2em;
                }}
                .custom-box p:first-child {{
                    text-indent: 0;
                }}
            </style>
            <div class="custom-box" style="
                font-size: 1.1em;
                padding: 10px;
                overflow-wrap: break-word;
                border-radius: 10px;">
                {paragraphs}
            </div>
            """,
            unsafe_allow_html=True
        )