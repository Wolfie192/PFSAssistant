import streamlit as st
import html
import base64

from pathlib import Path


class InfoBoxModel:
    """
    Model for displaying markdown formatted text and
    images within a formatted info box.
    """
    def __init__(self, content: list):
        self.content = content


    def _get_image_base64(self, file_path: Path):
        """
        Converts a local image/svg file to a base64 string.
        """
        if not file_path.exists():
            return None

        ext = file_path.suffix.lower()
        mime_type = "image/svg+xml" if ext == ".svg" else f"image/{ext.replace(".", "")}"

        with open(file_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:{mime_type};base64,{data}"


    def render(self):
        if not self.content:
            st.info("Empty read aloud module.")
            return

        inner_html = ""
        is_first_paragraph = True

        for item in self.content:
            if isinstance(item, str):
                escaped_text = html.escape(item.strip())
                klass = "" if is_first_paragraph else "indented"
                inner_html += f'<p class="{klass}">{escaped_text}</p>'
                is_first_paragraph = False

            elif isinstance(item, dict) and "image" in item:
                img_data = self._get_image_base64(item["image"])
                if img_data:
                    inner_html += f'<img src="{img_data}">'

        st.markdown(
            f"""
            <style>
                .custom-box {{
                    color: #2c2420;
                    font-size: 1.1em;
                    background-color: #fdf6e3;
                    border-left: 5px solid #8b4513;
                    padding: 10px;
                    overflow-wrap: break-word;
                    border-radius: 10px;
                }}
                .custom-box p {{
                    margin: 0;
                    padding-bottom: 5px;
                    line-height: 1.4;
                }}
                .custom-box .indented {{
                    text-indent: 2em;
                }}
                .custom-box img {{
                    display: block;
                    max-width: 100%;
                    height: auto;
                }}
            </style>
            <div class="custom-box">
                {inner_html}
            </div>
            """,
            unsafe_allow_html=True
        )