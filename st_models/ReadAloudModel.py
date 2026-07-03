import re
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

        stripped_content = []
        for content in self.content:
            stripped_content.append(content.strip())

        cleaned_content = '\n&emsp;'.join(stripped_content)

        st.markdown(
            f"""
            <div style="
                color: #1b5e20;
                background-color: #f1f8e9;
                border-left: 5px solid #2e7d32;
                padding: 5px 10px 0px 10px;
                font-size: 1.1em;
                font-style: italic;
                white-space: pre-wrap;
                border-radius: 4px;
                margin-bottom: 0px;">
                {cleaned_content}
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    ReadAloudModel([
        "The great black pyramid of the Cinerarium looms solemnly over Geb’s capital city of Mechitar. While an entire nation of the undead can seem grim and joyless to the living, Mechitar is not without its grandiose displays of color. Large banners and tapestries denoting houses of the ruling Blood Lords stand on the city walls and along the entrance to the great pyramid. Colorful canvas stretching from rooftop to rooftop shades the streets and the undead inhabitants performing their duties around the city.",
        "The Pathfinder Society has arranged an audience with a minor Blood Lord, a lich named Msasa Kuatuz. Two heavily armed and armored zombies provide an escort to Msasa’s office. The lich’s large office is grandly decorated with rich tapestries of green and gold, with insect motifs on every wall. Lit censers stand in each corner, a benefit more for the living who might find the ever-present odor of rot unpleasant.",
        "Msasa’s true age is impossible to guess, but her weathered skin and deep eyes hint at immense experience. Similarly ancient-looking texts cover the desk in her chambers, likely denoting extensive research and planning.",
        "Msasa stands from behind her desk and dismisses the zombie escorts. With practiced ease, she steps to the front of her desk, concealing her work from curious eyes."
    ]).render()