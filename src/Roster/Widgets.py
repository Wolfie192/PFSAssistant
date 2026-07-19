import streamlit as st
import copy


def update_character(c_idx, key, value):
    st.session_state["characters"][c_idx][key] = value

    if key == "level":
        min_level = st.session_state["min_level"]

        cp_map = {min_level: 2, min_level + 1: 3, min_level + 2: 4, min_level + 3: 6}
        st.session_state["characters"][c_idx]["challenge points"]= cp_map.get(value, 2)
        st.session_state[f"char_{c_idx}_challenge_points"] = cp_map.get(value, 2)


def update_skill(c_idx, skill_name, value):
    st.session_state["characters"][c_idx]["skills"][skill_name] = value


def name(char: dict, idx: int):
    st.text_input(
        label="Character Name", value=char["name"],
        key=f"char_{idx}_name",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(l_idx, "name", st.session_state[f"char_{l_idx}_name"])
    )


def level(char: dict, idx: int):
    st.number_input(
        label="Level", value=char["level"],
        min_value=st.session_state["tier_min"], max_value=st.session_state["tier_max"],
        key=f"char_{idx}_level",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(l_idx, "level", st.session_state[f"char_{l_idx}_level"])
    )


def challenge_points(char: dict, idx: int):
    st.number_input(
        label="Challenge Points", value=char["challenge points"],
        min_value=2, max_value=6,
        disabled=True,
        persist_state="session",
        key=f"char_{idx}_challenge_points"
    )


def perception(char: dict, idx: int):
    st.number_input(
        label="Perception", value=char["perception"],
        key=f"char_{idx}_perception",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(l_idx, "perception",st.session_state[f"char_{l_idx}_perception"]))


def skill(skill, modifier, idx: int):
    st.number_input(
        label=skill,
        value=modifier,
        key=f"char_{idx}_{skill}",
        persist_state="session",
        on_change=lambda l_idx=idx, s=skill: update_skill(l_idx, s, st.session_state[f"char_{l_idx}_{s}"])
    )


def add_character(blank_char: dict):
    if st.button("Add Characters", icon=":material/add:"):
        st.session_state["characters"].append(copy.deepcopy(blank_char))
        st.rerun()