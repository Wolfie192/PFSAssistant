import streamlit as st

from pathlib import Path

from src import Directory
from src.ImageModel import ImageModel
from src.TextModel import TextModel


def where_on_golarion():
    cols = st.columns([0.25, 0.75])

    with cols[0]:
        TextModel([
            "This scenario takes place in the undead nation of Geb on the east coast of Garund in the Inner Sea The PCs travel to the nation’s capital of Mechitar To learn more about Mechitar, see Lost Omens: Impossible Lands pages 141–157."
        ])

    with cols[1]:
        ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Area Map.svg"))


if __name__ == "__main__":
    where_on_golarion()