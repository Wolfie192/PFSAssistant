import streamlit as st

from src.Text import text
import src.Investigation.Widgets as Widgets


def investigation(skills: list[dict], sid: str,
                  desc: str|list[str]|None = None,
                  crit_success_text: str|None = None, success_text: str|None = None,
                  failure_text: str|None = None, crit_failure_text: str|None = None,
                  result_text: str|None = None, breakpoints: list[int]|None = None):
    with st.expander("Investigation", expanded=True):
        if sid not in st.session_state:
            st.session_state[sid] = 1
        if desc:
            if isinstance(desc, str):
                text(desc)
            elif isinstance(desc, list):
                for paragraph in desc:
                    text(paragraph)

        with st.container(border=True):
            headers = st.columns(7)
            headers[0].caption("Name")
            headers[1].caption("Skill")
            headers[2].caption("DC")
            headers[3].caption("Roll")
            headers[4].caption("Nat 20")
            headers[5].caption("Nat 1")
            headers[6].caption("Result")

            for idx in range(int(st.session_state.get(f"{sid}", 1))):
                with st.container():
                    cols = st.columns(7)
                    with cols[0]:
                        options = list(c["name"] for c in st.session_state["characters"])
                        Widgets.name(idx, options, sid)

                    with cols[1]:
                        options = list(s["name"] for s in skills)
                        Widgets.skill(idx, options, sid)

                    with cols[2]:
                        Widgets.dc(idx, skills, sid)

                    with cols[3]:
                        Widgets.roll(idx, sid)

                    with cols[4]:
                        Widgets.nat_20(idx, sid)

                    with cols[5]:
                        Widgets.nat_1(idx, sid)

                    with cols[6]:
                        Widgets.result(idx, skills, sid)
        results = st.columns(7)

        with results[0]:
            Widgets.add_check(sid)

        with results[5]:
            text("**Total Investigation Points:**")

        with results[6]:
            Widgets.total_investigation_points(sid, breakpoints)

        if result_text:
            text(result_text)