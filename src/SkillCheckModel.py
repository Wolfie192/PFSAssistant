import uuid
import random
import streamlit as st

from src.DataManager import DataManager

from src.SkillModel import Skill


class SkillCheck:
    def __init__(self, name: str, skills: list[Skill]):
        self.name = name
        self.skills = skills
        self.manager = DataManager()

        if f"{self.name}_id" not in st.session_state:
            st.session_state[f"{self.name}_id"] = str(uuid.uuid4())

        self.id = st.session_state[f"{self.name}_id"]

        if self.id not in st.session_state:
            all_data = self.manager.load_data()
            st.session_state[self.id] = all_data.get(self.id, {})

        for char in st.session_state["characters"]:
            char_id = char.get("id")

            if char_id not in st.session_state[self.id]:
                st.session_state[self.id][char_id] = {
                    "skill": None,
                    "modifier": 0,
                    "roll": random.randint(1, 20)
                }

        self.render()


    def _save(self):
        all_data = self.manager.load_data()
        all_data[self.id] = st.session_state.get(self.id)
        self.manager.save_data(all_data)


    @staticmethod
    def _get_degree_of_success(roll: int, modifier: int, dc: int):
        total = roll + modifier
        diff = total - dc

        if diff >= 10: result = 3
        elif diff >= 0: result = 2
        elif diff > -10: result = 1
        else: result = 0

        if roll == 20: result = min(result + 1, 3)
        if roll == 1: result = max(result - 1, 0)

        return {
            0: ":red[Crit Fail]",
            1: ":orange[Fail]",
            2: ":green[Success]",
            3: ":blue[Crit Success]"
        }.get(result)


    def _update_skill_callback(self, char_id):
        st.session_state[self.id][char_id]["skill"] = st.session_state[f"{self.id}_{char_id}_skill"]
        self._save()


    def _update_mod_callback(self, char_id):
        st.session_state[self.id][char_id]["modifier"] = st.session_state[f"{self.id}_{char_id}_modifier"]
        self._save()


    def render(self):
        with st.expander(self.name):
            headers = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])
            headers[0].caption("Character")
            headers[1].caption("Skill")
            headers[2].caption("Modifier")
            headers[3].caption("Result")
            headers[4].caption("Reroll")

            for char in st.session_state["characters"]:
                char_id = char.get("id")

                cols = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])

                cols[0].markdown(char.get("name"))

                current_skill = st.session_state[self.id][char_id].get("skill")
                options = [s.name for s in self.skills]
                idx = options.index(current_skill) if current_skill in options else None

                skill_val = cols[1].selectbox(
                    "Skill",
                    options=options,
                    index=idx,
                    on_change=self._update_skill_callback,
                    args=(char_id,),
                    label_visibility="collapsed",
                    key=f"{self.id}_{char_id}_skill"
                )

                cols[2].number_input(
                    "Modifier",
                    value=st.session_state[self.id][char_id].get("modifier", 0),
                    step=1,
                    on_change=self._update_mod_callback,
                    args=(char_id,),
                    label_visibility="collapsed",
                    key=f"{self.id}_{char_id}_modifier"
                )

                skill_obj = next((s for s in self.skills if s.name == st.session_state[self.id][char_id]["skill"]), None)

                if skill_obj:
                    current_roll = st.session_state[self.id][char_id].get("roll")
                    current_modifier = st.session_state[self.id][char_id].get("modifier")

                    dc = skill_obj.high_dc if st.session_state["tier"] == "High" else skill_obj.low_dc
                    result = self._get_degree_of_success(current_roll, current_modifier, dc)
                    cols[3].markdown(result)
                else:
                    cols[3].markdown("--")

                if cols[4].button("Reroll", icon=":material/casino:", key=f"{self.id}_{char_id}_reroll"):
                    st.session_state[self.id][char_id]["roll"] = random.randint(1, 20)
                    self._save()
                    st.rerun()