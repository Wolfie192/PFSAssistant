import streamlit as st
import html


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
                color: #1b5e20;
                font-size: 1.1em;
                font-style: italic;
                background-color: #f1f8e9;
                border-left: 5px solid #2e7d32;
                padding: 10px;
                overflow-wrap: break-word;
                border-radius: 10px;">
                {paragraphs}
            </div>
            """,
            unsafe_allow_html=True
        )