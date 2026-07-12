import uuid
import random
import streamlit as st

from src.DataManager import DataManager

from src.SkillModel import Skill


class SkillCheck:
    def __init__(self, name: str, skills: list[Skill]):
        self.name = name
        self.id = str(uuid.uuid4())
        self.skills = skills
        self.manager = DataManager()

        if self.id not in st.session_state:
            all_data = self.manager.load_data()
            saved_data = all_data.get(self.id, {})
            st.session_state[self.id] = saved_data

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
        all_data[self.id] = st.session_state[self.id]
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

                st.session_state[self.id][char_id]["skill"] = cols[1].selectbox(
                    "Skill",
                    options=[s.name for s in self.skills],
                    index=None,
                    on_change=self._save,
                    label_visibility="collapsed",
                    key=f"{self.id}_{char_id}_skill"
                )

                st.session_state[self.id][char_id]["modifier"] = cols[2].number_input(
                    "Modifier",
                    step=1,
                    on_change=self._save,
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


# class SkillCheck:
#     def __init__(self, name: str, skills: list[Skill], model_id: str):
#         self.name = name
#         self.id = model_id
#         self.skills = skills
#         self.manager = DataManager()
#
#         saved_data = self.manager.get_model_data(self.id)
#
#         if self.id not in st.session_state:
#             st.session_state[self.id] = saved_data
#
#         self.data = st.session_state[self.id]
#
#         for char in st.session_state["characters"]:
#             char_id = char.get("id")
#
#             if char_id not in self.data:
#                 self.data[char_id] = {
#                     "skill": None,
#                     "modifier": 0,
#                     "roll": random.randint(1, 20)
#                 }
#
#         self.render()
#
#
#     def _save(self):
#         all_data = self.manager.load_data()
#         all_data[self.id] = st.session_state[self.id]
#         self.manager.save_data(all_data)
#
#
#     @staticmethod
#     def _get_degree_of_success(roll, modifier, dc):
#         total = roll + modifier
#         diff = total - dc
#
#         if diff >=10: result = 3
#         elif diff >= 0: result = 2
#         elif diff > -10: result = 1
#         else: result = 0
#
#         if roll == 20: result = min(result + 1, 3)
#         if roll == 1: result = max(result - 1, 0)
#
#         return {0: ":red[Crit Fail]", 1: ":orange[Fail]",
#                 2: ":green[Success]", 3: ":blue[Crit Success]"}.get(result)
#
#
#     def render(self):
#         with st.expander(self.name):
#             headers = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])
#             headers[0].caption("Character")
#             headers[1].caption("Skill")
#             headers[2].caption("Modifier")
#             headers[3].caption("Result")
#             headers[4].caption("Reroll")
#
#             for char in st.session_state["characters"]:
#                 char_id = char.get("id")
#
#                 char_state = st.session_state[self.id][char_id]
#
#                 cols = st.columns([0.35, 0.25, 0.1, 0.2, 0.1])
#
#                 cols[0].markdown(char.get("name"))
#
#                 cols[1].selectbox(
#                     "Skill",
#                     options=[s.name for s in self.skills],
#                     key=f"{self.id}_{char_id}_skill",
#                     on_change=self._save,
#                     label_visibility="collapsed"
#                 )
#
#                 cols[2].number_input(
#                     "Modifier",
#                     key=f"{self.id}_{char_id}_modifier",
#                     step=1,
#                     on_change=self._save,
#                     label_visibility="collapsed"
#                 )
#
#                 current_roll = char.get("roll")
#                 current_mod = st.session_state.get(f"{self.id}_{char_id}_modifier")
#                 current_skill = st.session_state.get(f"{self.id}_{char_id}_skill")
#
#                 skill_obj = next((s for s in self.skills if s.name == current_skill), None)
#                 if skill_obj:
#                     dc = skill_obj.high_dc if st.session_state["tier"] == "High" else skill_obj.low_dc
#                     result = self._get_degree_of_success(current_roll, current_mod, dc)
#                     cols[3].markdown(result)
#
#                 if cols[4].button("Reroll", icon=":material/casino:", key=f"{self.id}_{char_id}_reroll"):
#                     st.session_state[self.id][char_id]["roll"] = random.randint(1, 20)
#                     self._save()
#                     st.rerun()