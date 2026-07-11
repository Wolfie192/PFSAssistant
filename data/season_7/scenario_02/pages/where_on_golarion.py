import streamlit as st

from src.ImageModel import Image
from src.TextModel import Text


def where_on_golarion():
    cols = st.columns(2)

    with cols[0]:
        Text([
            "*Shipyard Sabotage* takes place in the shipyards of Augustana, Andoran’s second largest city. It is located on the Apso Bay and boasts one of the largest shipyards on the Inner Sea. For more on Augustana and Andoran, see pages 30-43 of the Pathfinder Lost Omens Shining Kingdoms."
        ])

    with cols[1]:
        Image("Area Map")


if __name__ == "__main__":
    where_on_golarion()