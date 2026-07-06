from src.TextModel import TextModel
from src.ReadAloudModel import ReadAloudModel
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel


def entry_hall():
    ReadAloudModel([
        "The unlocked double door opens to the visible dust and detritus of a neglected great hall as the light creeps inward. Cobwebs stretch across decorative columns and along the railing of a staircase leading upward. A door to the south stands ajar, revealing several dusty chairs. Near a door at the foot of the staircase lies a body, sprawled on the floor."
    ])

    TextModel([
        "The corpse on the floor is a male human priest wearing blue and white vestments beneath a traveling cloak. A prominent wooden religious symbol of Pharasma hangs around their neck. Any PC trained or better in Religion realizes that Pharasma’s followers are foes of undead, so and finding them in Geb is very peculiar.",
        "A PC who spends at least 10 minutes examining the corpse and succeeds at a DC 15 Medicine check realizes the body has been chewed on, as from a large animal (the carapace beetle in area **A2**), and has been dead for about three weeks. On a critical success, the PCs also notice the corpse’s tongue is missing and was cut out many weeks prior to death."
    ])

    SkillCheckModel("Medicine Check on Bodies",
                    [SkillModel("Medicine", 15, 15)],
                    "zoroqs_villa_a1_medicine_check")

    TextModel([
        "This corpse is one of many the PCs find in the villa. All appear to be priests of Pharasma but are secretly members of a cult of Norgorber from distant Ustalav called the Anaphexia.",
        "The stairs lead up to the library (area **B4**) on the upper floor.",
        "**Development:** If the PCs remain in this room for more than a minute or so, the carapace beetle in area **A2** comes through the open door and attacks."
    ], first_line_indent=False)


if __name__ == "__main__":
    entry_hall()