import streamlit as st


class RosterModel:
    @staticmethod
    def render():
        state = st.session_state.scenario_state

        headers = st.columns([0.7, 0.1, 0.1, 0.1])
        headers[0].caption("Character Name")
        headers[1].caption("Level")
        headers[2].caption("CP")
        headers[3].write("")

        for i, character in enumerate(state["characters"]):
            cols = st.columns([0.7, 0.1, 0.1, 0.1])

            name = cols[0].text_input(
                "Name",
                value=character.get("name", ""),
                key=f"name_{i}",
                label_visibility="collapsed"
            )
            level = cols[1].number_input(
                "Level",
                value=int(character.get("level", state["tier_min"])),
                min_value=state["tier_min"],
                max_value=state["tier_max"],
                key=f"level_{i}",
                label_visibility="collapsed"
            )

            state["characters"][i] = {"name": name, "level": level}

            diff = level - state["tier_min"]
            cp = {0: 2, 1: 3, 2: 4, 3: 6}.get(diff, 0)
            cols[2].markdown(f"**{cp}**")

            if cols[3].button("", icon=":material/delete:", key=f"del_{i}"):
                state["characters"].pop(i)
                st.rerun()

        if len(state["characters"]) < 6:
            if st.button("Add Characters", icon=":material/add:"):
                state["characters"].append({"name": "", "level": state["tier_min"]})
                st.rerun()