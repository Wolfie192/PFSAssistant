import streamlit as st

from pathlib import Path

from src import Directory
from util import Scenarios


def main():
    st.set_page_config(page_title="PFS Society", layout="wide")

    if "season" not in st.session_state:
        st.session_state["season"] = None
    if "scenario" not in st.session_state:
        st.session_state["scenario"] = None

    if st.session_state.season and st.session_state.scenario:
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
                st.session_state["season"] = season
                st.session_state["scenario"] = scenario
                st.rerun()
        else:
            st.button("Select Scenario", disabled=True)


if __name__ == "__main__":
    main()