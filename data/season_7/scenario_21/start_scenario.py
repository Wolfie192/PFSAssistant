import streamlit as st

from pathlib import Path
from src import Directory


def start_scenario():
    if "tier_min" not in st.session_state:
        st.session_state["tier_min"] = 5
    if "tier_max" not in st.session_state:
        st.session_state["tier_max"] = 6

    scenario = {
        "The Home of Empty Breath": [
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "roster.py"), title="Character Roster"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "where_on_golarion.py"), title="Where on Golarion?"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "adventure_background.py"), title="Adventure Background"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "getting_started.py"), title="Getting Started"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "anaphexia.py"), title="The Anaphexia"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "zoroqs_villa.py"), title="Zoroq's Villa")
        ],
        "Zoroq's Villa Ground Floor": [
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "villa_ground_floor_map.py"), title="A. Villa Ground Floor"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a1_entry_hall.py"), title="A1. Entry Hall"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a2_magical_study.py"), title="A2. Magical Study (Low)"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a3_sitting_room.py"), title="A3. Sitting Room"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a4_grand_stair.py"), title="A4. Grand Stair"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a5_kitchen.py"), title="A5. Kitchen"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a6_banquet_hall.py"), title="A6. Banquet Hall"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_ground_floor", "a7_greenhouse.py"), title="A7. Greenhouse (Trivial)")
            ],
        "Zoroq's Villa Upper Floor":[
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "villa_upper_floor_map.py"), title="B. Villa Upper Floor"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b1_laboratory.py"), title="B1. Laboratory (Trivial)"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b2_storage.py"), title="B2. Storage"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b3_statuary_room.py"), title="B3. Statuary Room"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b4_library.py"), title="B4. Library"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b5_antechamber.py"), title="B5. Antechamber (Moderate)"),
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "zoroq's_villa", "villa_upper_floor", "b6_study.py"), title="B6. Study")
        ],
        "Conclusion": [
            st.Page(Path.joinpath(Directory.scenario_pages_dir(), "conclusion.py"), title="Conclusion")
        ]
    }

    st.navigation(scenario).run()


if __name__ == "__main__":
    start_scenario()