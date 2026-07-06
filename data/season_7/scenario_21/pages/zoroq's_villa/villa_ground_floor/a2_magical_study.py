import streamlit as st

from pathlib import Path

from src import Directory
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.MonsterModel import MonsterModel
from src.CombatEncounterModel import CombatEncounterModel


def magical_study():
    ReadAloudModel([
        "Esoteric runes and ritualistic formulas cover the walls of this study. Various ingredients are scattered on some shelves here, next to a few old books."
    ])

    TextModel([
        "Zoroq began their research for Msasa in this room, but when it became clear that they didn’t have enough space here, they moved their experiments to the laboratory upstairs. A PC who succeeds at a DC 12 Nature or Occultism check realizes that these runes and formulas involve infusing a particular kind of beetle with necromantic energy; on a critical success, the PC realizes that the formulas are all speculative and incomplete. Nothing has been touched here for years."
    ])

    SkillCheckModel("Nature and Occultism Check on Runes",
                    [SkillModel("Nature", 12, 12),
                     SkillModel("Occultism", 12, 12)],
                    model_id="zoroqs_villa_a2_nature_occultism_check")

    TextModel([
        "**Creatures:** One of Zoroq’s experiments in undead insects, an enormous beetle carapace, lumbered into this room after killing the intruder in the entry hall (area **A1**). It remains here, occasionally swallowing a book or alchemical ingredient to keep the swarm that lives inside abdomen fed. It immediately attacks intruders, including those it detects elsewhere in the house. The ant swarm inside it—a species of striped yellow ant native to Geb—doesn’t act in the first round of combat and emerges from the carapace as its first action on the second round. These foes fight until destroyed."
    ])

    with st.expander("Combat Encounter"):
        with st.container(border=True):
            SubsectionHeaderModel("Adjusting Difficulty")
            TextModel([
                "You can adjust the difficulty of encounter **A2** in the following ways to make it easier or harder.",
                "**Easier:** Remove the swarm; the beetle's abdomen is empty.",
                "**Harder:** Add another army ant swarm that starts combat outside the beetle carapace."
            ], first_line_indent=False)

        beetle_carapace = MonsterModel(name="Beetle Carapace",
                                       path=Path.joinpath(Directory.scenario_monsters_dir(), "Beetle Carapace.svg")
                                       )
        army_ant_swarm = MonsterModel(name="Army Ant Swarm",
                                      path=Path.joinpath(Directory.scenario_monsters_dir(), "Army Ant Swarm.svg")
                                      )
        CombatEncounterModel("Combat Encounter",
                             [beetle_carapace, army_ant_swarm],
                             "zoroqs_villa_a2_combat_encounter")


if __name__ == "__main__":
    magical_study()