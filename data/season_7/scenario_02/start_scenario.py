import streamlit as st

from src.Page import page


def start_scenario():
    if "tier_min" not in st.session_state:
        st.session_state["tier_min"] = 1
    if "tier_max" not in st.session_state:
        st.session_state["tier_max"] = 4

    scenario = {
        "Shipyard Sabotage": [
            page("Roster", "roster.py"),
            page("Where on Golarion?", "where_on_golarion.py"),
            page("Adventure Background", "adventure_background.py"),
            page("Getting Started", "getting_started.py"),
            page("Touring the Shipyards", "touring_the_shipyards.py")
        ],
        "A. Battle for the Docks": [
            page("Map", "battle_for_the_docks_map.py"),
            page("A. Battle for the Docks", "battle_for_the_docks.py"),
            page("Dock Defense", "dock_defense.py"),
            page("Wave 1: Gorilla Warfare (Moderate)", "gorilla_warfare.py"),
            page("Between the Waves", "between_the_waves.py")
        ]
    }

    st.navigation(scenario).run()


if __name__ == "__main__":
    start_scenario()