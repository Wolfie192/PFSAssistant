import streamlit as st
import copy

from src.Roster import Widgets
from src.Skills.SkillChecks import Skills


def calc_tier():
    cp = 0
    for idx, char in enumerate(st.session_state["characters"]):
        cp += char["challenge points"]

    match cp:
        case c if c >= 19: st.session_state["tier"] = "high"
        case c if c >= 16 and len(st.session_state["characters"]) <= 4: st.session_state["tier"] = "high"
        case _: st.session_state["tier"] = "low"


def roster():
    blank_char = {
                "name": "", "level": st.session_state["tier_min"], "challenge points": 2, "perception": 0,
                "skills": {s: 0 for s in [Skills.RELIGION.value, Skills.DEMON_LORE.value]}
    }

    if "characters" not in st.session_state:
        st.session_state["characters"] = [copy.deepcopy(blank_char) for _ in range(2)]
    if "min_level" not in st.session_state:
        st.session_state["min_level"] = st.session_state["tier_min"]

    for c_idx, character in enumerate(st.session_state["characters"]):
        with st.container(border=True):
            row_1 = st.columns(4)

            with row_1[0]:
                Widgets.name(character, c_idx)

            with row_1[1]:
                Widgets.level(character, c_idx)

            with row_1[2]:
                Widgets.challenge_points(character, c_idx)

            with row_1[3]:
                Widgets.perception(character, c_idx)

            cols_per_row = 9
            skill_items = list(character["skills"].items())

            for i in range(0, len(skill_items), cols_per_row):
                row = st.columns(cols_per_row)
                for j, (skill, modifier) in enumerate(skill_items[i: i+ cols_per_row]):
                    with row[j]:
                        Widgets.skill(skill, modifier, c_idx)

    cols = st.columns([0.2, 0.7, 0.1])

    if len(st.session_state["characters"]) < 6:
        with cols[0]:
            Widgets.add_character(blank_char)

    calc_tier()