from src.ImageModel import ImageModel
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def battle_for_the_docks():
    TextModel([
        "Unknown to the Pathfinder delegation, some pirates from Captain Conziva’s ship, the Clawhold, have arrived to cause chaos on the docks. Captain Conziva has complicated feelings about Cheliax. Born and raised the youngest daughter of a mercantile demibaroness, she was tossed out as a teenager when her horns grew in, as Chelaxian society holds hellspawn nephilim in contempt. Conziva survived, fleeing to the Shackles, and joined a pirate crew as a ship’s girl. Conziva slowly rose through the ranks and now captains her own ship. In memory of her own welcome to ship life, she’s made a point of recruiting other outcasts. She’s reckless and a bit desperate, but her crew respects her and gave her the nickname “Lady Longboat” for both her willingness to be part of boarding parties and her slightly hoity-toity mannerisms.",
        "Conziva tossed the first Chelaxian agents who came to call on her off her ship, but then Cheliax offered a letter of marque, a title with an estate that could provide a safe home for all her crew, and the ability to confront the parents who abandoned her. Conziva did not want to lose this opportunity to make a new life for her chosen family while also getting the chance for closure with her parents. Now, she and her crew have gone beyond Cheliax’s mandate of harassing the sea trade and decided to attack the shipyards themselves. The pirates’ goal is to destroy ships, but they’re also endangering the workers in the yard. Before the attacks start, there are pirate saboteurs starting fires, and swinging weapons at shipyard workers to scare them away from the docks."
    ])

    ReadAloudModel([
        "The wooden docks creak underfoot as Olad leads the way off the Lucky Duck. “I have a few other options for—” he breaks off as a commotion starts near the docks. Dozens of rough-looking goblin sailors swarm throughout the area, lighting fires in the shipyard and brandishing weapons. They shriek gleefully as terrified dockworkers scream and scramble out of the way. Plumes of smoke rise, and the scent of burning wood fills the air.",
        "Olad puffs out his chest. “My ships! You’ll have my ships over my dead body!” Olad shouts as he grabs a belaying pin and jumps into the fray.",
        "From all sides, the sounds of “Ook-ook-ook!” calls rise as both monkey goblins and gorilla pirates grab onto ropes and swing into the dock area, attacking everyone in their path."
    ])

    ImageModel("A. Battle for the Docks GM Map")


if __name__ == "__main__":
    battle_for_the_docks()