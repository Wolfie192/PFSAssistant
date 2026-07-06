import streamlit as st

from pathlib import Path

from src import Directory
from src.TextModel import TextModel
from src.ReadAloudModel import ReadAloudModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.MonsterModel import MonsterModel
from src.CombatEncounterModel import CombatEncounterModel


def laboratory():
    TextModel([
        "This room is illuminated by *everlight crystals* embedded in the ceiling, showing the extent of the damage here; the lights flicker occasionally."
    ])

    ReadAloudModel([
        "A terrible accident has befallen this laboratory, spreading debris and ash around the room. A lab table to the west was the source of the explosion, which shredded a fine rug and blew down the staircase in the middle of this room. Three cages that once stood near the table are now nothing more than twisted metal."
    ])

    TextModel([
        "The cause of this explosion was mere negligence. Zoroq became so engrossed by work in their study that their alchemical experiments here overloaded and exploded a few weeks ago. Zoroq had been studying the unusual nature of a tiny, rust-colored beetle native to the region, the Gebbite rust beetle. He suspects some connection between the beetles and the exceedingly ancient type of elementals from the Plane of Metal called rust scarabs.",
        "Zoroq had been experimenting with the beetles and managed to not only grow two of them to immense size for ease of study, but to capture one of the elusive rust scarabs as well (being focused on their work and unable to speak Talican, Zoroq never realized that the rust scarab is a sapient creature). The explosion freed all three creatures, who now roam this room freely. The rust scarab has been carefully examining the destroyed remains of the experiments, hoping to learn a little about why the ghoul captured it.",
        "The stairs lead down to area **A4**. They are damaged but safe for the PCs to traverse.",
        "**Creatures:** The rust scarab is still surly about its imprisonment and likely to attack any intruders. The two giant Gebbite rust beetles, who indeed have a strange affinity with the rust scarab, join the attack. Once the rust scarab’s carapace breaks, it retreats to one side of the room and grouses in Talican about its fate.",
        "If the PCs can establish communication, the rust scarab explains that it was a captive of a studious and absent-minded ghoul with a wide range of interests in insects and immortality. The ghoul left through the doors to the south a few weeks ago and the untended experiments exploded soon thereafter, freeing the captives. Given the option, the rust scarab would prefer to leave the villa. Surviving giant beetles trail behind it like loyal pets."
    ])

    with st.expander("Combat Encounter"):
        with st.container(border=True):
            SubsectionHeaderModel("Adjusting Difficulty")

            TextModel([
                "You can adjust the difficulty of encounter **B1** in the following ways to make it easier or harder although, as a Trivial encounter, adjustment probably isn't necessary.",
                "**Easier:** Remove one giant Gebbite rust bettle.",
                "**Harder:** Add another rust scarab."
            ], first_line_indent=False)

        rust_scarab = MonsterModel(
            name="Rust Scarab",
            path=Path.joinpath(Directory.scenario_monsters_dir(), "Rust Scarab.svg")
        )
        giant_gebbite_rust_beetle = MonsterModel(
            name="Giant Gebbite Rust Beetle",
            path=Path.joinpath(Directory.scenario_monsters_dir(), "Giant Gebbite Rust Beetle.svg")
        )

        CombatEncounterModel("Combat Encounter",
                             [rust_scarab, giant_gebbite_rust_beetle],
                             "zoroqs_villa_combat_encounter_b1")


if __name__ == "__main__":
    laboratory()