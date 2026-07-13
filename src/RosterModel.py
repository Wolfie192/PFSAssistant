import streamlit as st
import uuid

from src.DataManager import DataManager


class Roster:
    def __init__(self):
        self.manager = DataManager()

        if "characters" not in st.session_state:
            all_data = self.manager.load_data()
            st.session_state["characters"] = all_data.get("characters", [])

        self.render()


    def _save(self):
        all_data = self.manager.load_data()
        all_data["characters"] = st.session_state["characters"]
        self.manager.save_data(all_data)


    @staticmethod
    def _calc_cp(level: int):
        diff = level - st.session_state["tier_min"]
        return {0: 2, 1: 3, 2: 4, 3: 6}.get(diff, 0)


    def _update_tier(self):
        total_cp = sum(self._calc_cp(char.get("level", st.session_state["tier_min"])) for char in st.session_state["characters"])
        st.session_state["cp"] = total_cp

        if total_cp <= 14:
            st.session_state["tier"] = "low"
        elif total_cp >= 19:
            st.session_state["tier"] = "high"
        elif total_cp <= 18 and len(st.session_state["characters"]) >= 5:
            st.session_state["tier"] = "low"
        else:
            st.session_state["tier"] = "high"


    def _update_name_callback(self, idx, char_id):
        st.session_state["characters"][idx]["name"] = st.session_state[f"roster_{char_id}_name"]
        self._save()


    def _update_level_callback(self, idx, char_id):
        st.session_state["characters"][idx]["level"] = st.session_state[f"roster_{char_id}_level"]
        self._save()


    def render(self):
        headers = st.columns([0.75, 0.1, 0.1, 0.05])
        headers[0].caption("Character")
        headers[1].caption("Level")
        headers[2].caption("CP")
        headers[3].caption("")

        for i, char in enumerate(st.session_state["characters"]):
            char_id = char.get("id")

            cols = st.columns([0.75, 0.1, 0.1, 0.05])

            st.session_state["characters"][i]["name"] = cols[0].text_input(
                "Name",
                value=char.get("name", ""),
                on_change=self._update_name_callback,
                args=(i, char_id,),
                label_visibility="collapsed",
                key=f"roster_{char_id}_name"
            )

            st.session_state["characters"][i]["level"] = cols[1].number_input(
                "Level",
                value=char.get("level", st.session_state["tier_min"]),
                min_value=st.session_state.get("tier_min", 1),
                max_value=st.session_state.get("tier_max", 20),
                on_change=self._update_level_callback,
                args=(i, char_id,),
                label_visibility="collapsed",
                key=f"roster_{char_id}_level"
            )

            cp = self._calc_cp(st.session_state["characters"][i]["level"])
            cols[2].markdown(f"##### {cp}")

            if cols[3].button("", icon=":material/delete:", key=f"roster_{char_id}_del"):
                st.session_state["characters"].pop(i)
                self._save()
                st.rerun()

        self._update_tier()

        cols = st.columns([0.2, 0.7, 0.1])

        if len(st.session_state["characters"]) < 6:
            if cols[0].button("Add Characters", icon=":material/add:"):
                st.session_state["characters"].append(
                    {
                        "id": str(uuid.uuid4()),
                        "name": None,
                        "level": st.session_state["tier_min"]
                    }
                )
                self._save()
                st.rerun()

        if cols[2].button("Reset", icon=":material/delete:", key="reset_button"):
            season = st.session_state.get("season")
            scenario = st.session_state.get("scenario")
            st.session_state.clear()
            st.session_state["season"] = season
            st.session_state["scenario"] = scenario
            self.manager.save_data({})
            st.rerun()