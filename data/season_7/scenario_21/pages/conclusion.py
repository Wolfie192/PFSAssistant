from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.TextModel import TextModel


def conclusion():
    TextModel([
        "Once the PCs return Zoroq to Msasa’s office (or when the PCs alert her to Zoroq’s safety and eventual arrival), she thanks them for their efforts. As promised, Msasa puts the prospect of a Mechitar Pathfinder Society lodge to the other Blood Lords. She requests that the organization remain patient while the process works through the undead courts."
    ])

    SubsectionHeaderModel("Reporting Notes")

    TextModel([
        "If the PCs returned Zoroq to Msasa immediately, check box A on the reporting sheet. If they let Zoroq have more time to complete their research, check box **B**."
    ])

    SubsectionHeaderModel("Primary Objectives")

    TextModel([
        "The PCs complete their primary objective if they return Zoroq to Msasa or if they alert her of their research. Doing so earns each PC 2 Reputation with their chosen faction."
    ])

    SubsectionHeaderModel("Secondary Objectives")

    TextModel([
        "The PCs complete their secondary objective if they discover the five cultist corpses in the villa. Doing so earns each PC 2 Reputation with their chosen faction."
    ])

    SubsectionHeaderModel("Faction Notes")

    TextModel([
        "The mission into Geb provides the Grand Archive an opportunity to gain information about Blood Lords politics and provides the Radiant Oath an opening to evaluate the use of prohibited vitality magic in Geb."
        "**Grand Archive:** If at least one PC critically succeeds at the Recall Knowledge at the start of the scenario or learns all of the details Msasa has to share after the mission briefing, each PC earns 2 Reputation with the Grand Archive faction."
        "**Radiant Oath:** If the PCs use an item or spell with the vitality trait in the villa (such as when fighting undead or healing themselves), they confirm that such magic operates normally within Geb’s boarders. Each PC earns 2 additional Reputation with the Radiant Oath faction."
    ])

    SubsectionHeaderModel("Treasure Bundles")

    TextModel([
        "Area **B2a**, page 10: 1 Treasure Bundle for investigating the storage room.",
        "Area **B3**, page 10: 2 Treasure Bundles for searching the corpses.",
        "Area **B5**, page 10: 3 Treasure Bundles for searching the corpses.",
        "**Conclusion**, page 11: 4 Treasure Bundles for locating Zoroq for Msasa."
    ], first_line_indent=False)


if __name__ == "__main__":
    conclusion()