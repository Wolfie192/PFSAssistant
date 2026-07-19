import streamlit as st
import random


def calculate_check_result(idx: int, skills: list[dict], sid: str):
    if st.session_state[f"{sid}_{idx}_name"] is None:
        return None
    if st.session_state[f"{sid}_{idx}_skill"] is None:
        return None

    roll = st.session_state[f"{sid}_{idx}_roll"]

    skill_key = f"{sid}_{idx}_skill"
    target_name = st.session_state[skill_key]
    selected_skill = next((s for s in skills if s["name"] == target_name), None)
    dc = int(calculate_dc(selected_skill))

    diff = roll - dc

    if diff >= 10: result = 3
    elif diff >= 0: result = 2
    elif diff > -10: result = 1
    else: result = 0

    nat_20 = st.session_state[f"{sid}_{idx}_nat_20"]
    nat_1 = st.session_state[f"{sid}_{idx}_nat_1"]
    if nat_20: result = min(result + 1, 3)
    if nat_1: result = max(result - 1, 0)

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


def name(idx: int, options: list, sid: str):
    st.selectbox(
        label="Name",
        label_visibility="collapsed",
        index=None,
        options=options,
        persist_state="session",
        key=f"{sid}_{idx}_name"
    )


def skill(idx: int, options: list, sid: str):
    st.selectbox(
        label="Skill",
        label_visibility="collapsed",
        options=options,
        index=None,
        persist_state="session",
        key=f"{sid}_{idx}_skill"
    )


def dc(idx: int, skills: list[dict], sid: str):
    skill_key = f"{sid}_{idx}_skill"
    target_name = st.session_state[skill_key]
    selected_skill = next((s for s in skills if s["name"] == target_name), None)

    dc = calculate_dc(selected_skill)
    st.markdown(format_dc(dc))


def roll(idx: int, sid: str):
    st.number_input(
        label="Roll",
        label_visibility="collapsed",
        value=random.randint(1, 20),
        step=1,
        persist_state="session",
        key=f"{sid}_{idx}_roll"
    )


def nat_20(idx: int, sid: str):
    if f"{sid}_{idx}_nat_1" not in st.session_state:
        st.session_state[f"{sid}_{idx}_nat_1"] = False

    if st.session_state[f"{sid}_{idx}_nat_1"]:
        st.checkbox(
            label="Nat 20",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            disabled=True,
            key=f"{sid}_{idx}_nat_20"
        )
    else:
        st.checkbox(
            label="Nat 20",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            key=f"{sid}_{idx}_nat_20"
        )


def nat_1(idx: int, sid: str):
    if st.session_state[f"{sid}_{idx}_nat_20"]:
        st.checkbox(
            label="Nat 1",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            disabled=True,
            key=f"{sid}_{idx}_nat_1"
        )
    else:
        st.checkbox(
            label="Nat 1",
            label_visibility="collapsed",
            value=False,
            persist_state="session",
            key=f"{sid}_{idx}_nat_1"
        )


def result(idx: int, skills: list[dict], sid: str):
    res = calculate_check_result(idx, skills, sid)

    if f"{sid}_{idx}_result" not in st.session_state:
        st.session_state[f"{sid}_{idx}_result"] = None
    else:
        st.session_state[f"{sid}_{idx}_result"] = res
    st.markdown(format_result(res))


def add_check(sid: str):
    if st.button("Add Check", icon=":material/add:", width="stretch"):
        st.session_state[sid] += 1
        st.rerun()


def total_investigation_points(sid: str, breakpoints: list[int]):
    inv_points = 0
    for idx in range(st.session_state[sid]):
        match st.session_state[f"{sid}_{idx}_result"]:
            case "Critical Success": inv_points += 2
            case "Success": inv_points += 1
            case "Critical Failure": inv_points = max(inv_points - 1, 0)

    if breakpoints:
        if inv_points < breakpoints[0]:
            st.markdown(f"**:red[{inv_points}]**")
        elif len(breakpoints) > 1 and inv_points < breakpoints[1]:
            st.markdown(f"**:orange[{inv_points}]**")
        elif len(breakpoints) > 2 and inv_points < breakpoints[2]:
            st.markdown(f"**:yellow[{inv_points}]**")
        elif len(breakpoints) > 3 and inv_points < breakpoints[3]:
            st.markdown(f"**:violet[{inv_points}]**")
        elif len(breakpoints) > 4 and inv_points < breakpoints[4]:
            st.markdown(f"**:blue[{inv_points}]**")
        else:
            st.markdown(f"**:green[{inv_points}]**")
    else:
        st.markdown(f"**:green[{inv_points}]**")