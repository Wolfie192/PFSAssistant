import random

import streamlit as st

from src.DataManager import DataManager

from src.SkillModel import SkillModel



class SkillCheckModel:
    def __init__(self, name: str, skills: list[SkillModel], model_id: str):
        self.name = name
        self.id = model_id
        self.skills = skills
        self.manager = DataManager()

        all_data = self.manager.load_data()
        saved_state = all_data.get(self.id, {})

        num_char = len(st.session_state.get("characters", []))

        saved_skills = saved_state.get("selected_skills", [None] * num_char)
        saved_mods = saved_state.get("modifiers", [0] * num_char)
        saved_rolls = saved_state.get("rolls", [random.randint(1, 20) for _ in range(num_char)])

        for i in range(num_char):
            if f"{self.id}_skill_{i}" not in st.session_state:
                st.session_state[f"{self.id}_skill_{i}"] = saved_skills[i]
            if f"{self.id}_modifier_{i}" not in st.session_state:
                st.session_state[f"{self.id}_modifier_{i}"] = saved_mods[i]
            if f"{self.id}_roll_{i}" not in st.session_state:
                st.session_state[f"{self.id}_roll_{i}"] = saved_rolls[i]

        self.render()


    def _save(self):
        current_chars = st.session_state.get("characters", [])
        num_char = len(current_chars)

        save_data = {
            "selected_skills": [st.session_state.get(f"{self.id}_skill_{i}") for i in range(num_char)],
            "modifiers": [st.session_state.get(f"{self.id}_modifier_{i}") for i in range(num_char)],
            "rolls": [st.session_state.get(f"{self.id}_roll_{i}") for i in range(num_char)]
        }

        all_data = self.manager.load_data()
        all_data[self.id] = save_data
        self.manager.save_data(all_data)


    @staticmethod
    def _get_degree_of_success(roll, modifier, dc):
        total = roll + modifier
        diff = total - dc

        if diff >=10: result = 3
        elif diff >= 0: result = 2
        elif diff > -10: result = 1
        else: result = 0

        if roll == 20: result = min(result + 1, 3)
        if roll == 1: result = max(result - 1, 0)

        return {0: ":red[Crit Fail]", 1: ":orange[Fail]",
                2: ":green[Success]", 3: ":blue[Crit Success]"}.get(result)


    def render(self):
        with st.expander(self.name):
            headers = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])
            headers[0].caption("Character")
            headers[1].caption("Skill")
            headers[2].caption("Modifier")
            headers[3].caption("Result")
            headers[4].caption("Reroll")

            for i, character in enumerate(st.session_state["characters"]):
                skill_key = f"{self.id}_skill_{i}"
                mod_key = f"{self.id}_modifier_{i}"
                roll_key = f"{self.id}_roll_{i}"

                with st.container(border=True):
                    cols = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])

                    cols[0].markdown(character.get("name"))

                    cols[1].selectbox(
                        "Skill",
                        options=[s.name for s in self.skills],
                        key=skill_key,
                        on_change=self._save,
                        label_visibility="collapsed"
                    )

                    cols[2].number_input(
                        "Modifier",
                        key=mod_key,
                        step=1,
                        format="%d",
                        on_change=self._save,
                        label_visibility="collapsed"
                    )

                    selected = st.session_state.get(skill_key)
                    if selected:
                        skill_obj = next((s for s in self.skills if s.name == selected), None)
                        if skill_obj:
                            dc = skill_obj.low_dc if st.session_state.get("tier") == "Low" else skill_obj.high_dc

                        result = self._get_degree_of_success(st.session_state[roll_key],
                                                             int(st.session_state[mod_key]),
                                                             dc)

                        cols[3].markdown(result)

                    if cols[4].button("Reroll", icon=":material/casino:", key=f"{self.id}_reroll_{i}"):
                        st.session_state[roll_key] = random.randint(1, 20)
                        self._save()
                        st.rerun()