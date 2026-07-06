from pathlib import Path

from src import Directory
from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel
from src.ImageModel import ImageModel


def statuary_room():
    ReadAloudModel([
        "This wide room contains two rows of statues, each depicting a female warrior charging to battle or raising a weapon. Each statue has a necklace placed around its neck A litter of dead leaves is scattered before doors leading to an exterior balcony. These doors stand slightly ajar, revealing two corpses lying face-down on the balcony, twisted as though in agony."
    ])

    TextModel([
        "All eight statues here were taken from the Field of Maidens, an area in southern Geb where the ghost king petrified an army of attackers. Some petrified maidens can move, especially to return to the field where they were petrified, but these eight have been immobile for decades and don’t move while the PCs are here.",
        "The necklaces around each statue’s throat were obviously added more recently and are made of fused insect carapaces. They used to bear a collective curse, but the curse was expended when one of the Anaphexia cultists tried to remove a necklace. The curse struck them both dead with millions of spectral insect bites.",
        "The corpses are two male humans dressed in priestly attire and bearing symbols of Pharasma, just like the corpse in area **A1**, and are also missing their tongues. Here, a successful DC 15 Medicine check reveals the pair were killed by a swarm of insects, though no insects are present now. A PC who learns this cause of death can attempt a DC 15 Arcana or Occultism check; on a success, the PC realizes that the deaths are not due to any physical insects, but spectral ones summoned by some type of curse or hazard that is now expended."
    ])

    SkillCheckModel("Medicine Check on Corpses",
                    [SkillModel("Medicine", 15, 15)],
                    model_id="zoroqs_villa_b3_medicine_check")

    SkillCheckModel("Arcana or Occultism Check on Cause of Death",
                    [SkillModel("Arcana", 15, 15),
                     SkillModel("Occultism", 15, 15)],
                    model_id="zoroqs_villa_b3_arcana_occultism_check")

    TextModel([
        "One corpse bears a satchel containing some treasure and Handout #4: Letter from Msasa."
    ])

    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "Handout #4 Letter from Msasa.svg"))

    TextModel([
        "**Development:** The necklaces don’t survive attempts to remove them; a PC who attempts to remove a necklace finds that it stretches oddly, like taffy, before falling to pieces. These statues and necklaces are all from one of Zoroq’s prior experiments that didn’t bear fruit, but the ghoul liked the statues enough to use them as decor."
        "**Reward:** The corpse’s satchel holds two vials of moderate bottled sunlight, which is illegal in Geb, and a religious symbol of Norgorber worth 15 gp. A PC who examines this religious symbol can attempt a DC 20 Religion or Society check to Recall Knowledge. On a success, the PC remembers about the Anaphexia and their obsession with secrets; share the first paragraph of the Anaphexia section."
    ])

    SkillCheckModel("Religion or Society Check on Religious Symbol",
                    [SkillModel("Religion", 20, 20),
                     SkillModel("Society", 20, 20)],
                    model_id="zoroqs_villa_b3_religion_society_check")


if __name__ == "__main__":
    statuary_room()