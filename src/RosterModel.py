import streamlit as st

from src.DataManager import DataManager


class RosterModel:
    def __init__(self):
        self.id = "roster"
        self.manager = DataManager()

        if "characters" not in st.session_state:
            saved_data = self.manager.load_data()
            st.session_state["characters"] = saved_data.get("characters", [])

        self.render()


    def _save(self):
        for i in range(len(st.session_state["characters"])):
            st.session_state["characters"][i]["name"] = st.session_state.get(f"name_{i}", "")
            st.session_state["characters"][i]["level"] = st.session_state.get(f"level_{i}", st.session_state.get("tier_min", 1))

        all_data = self.manager.load_data()
        all_data["characters"] = st.session_state["characters"]
        self.manager.save_data(all_data)


    def render(self):
        def update_char():
            self._save()

        headers = st.columns([0.85, 0.05, 0.05, 0.05])
        headers[0].caption("Character Name")
        headers[1].caption("Level")
        headers[2].caption("CP")
        headers[3].write("")

        delete_index = None

        for i, character in enumerate(st.session_state["characters"]):
            with st.container(border=True):
                cols = st.columns([0.85, 0.05, 0.05, 0.05])

                st.session_state["characters"][i]["name"] = cols[0].text_input(
                    "Name",
                    value=character.get("name", ""),
                    key=f"name_{i}",
                    on_change=update_char,
                    label_visibility="collapsed"
                )

                st.session_state["characters"][i]["level"] = cols[1].number_input(
                    "Level",
                    value=character.get("level", st.session_state.get("tier_min", 1)),
                    min_value=st.session_state.get("tier_min", 1),
                    max_value=st.session_state.get("tier_max", 20),
                    key=f"level_{i}",
                    on_change=update_char,
                    label_visibility="collapsed"
                )

                diff = st.session_state["characters"][i]["level"] - st.session_state["tier_min"]
                cp = {0: 2, 1: 3, 2: 4, 3: 6}.get(diff, 0)
                cols[2].markdown(f"**{cp}**")

                if cols[3].button("", icon=":material/delete:", key=f"del_{i}"):
                    delete_index = i

        if delete_index is not None:
            st.session_state["characters"].pop(delete_index)
            self._save()
            st.rerun()

        cols = st.columns([0.2, 0.7, 0.1])

        if len(st.session_state["characters"]) < 6:
            if cols[0].button("Add Characters", icon=":material/add:"):
                st.session_state["characters"].append({"name": "", "level": st.session_state["tier_min"]})
                self._save()
                st.rerun()

        if cols[2].button("Reset", icon=":material/delete:", key="reset_button"):
            st.session_state.clear()
            self.manager.save_data({})
            st.rerun()