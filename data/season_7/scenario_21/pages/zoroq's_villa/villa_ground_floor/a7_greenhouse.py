import streamlit as st

from pathlib import Path

from src import Directory
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel
from src.MonsterModel import MonsterModel
from src.CombatEncounterModel import CombatEncounterModel


def greenhouse():
    ReadAloudModel([
        "Foliage left to grow wild has overtaken the beds in this greenhouse. Creepers stretch up the walls to the dirty glass ceiling above. Near the open door into the villa, a lump amid a long garden bed resembles a prone corpse overgrown with mold."
    ])

    TextModel([
        "A PC who examines the seedbeds here and succeeds at a DC 15 Nature check realizes the plants were all selected because they are attractive to insects of various types. On a critical success, the PC notices a few tiny flakes of rust and recalls a specialized local beetle called a Gebbite rust beetle that must have been drawn here in the past."
    ])

    SkillCheckModel("Nature Check on Plants",
                    [SkillModel("Nature", 15, 15)],
                    model_id="zoroqs_villa_a7_nature_check")

    TextModel([
        "**Hazard:** The corpse-shaped lump isn’t a body or a creature, only a coincidental shape of a dangerous mold."
    ])

    with st.expander("Poisonous Mold Hazard"):
        poisonous_mold = MonsterModel(
            name="Poisonous Mold",
            path=Path.joinpath(Directory.scenario_monsters_dir(), "Poisonous Mold.svg")
        )

        CombatEncounterModel("Hazard",
                             [poisonous_mold],
                             "zoroqs_villa_a7_hazard"
                             )


if __name__ == "__main__":
    greenhouse()