import streamlit as st

from pathlib import Path

from src import Directory
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel
from src.TextModel import TextModel
from src.ImageModel import ImageModel
from src.ReadAloudModel import ReadAloudModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.SectionHeaderModel import SectionHeaderModel


def getting_started():
    with st.container(border=True):
        SubsectionHeaderModel("The Danger of Death!")
        TextModel([
            "All PCs know that if they perish in Geb, Gebbite society is allowed to raise them as mindless undead to serve the nation for eternity The Pathfinder Society wouldn’t send agents to Geb without this pivotal piece of information!"
        ])

    TextModel([
        "When this scenario begins, the PCs have already arrived in Mechitar to meet with Blood Lord Msasa Kuatuz on behalf of the Society.",
        "Read or paraphrase the following to get the adventure underway."
    ], first_line_indent=False)

    ReadAloudModel([
        "The great black pyramid of the Cinerarium looms solemnly over Geb’s capital city of Mechitar. While an entire nation of the undead can seem grim and joyless to the living, Mechitar is not without its grandiose displays of color. Large banners and tapestries denoting houses of the ruling Blood Lords stand on the city walls and along the entrance to the great pyramid. Colorful canvas stretching from rooftop to rooftop shades the streets and the undead inhabitants performing their duties around the city.",
        "The Pathfinder Society has arranged an audience with a minor Blood Lord, a lich named Msasa Kuatuz. Two heavily armed and armored zombies provide an escort to Msasa’s office. The lich’s large office is grandly decorated with rich tapestries of green and gold, with insect motifs on every wall. Lit censers stand in each corner, a benefit more for the living who might find the ever-present odor of rot unpleasant.",
        "Msasa’s true age is impossible to guess, but her weathered skin and deep eyes hint at immense experience. Similarly ancient-looking texts cover the desk in her chambers, likely denoting extensive research and planning.",
        "Msasa stands from behind her desk and dismisses the zombie escorts. With practiced ease, she steps to the front of her desk, concealing her work from curious eyes.",
        "“Allow me to welcome the Pathfinder Society to Geb,” Msasa says. Her words are patient and deliberate, as befits someone with the luxury of time to practice speech. “Your organization wishes to place a lodge upon our soil, I know. As I’ve described to your superiors in detail, such a thing could take some time. Particularly with regard to an organization filled with so many... vibrant people, our Dead Laws can be, ah, difficult to navigate. But perhaps the process may be expedited if you could perform a much-needed task I require.”",
        "“An ancient ally of mine, a ghoul by the name of Zoroq, was working on some research for me. They have not been heard from for many months now. It is unlikely they have met with a violent end, ensconced as they are within the safety of their villa, but I need to know for sure.” Msasa gestures toward one of the insect designs in her office. “Zoroq is a well-known entomologist. You can imagine the field can have some interesting implications when it comes to dead flesh. I need to be assured not only that Zoroq is safe, but that their research hasn’t been stolen or fallen in the hands of rivals who only wished they had the time we do to dedicate to study. Bring Zoroq and their research back to me and I will ensure your request is put before the courts and addressed as expeditiously as possible for our culture and government.”"
    ])

    TextModel([
        "After Msasa introduces herself, the PCs can also introduce themselves to each other, if they haven’t already. In addition to their primary mission to establish a good relationship with Msasa, the PCs have additional requests from the Grand Lodge and Radiant Oath factions; give the players **Handout #1: Machinations of Politics** and **Handout #2: The Efficacy of Life Magic.**"
    ])

    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Handout #1 Machinations of Politics.svg"), width=900)
    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Handout #2 The Efficacy of Life Magic.svg"), width=900)

    TextModel([
        "The PCs also have an opportunity to ask Msasa questions about her errand, which is also a chance to learn a few things about Gebbite high society, as Gorm Greathammer requested. She is forthright in her answers, but it should be clear she’s withholding the full situation, as is to be expected from an ancient politician.",
        "**What is your role/position in the Blood Lords?** “I contribute to the education of Mechitar’s intelligent undead in the arts of science and magic. My work occasionally includes the exchange of information with living mortals such as yourselves, though this would be the first act of cooperation between our nation and the Pathfinder Society as a whole.”",
        "**Where do we find Zoroq?** “They own a villa a few miles north of the city along the Axanir River. I’ll arrange for all of your transportation.”",
        "**What is Zoroq’s research?** “As an entomologist and a ghoul, Zoroq has unique insights into how insects might help to preserve dead flesh and ensure immortality in an unusual way. With our long *lifespans*,” she air-quotes almost mockingly, “the applications might prove useful.”",
        "**How long have you and Zoroq known each other?** “For at least two human lifetimes. We are...” Msasa pauses in the search for an unfamiliar word, turning options over in her mind. “...friends, you might say.”",
        "**Were you funding their research?** “Yes. Heavily.” Msasa does not explain further.",
        "**Are you currently in conflict with any of the other Blood Lords?** Msasa laughs and does not elaborate.",
        "**Mission Gear:** Msasa offers the PCs a *scroll of soothe* (rank 2) if anyone can use it, remarking about the wisdom of securing investments and ensuring their safety.",
        "Whether or not she hands over the scroll, Msasa also gives the PCs **Handout #3: Kuatuz Writ**, which permits them to use forbidden vitality magic only in Zoroq’s villa during the course of their recovery efforts. “Do not make me regret this, Pathfinders,” she says sternly."
    ], first_line_indent=False)

    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Handout #3 Kuatuz Writ.svg"), width=900)

    SectionHeaderModel("Religion, Society, or Geb Lore (Recall Knowledge)")

    TextModel([
        "A PC who succeeds at a DC 22 Religion check, a DC 20 Society check, or a DC 15 Geb Lore check to Recall Knowledge might know more about the nation of Geb. A failure grants no information, and a critical success grants the additional information in the critical success entry. Remember that these checks should be rolled secretly."
    ])

    SkillCheckModel("Religion, Society, or Geb Lore Check",
        [SkillModel("Religion", 22, 22),
        SkillModel("Society", 20, 20),
        SkillModel("Geb Lore", 15, 15)],
        model_id="getting_started_recall_knowledge_geb"
    )

    TextModel([
        "**Critical Success** Intrigue between the Blood Lords has never been greater Since Geb returned to inexorably turn the nation’s economy to fielding a war against his rival Nex, Blood Lords who have been used to power for centuries risk it slipping away Many are secretly frustrated with their monarch’s plans and eager to make new allies as politics shift.",
        "**Success** The Blood Lords have spent many long years administering the nation while the Ghost King Geb was effectively absent Many Blood Lords have longstanding feuds with each other, and all cultivate useful agents across the nation and beyond.",
        "**Critical Failure** Rumors of Geb’s return are false and are only a trick of a particularly cunning Blood Lord looking to seize greater power in the nation."
    ], first_line_indent=False)

    SubsectionHeaderModel("Hero Points")
    TextModel([
        "Once the PCs have finished their preparations, remind them that they each have 1 Hero Point available."
    ])


if __name__ == "__main__":
    getting_started()