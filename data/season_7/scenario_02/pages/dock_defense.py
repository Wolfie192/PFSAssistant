import streamlit as st

from src.ImageModel import ImageModel
from src.TextModel import TextModel
from src.VariableModel import VariableModel


def dock_defense():
    TextModel([
        "A preponderance of hanging ropes throughout the area can be used for climbing and swinging. PCs who have the pirate dedication (or other abilities that allow for swinging) will find a hanging rope anywhere they need one to be. Consider allowing swashbucklers and others to roll Acrobatics or Athletics for their initiative if they swing in on the ropes. The lower docks are only three feet below the upper ones, and do not require a check to leap down or clamber up.",
        "**The Waves:** There will be two waves to this fight. In wave one, pirate goblins come swinging in with their well-trained pirate gorillas. In wave two, more pirate goblins arrive accompanied by an underwater assault team of athamaru that peek out of the waves, take their shots, and then dive below the waters again. The waves follow one another with only a one-minute break.",
        "**Olad:** Olad doesn’t run and hide when his shipyard is set aflame he leaps into the fray! He grabs a belaying pin and runs to battle with the PCs, but he does not roll initiative or act. Mechanically, Olad is represented by allowing one of the PCs each round (the players can choose or make flat checks to see who gets this benefit) to count as flanking an enemy and gain an extra 1d6 Bludgeoning damage if the PC successfully hits.",
        "**Nairaba and Kitsch:** As noncombatants, Nairaba and Kitsch run and hide during combat, but also take steps to heal their fellow Pathfinders. At the end of each round, Nairaba hands Kitsch a healing potion (or elixir of unlife if the PC has negative healing) that Kitsch then loads into a bolt and fires at the most wounded Pathfinder while shouting, “This may sting!” Kitsch never misses with these bolts or hits someone with the wrong ammunition. Given that the PCs only have a minute-long break between waves, the healing from Nairaba and Kitsch is crucial to their success in this fight. They will also heal each PC once in between the waves.",
        "**Special Actions:** There are two special actions that the PCs may use during this fight. One is the one-action “Save the Shipyard!” and the other is the two-action “Appeal to Surrender!” Saving the shipyard earns the party Shipyard Successes that will bring them goodwill later. A successful Appeal to Surrender means that the PCs have prisoners they can question for information.",
        "Offer **Handout 2: Special Actions** to your players so that they are aware both of their own options and what Olad, Nairaba and Kitsch can offer them. The DCs for successful checks for “Save the Shipyard!” are DC 13 for Lore skills, DC 15 for other skills (DC 15 and DC 17 respectively for levels 3–4)."
    ])

    ImageModel("Handout 2 Special Actions")

    VariableModel("Shipyard Successes")


if __name__ == "__main__":
    dock_defense()