import streamlit as st

from src.DataManager import DataManager
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.VariableModel import VariableModel


def between_the_waves():
    ReadAloudModel([
        "Fires smolder all over the shipyard, and frantic workers scramble to douse the remaining flames. Meanwhile, sounds of pirate mayhem and fighting grow ever closer. The next wave of pirates is already approaching, but there’s a brief opportunity to put out some of the fire before they arrive."
    ])

    TextModel([
        "After the last of the pirate goblins and gorillas die or are captured, the PCs have one minute before the next wave of pirates arrives. During that time, allow each PC to do a single “Save the Shipyard!” check to represent them putting out fires and getting workers to safety."
    ])

    if "shipyard_successes" not in st.session_state:
        st.session_state["shipyard_successes"] = 0

    VariableModel("Shipyard Successes")


if __name__ == "__main__":
    between_the_waves()