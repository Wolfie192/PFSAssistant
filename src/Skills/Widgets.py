import streamlit as st
import random


def calculate_check_result(char: dict, skills: list[dict], sid: str):
    if st.session_state[f"{sid}_{char.get("name")}_skill"] is None:
        return None

    roll = st.session_state[f"{sid}_{char.get("name")}_roll"]

    skill_key = f"{sid}_{char.get("name")}_skill"
    target_name = st.session_state[skill_key]
    selected_skill = next((s for s in skills if s["name"].value == target_name), None)
    dc = int(calculate_dc(selected_skill))

    diff = roll - dc

    if diff >= 10: result = 3
    elif diff >= 0: result = 2
    elif diff > -10: result = 1
    else: result = 0

    nat_20 = st.session_state[f"{sid}_{char.get("name")}_nat_20"]
    nat_1 = st.session_state[f"{sid}_{char.get("name")}_nat_1"]
    if nat_20: result = min(result + 1, 3)
    if nat_1: result = max(result - 1, 0)

    if selected_skill["auto_success"]:
        return "Success"
    elif selected_skill["auto_crit_success"]:
        return "Critical Success"
    else:
        return {
            0: "Critical Failure",
            1: "Failure",
            2: "Success",
            3: "Critical Success"
        }.get(result)


def calculate_secret_check_result(char: dict, skills: list[dict], sid: str):
    if st.session_state[f"{sid}_{char.get("name")}_skill"] is None:
        return None

    if st.session_state[f"{sid}_{char.get("name")}_modifier"] is None:
        return None

    modifier = st.session_state[f"{sid}_{char.get("name")}_modifier"]
    roll = st.session_state[f"{sid}_{char.get("name")}_roll"]

    skill_key = f"{sid}_{char.get("name")}_skill"
    target_name = st.session_state[skill_key]
    selected_skill = next((s for s in skills if s["name"] == target_name), None)
    dc = int(calculate_dc(selected_skill))

    total = modifier + roll
    diff = total - dc

    if diff >= 10: result = 3
    elif diff >= 0: result = 2
    elif diff > -10: result = 1
    else: result = 0

    if roll == 20: result = min(result + 1, 3)
    if roll == 1: result = max(result - 1, 0)

    return {
        0: "Critical Failure",
        1: "Failure",
        2: "Success",
        3: "Critical Success"
    }.get(result)


def format_result(result: str):
    match result:
        case "Critical Success": return f"**:blue[Critical Success]**"
        case "Success": return f"**:green[Success]**"
        case "Failure": return f"**:orange[Failure]**"
        case "Critical Failure": return f"**:red[Critical Failure]**"
        case _: return f"**None**"


def calculate_dc(selected_skill: dict|None):
    if selected_skill is None: return None

    tier = st.session_state["tier"]
    if tier == "high":
        return selected_skill.get("high")
    elif tier == "low":
        return selected_skill.get("low")
    else: return None


def format_dc(dc):
    if st.session_state["tier"] == "low":
        return f"**{dc} (low)**"
    else:
        return f"**{dc} (high)**"


def name(name: str):
    st.markdown(f"**{name}**")


def skill(char: dict, options: list, sid: str):
    st.selectbox(
        label="Skill",
        label_visibility="collapsed",
        index=None,
        options=options,
        persist_state="session",
        key=f"{sid}_{char.get("name")}_skill"
    )


def dc(char: dict, skills: list[dict], sid: str):
    skill_key = f"{sid}_{char.get("name")}_skill"
    target_name = st.session_state[skill_key]
    selected_skill = next((s for s in skills if s["name"] == target_name), None)

    dc = calculate_dc(selected_skill)
    st.markdown(format_dc(dc))


def modifier(char:dict, sid: str):
    skill_key = f"{sid}_{char.get("name")}_skill"
    selected_skill = st.session_state[skill_key]
    modifier = char["skills"].get(selected_skill, None)
    st.session_state[f"{sid}_{char.get("name")}_modifier"] = modifier

    st.number_input(
        label="Modifier",
        label_visibility="collapsed",
        step=1,
        persist_state="session",
        key=f"{sid}_{char.get("name")}_modifier"
    )


def roll(char: dict, sid: str):
    st.number_input(
        label="Roll",
        label_visibility="collapsed",
        value=random.randint(1, 20),
        step=1,
        persist_state="session",
        key=f"{sid}_{char.get("name")}_roll"
    )


def nat_20(char: dict, sid: str):
    if st.session_state[f"{sid}_{char.get("name")}_nat_1"]:
        st.checkbox(
            label="Nat 20",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            disabled=True,
            key=f"{sid}_{char.get("name")}_nat_20"
        )
    else:
        st.checkbox(
            label="Nat 20",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            key=f"{sid}_{char.get("name")}_nat_20"
        )


def nat_1(char: dict, sid: str):
    if st.session_state[f"{sid}_{char.get("name")}_nat_20"]:
        st.checkbox(
            label="Nat 1",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            disabled=True,
            key=f"{sid}_{char.get("name")}_nat_1"
        )
    else:
        st.checkbox(
            label="Nat 1",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            key=f"{sid}_{char.get("name")}_nat_1"
        )


def result(char: dict, skills: list[dict], sid: str):
    res = calculate_check_result(char, skills, sid)
    st.markdown(format_result(res))


def secret_result(char: dict, skills: list[dict], sid: str):
    res = calculate_secret_check_result(char, skills, sid)
    st.markdown(format_result(res))


