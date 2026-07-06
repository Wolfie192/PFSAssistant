import streamlit as st

from pathlib import Path

from src import Directory
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.MonsterModel import MonsterModel
from src.CombatEncounterModel import CombatEncounterModel


def antechamber():
    ReadAloudModel([
        "Fine but tattered furniture and a cold fireplace adorn this wide room. Two corpses in priestly vestments sprawl in the center of the room amid pools of dried blood. Double doors lead north and south The pungent aroma of rot and sulfur fills the room."
    ])

    TextModel([
        "These two corpses are more Anaphexia cultists dressed as Pharasmin priests, just as in area **A1**. One is a male human and the other is a female human; both lack their tongues. The cultists nearly reached Zoroq’s study before the guardians in this room killed them."
        "**Creatures:** Two unusual zombies stand in this room. They serve Zoroq as attendants and guards. A success in Zoroq’s recent research, these zombies are stuffed with chemicals and hundreds of tiny Gebbite rust beetles. The beetles crawl in and out of tears in the zombie flesh, continually feeding upon the zombie flesh and being restored by the acrid chemicals. The zombies don’t respond unless intruders enter the room or attack them, at which point they fight until destroyed."
    ])

    with st.expander("Combat Encounter"):
        with st.container(border=True):
            SubsectionHeaderModel("Adjusting Difficulty")
            TextModel([
                "You can adjust the difficulty of encounter B5 in the following ways to make it easier or harder.",
                "**Easier:** Replace one infested attendant with two giant Gebbite rust beetles (see area **B1**).",
                "**Harder:** Add another infested attendant."
            ], first_line_indent=False)

        infested_attendants = MonsterModel(
            name="Infested Attendant",
            path=Path.joinpath(Directory.scenario_monsters_dir(), "Infested Attendant.svg")
        )
        giant_gebbite_rust_beetle = MonsterModel(
            name="Giant Gebbite Rust Beetle",
            path=Path.joinpath(Directory.scenario_monsters_dir(), "Giant Gebbite Rust Beetle.svg")
        )

        CombatEncounterModel("Combat Encounter",
                             [infested_attendants, giant_gebbite_rust_beetle],
                             "zoroqs_villa_combat_b5_encounter")


if __name__ == "__main__":
    antechamber()