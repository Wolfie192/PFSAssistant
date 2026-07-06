from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def storage():
    ReadAloudModel([
        "Dusty crates are stacked haphazardly in this chamber. This might have once been a guest room, as a wide couch and furniture are just visible beneath the stacked storage."
    ])

    TextModel([
        "Though undead guests have little need for beds, the comfortable furnishings that groan beneath the weight of decades of haphazard storage show that these used to be private rooms. Zoroq hasn’t had visitors staying in their villa for quite some time.",
        "The crates contain some unused equipment but mostly paper: stacks upon stacks of academic treatises, research, and rough drafts.",
        "**Reward:** If the PCs look around in area **B2a**, they discover a strange charm forgotten by a long-ago guest. This is a *grave token*."
    ], first_line_indent=False)


if __name__ == "__main__":
    storage()