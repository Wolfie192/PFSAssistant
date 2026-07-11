import streamlit as st

from src.VariableModel import VariableModel
from src.CombatEncounterModel import CombatEncounterModel
from src.TextModel import TextModel
from src.MonsterModel import MonsterModel


def gorilla_warfare():
    TextModel([
        "The riggers of the Clawhold are a bunch of monkey goblins who have been loyal to Captain Conziva ever since she welcomed not just them, but their pet gorillas as well. These pirates and their pet shriek as they swing into battle and take boarding actions against the PCs, letting out a cacophony of “ooks.” The moment they’re in range, the gorillas use their frightening display. Because the goblins have trained their gorillas well, spells and abilities with the linguistic trait work on them, including the Appeal to Surrender action."
    ])

    VariableModel("Shipyard Successes")


    if st.session_state["tier"] == "Low" and st.session_state["challenge_points"] <= 9:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (Low Tier: <10 CP)",
            [
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Gorilla")
            ], model_id="gorilla_warfare_combat_encounter_low_9"
        )
    elif st.session_state["tier"] == "Low" and st.session_state["challenge_points"] <= 11:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (Low Tier: 10-11 CP)",
            [
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Gorilla")
            ], model_id="gorilla_warfare_combat_encounter_low_10_11"
        )
    elif st.session_state["tier"] == "Low" and st.session_state["challenge_points"] <= 13:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (Low Tier: 12-13 CP)",
            [
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_low_12_13"
        )
    elif st.session_state["tier"] == "Low" and st.session_state["challenge_points"] <= 15:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (Low Tier: 14-15 CP)",
            [
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Gorilla"),
                MonsterModel("Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_low_14_15"
        )
    elif st.session_state["tier"] == "Low" and st.session_state["challenge_points"] <= 18:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (Low Tier: 16-18 CP)",
            [
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Goblin"),
                MonsterModel("Pirate Gorilla"),
                MonsterModel("Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_low_16_18"
        )
    elif st.session_state["tier"] == "High" and st.session_state["challenge_points"] < 19:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (High Tier: <19 CP)",
            [
                MonsterModel("Goblin Rigger"),
                MonsterModel("King Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_high_18"
        )
    elif st.session_state["tier"] == "High" and st.session_state["challenge_points"] <= 22:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (High Tier: 19-22 CP)",
            [
                MonsterModel("Goblin Rigger"),
                MonsterModel("Goblin Rigger"),
                MonsterModel("King Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_high_19_22"
        )
    elif st.session_state["tier"] == "High" and st.session_state["challenge_points"] <= 27:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (High Tier: 23-27 CP)",
            [
                MonsterModel("Goblin Rigger"),
                MonsterModel("Goblin Rigger"),
                MonsterModel("Goblin Rigger"),
                MonsterModel("King Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_high_23_27"
        )
    elif st.session_state["tier"] == "High" and st.session_state["challenge_points"] <= 32:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (High Tier: 28-32 CP)",
            [
                MonsterModel("Goblin Rigger"),
                MonsterModel("King Pirate Gorilla"),
                MonsterModel("King Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_high_28_32"
        )
    elif st.session_state["tier"] == "High" and st.session_state["challenge_points"] >= 33:
        CombatEncounterModel(
            "Wave 1: Gorilla Warfare (High Tier: >32 CP)",
            [
                MonsterModel("Goblin Rigger"),
                MonsterModel("Goblin Rigger"),
                MonsterModel("Goblin Rigger"),
                MonsterModel("King Pirate Gorilla"),
                MonsterModel("King Pirate Gorilla")
            ], model_id = "gorilla_warfare_combat_encounter_high_33"
        )


if __name__ == "__main__":
    gorilla_warfare()