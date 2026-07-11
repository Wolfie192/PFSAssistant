import streamlit as st

from src.Page import page


def start_scenario():
    if "tier_min" not in st.session_state:
        st.session_state["tier_min"] = 1
    if "tier_max" not in st.session_state:
        st.session_state["tier_max"] = 4

    scenario = {
        "Shipyard Sabotage": [
            page("Roster"),
            page("Where on Golarion?"),
            page("Adventure Background"),
            page("Getting Started"),
            page("Touring the Shipyards")
        ],
        "A. Battle for the Docks": [
            page("A. Battle for the Docks"),
            page("Dock Defense"),
            page("Wave 1: Gorilla Warfare (Moderate)"),
            page("Between the Waves")
        ]
    }

    st.navigation(scenario).run()


if __name__ == "__main__":
    start_scenario()