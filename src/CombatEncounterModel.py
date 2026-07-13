import random
import streamlit as st

from src.DataManager import DataManager
from src.ImageModel import Image


class CombatEncounter:
    def __init__(self, name: str):
        self.name = name
        self.manager = DataManager()

        if self.name not in st.session_state:
            all_data = self.manager.load_data()
            st.session_state[self.name] = all_data.get(self.name, {"entities": []})

        if "entities" not in st.session_state[self.name]:
            st.session_state[self.name]["entities"] = []

        if "combat_started" not in st.session_state[self.name]:
            st.session_state[self.name]["combat_started"] = False

        self._sync_characters()


    def _sync_characters(self):
        existing_ids = {e["id"] for e in st.session_state[self.name]["entities"]}

        for char in st.session_state.get("characters", []):
            if char.get("id") not in existing_ids:
                st.session_state[self.name]["entities"].append({
                    "id": char.get("id"),
                    "is_player": True,
                    "name": char.get("name"),
                    "token_num": None,
                    "init": None,
                    "max_hp": None,
                    "damage": None,
                    "is_active": False,
                    "reaction_used": False,
                    "conditions": []
                })


    def add_enemy(self, enemy_id: str, name: str, token: int, init_mod: int, max_hp: int, img_name: str):
        existing_ids = {e["id"] for e in st.session_state[self.name]["entities"]}

        if enemy_id not in existing_ids:
            st.session_state[self.name]["entities"].append({
                "id": enemy_id,
                "is_player": False,
                "name": name,
                "token_num": token,
                "init": random.randint(1, 20) + init_mod,
                "max_hp": max_hp,
                "damage": 0,
                "is_active": False,
                "reaction_used": False,
                "conditions": [],
                "img_name": img_name
            })
        self._save()


    def _save(self):
        all_data = self.manager.load_data()
        all_data[self.name] = st.session_state[self.name]
        self.manager.save_data(all_data)


    def _player_init_callback(self, entity_id):
        entities = st.session_state[self.name]["entities"]

        for entity in entities:
            if entity["id"] == entity_id:
                entity["init"] = st.session_state[f"{self.name}_{entity_id}_init"]

        st.session_state[self.name]["entities"] = entities
        self._save()


    def _update_damage_callback(self, entity_id):
        entities = st.session_state[self.name]["entities"]

        for entity in entities:
            if entity["id"] == entity_id:
                entity["damage"] += st.session_state[f"{self.name}_{entity_id}_damage_healing"]

                if entity["damage"] < 0: entity["damage"] = 0
                if entity["damage"] > entity["max_hp"]: entity["damage"] = entity["max_hp"]

                st.session_state[f"{self.name}_{entity_id}_damage_healing"] = None

        st.session_state[self.name]["entities"] = entities
        self._save()


    def render(self):
        with st.expander(self.name, expanded=True):
            headers = st.columns([0.05, 0.5, 0.05, 0.1, 0.1, 0.1, 0.05, 0.05])
            # Active Entity
            headers[0].caption("Active")
            headers[1].caption("Character")
            headers[2].caption("Token #")
            headers[3].caption("Init")
            headers[4].caption("HP")
            headers[5].caption("Damage/Healing")
            headers[6].caption("Reorder")
            headers[7].caption("")

            for i, entity in enumerate(st.session_state[self.name]["entities"]):
                cols = st.columns([0.05, 0.5, 0.05, 0.1, 0.1, 0.1, 0.05, 0.05])
                # cols = st.columns(8)

                if entity["is_active"]:
                    cols[0].markdown(":material/arrow_right_alt:")
                else:
                    cols[0].markdown(":material/check_indeterminate_small:")

                cols[1].markdown(entity["name"])

                cols[3].number_input(
                    "Init",
                    value=entity["init"],
                    step=1,
                    on_change=self._player_init_callback,
                    args=(entity["id"],),
                    label_visibility="collapsed",
                    key=f"{self.name}_{entity["id"]}_init"
                )

                if st.session_state[self.name]["entities"].index(entity) == 0:
                    if cols[6].button(
                            "",
                            icon=":material/arrow_upward:",
                            disabled=True,
                            key=f"{self.name}_{entity["id"]}_move_up"
                    ):
                        pass
                else:
                    if cols[6].button(
                            "",
                            icon=":material/arrow_upward:",
                            key=f"{self.name}_{entity["id"]}_move_up"
                    ):
                        st.session_state[self.name]["entities"][i], st.session_state[self.name]["entities"][i - 1] = \
                        st.session_state[self.name]["entities"][i - 1], st.session_state[self.name]["entities"][i]
                        self._save()
                        st.rerun()

                if st.session_state[self.name]["entities"].index(entity) == (
                        len(st.session_state[self.name]["entities"]) - 1):
                    if cols[7].button(
                            "",
                            icon=":material/arrow_downward:",
                            disabled=True,
                            key=f"{self.name}_{entity["id"]}_move_down"
                    ):
                        pass
                else:
                    if cols[7].button(
                            "",
                            icon=":material/arrow_downward:",
                            key=f"{self.name}_{entity["id"]}_move_down"
                    ):
                        st.session_state[self.name]["entities"][i], st.session_state[self.name]["entities"][i + 1] = \
                        st.session_state[self.name]["entities"][i + 1], st.session_state[self.name]["entities"][i]
                        self._save()
                        st.rerun()

                if not entity["is_player"]:
                    cols[2].markdown(entity.get("token_num"))

                    cols[4].markdown(f"{max(entity.get("max_hp") - entity.get("damage"), 0)}/{entity.get("max_hp")}")

                    cols[5].number_input(
                        "Damage",
                        step=1,
                        key=f"{self.name}_{entity["id"]}_damage_healing",
                        value=None,
                        on_change=self._update_damage_callback,
                        args=(entity.get("id"),),
                        label_visibility="collapsed"
                    )

            if st.session_state[self.name]["combat_started"]:
                cols = st.columns(4)

                if cols[0].button(
                    "Previous",
                    icon=":material/skip_previous:",
                    key="previous_turn_button",
                    width="stretch"
                ):
                    for entity in st.session_state[self.name]["entities"]:
                        if entity["is_active"]:
                            entity["is_active"] = False
                            active_idx = st.session_state[self.name]["entities"].index(entity)

                    if active_idx == 0: active_idx = len(st.session_state[self.name]["entities"]) - 1
                    else: active_idx -= 1

                    st.session_state[self.name]["entities"][active_idx]["is_active"] = True
                    st.rerun()


                if cols[1].button(
                    "Next",
                    icon=":material/skip_next:",
                    key="next_turn_button",
                    width="stretch"
                ):
                    for entity in st.session_state[self.name]["entities"]:
                        if entity["is_active"]:
                            entity["is_active"] = False
                            active_idx = st.session_state[self.name]["entities"].index(entity)

                    if active_idx == len(st.session_state[self.name]["entities"]) - 1: active_idx = 0
                    else: active_idx += 1

                    st.session_state[self.name]["entities"][active_idx]["is_active"] = True
                    st.rerun()

            else:
                cols = st.columns(2)

                if cols[0].button(
                    "Start Combat",
                    icon=":material/play_arrow:",
                    key="start_combat_button",
                    width="stretch"
                ):
                    st.session_state[self.name]["entities"] = sorted(st.session_state[self.name]["entities"], key=lambda x: (-x["init"], x["is_player"]))
                    st.session_state[self.name]["entities"][0]["is_active"] = True
                    st.session_state[self.name]["combat_started"] = True
                    st.rerun()

        displayed_entities = []
        for entity in st.session_state[self.name]["entities"]:
            if not entity.get("is_player"):
                if not entity.get("name") in displayed_entities:
                    displayed_entities.append(entity.get("name"))
                    with st.expander(entity.get("name")):
                        Image(entity.get("img_name"))