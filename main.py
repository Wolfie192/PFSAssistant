import streamlit as st

from pathlib import Path

from src import Scenarios, Directory


def main():
    st.set_page_config(page_title="PFS Society", layout="wide")

    if "selected_season" not in st.session_state:
        st.session_state["selected_season"] = None
    if "selected_scenario" not in st.session_state:
        st.session_state["selected_scenario"] = None

    if st.session_state.selected_season and st.session_state.selected_scenario:
        st.navigation([Path.joinpath(Directory.scenario_dir(), "start_scenario.py")]).run()

    else:
        available_seasons = []
        for season in list(Scenarios.scenarios.keys()):
            available_seasons.append(season)

        season = st.selectbox("Season", available_seasons)

        try:
            available_scenarios = Scenarios.scenarios[season].get("scenarios", [])
        except KeyError:
            available_scenarios = []

        scenario = st.selectbox("Scenario", available_scenarios)


        if season and scenario:
            if st.button("Select Scenario"):
                st.session_state["selected_season"] = season
                st.session_state["selected_scenario"] = scenario
                st.rerun()
        else:
            st.button("Select Scenario", disabled=True)


if __name__ == "__main__":
    main()