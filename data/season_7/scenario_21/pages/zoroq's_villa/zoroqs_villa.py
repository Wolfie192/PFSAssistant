from src.ReadAloudModel import ReadAloudModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.TextModel import TextModel


def zoroqs_villa():
    TextModel([
        "Zoroq’s two-story villa lies approximately five miles to the north of Mechitar, atop a small cliff along the inland route following the Axanir River. Msasa offers to have the PCs delivered to the villa in a wagon pulled by zombified cattle and driven by a skeleton chauffeur. Along the way, the PCs pass several sprawling farms. Various undead, predominantly zombies, tend to crops growing in the fields. Few living creatures also work on the farms, always kept behind fences that separate them from the mindless undead. These “quick” sport sallow countenances and neck injuries that belie frequent feeding.",
        "Read or paraphrase the following text when the PCs arrive at the villa."
    ], first_line_indent=False)

    ReadAloudModel([
        "The wagon shudders to a sudden stop just outside of the villa’s wide front porch. The building’s exterior shows signs of neglect and disrepair: shrubs haven’t been tended, dead leaves blow about the wide front portico, and the stone exterior is streaked with grime. The villa’s few windows have been bricked over long ago. The structure has a forlorn atmosphere that discourages approach."
    ])

    TextModel([
        "**Entering the Villa:** The PCs can enter the villa through the front doors to the entry hall (area **A1**), through the rear entrances to the greenhouse (area **A7**), or even by climbing to the upstairs balcony and entering the experiment room (area **B3**).",
        "**Villa Features:** The villa is constructed of sturdy stone. Its small windows have all been sealed with stone or brick, a common architectural choice in Geb. The villa interior is dark unless otherwise indicated, though dusty candelabras and cold fireplaces throughout can be relit. Ceilings are 15 feet high."
    ], first_line_indent=False)

    SubsectionHeaderModel("Timeline")
    TextModel([
        "Attentive PCs can piece together a rough timeline of recent events in the villa.",
        "- Zoroq’s prior experiments with striped yellow ants and petrified warriors are in the more distant past.",
        "- Six months ago, Zoroq became fixated on researching a local type of beetle with some connection to long-lived elementals. Msasa funded more work to connect these insects with immortality, and Zoroq jumped into experiments with enthusiasm.",
        "- A month ago, several mute priests arrived to ask about the secrets Zoroq was researching. Suspicious, the ghoul turned them away and retreated to their study to focus.",
        "- Three weeks ago, the priests snuck into the villa to steal Zoroq’s research, but the ghoul’s strange creatures and guardians defeated them all. Their bodies are still strewn throughout the villa, ignored by the obsessed entomologist.",
        "- Two weeks ago, an untended laboratory experiment exploded, freeing captive creatures there.",
        "- Zoroq remains in their study on the upper floor to this day, so engrossed with research that they have neglected to give Msasa any updates. Zoroq only leaves the study to take meals of fresh meat, which are delivered every week or so."
    ], first_line_indent=False)


if __name__ == "__main__":
    zoroqs_villa()