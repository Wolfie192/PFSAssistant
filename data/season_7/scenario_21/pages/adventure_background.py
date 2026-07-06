import streamlit as st

from pathlib import Path

from src import Directory
from src.ImageModel import ImageModel
from src.TextModel import TextModel


def adventure_background():
    cols = st.columns([0.75, 0.25])
    with cols[0]:
        TextModel([
            "The nation of Geb is like no other in the Inner Sea region, for it is a nation whose primary residents are undead. Ghouls, ghosts, vampires, and other intelligent undead not only rule this land but run the economy, field the country’s imports and exports, and hawk their wares to each other. Life—traditional life, as most of the world knows it—is treated as a commodity, and often a one of little value.",
            "Mortal species can and do exist in Geb, where they’re colloquially known as the “quick.” The quick often act as agents, servants, or sustenance for undead in power. The Dead Laws, Geb’s legal code, define the country’s relationship between the living and the undead. They allow the mortals who exist in this place a modicum of protection in their everyday lives, although they restrict the use of vitality magic that is so often harmful to undead. Despite the complicated permissions found in the Dead Laws, a mortal that wanders too far from the safety of their home or patron can find many neighbors just waiting for the opportunity to feed.",
            "The grand black pyramid of the Cinerarium overlooks the nation’s capital of Mechitar. Here, the Ghost King Geb rules over his high court of Blood Lords, who in turn rule over the various aspects of the nation. Geb is a mostly absent monarch. Ever since word spread that his eternal foe, the immortal wizard Nex, has returned to his nation to the north, Geb has been slowly steering his forces once more back to war. These preparations consume the king’s time yet seem to proceed at a snail’s pace, but what do the undead have if not time?",
            "The Blood Lords are as ruthless and cunning as the living aristocrats and bureaucrats of other nations, with the added benefit of centuries to develop their plots and schemes. The Ghost King largely ignores the backstabbing and plotting of his lower courts. With his attention focused ever northward, the Pathfinder Society hopes to entreat the Blood Lords for access to Geb. The nation’s vast history makes it an enticing land to study, and it’s within the capital of Mechitar the Society hopes to earn a foothold with the spirit of cooperation.",
            "By leveraging a few contacts and pulling strings, the Pathfinder Society contacted **Msasa Kuatuz** (scheming female lich politician), a relatively low-ranking Blood Lord. For her part, Msasa sees the Pathfinder Society as the possible next rung on her ladder to success. If they can prove themselves, that is."
        ])

    with cols[1]:
        ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Msasa Kuatuz.svg"))


if __name__ == "__main__":
    adventure_background()