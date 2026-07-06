from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SkillCheckModel import SkillCheckModel
from src.SkillModel import SkillModel


def study():
    ReadAloudModel([
        "This lofty study is strewn with books and notes. Notes and graphs are scattered haphazardly across a central table and pinned to the walls. Many papers display images of beetles inscribed within esoteric sigils. The only clear space in the room is, oddly, an enormous wooden desk against the room’s west wall, which bears only a few trays and small pieces of chitin."
    ])

    TextModel([
        "The ghoul entomologist **Zoroq** (obsessive nonbinary ghoul researcher) is here working at the desk, which holds the dissected remains of several tiny Gebbite rust beetles in various states of anatomical examination. Zoroq is surprised to see visitors and initially recoils if any PC bears symbols of Pharasma, since they remind them of their recent pushy visitors. However, it should be easy for the PCs to calm Zoroq and explain why they’ve come. When it becomes clear that Zoroq has neglected to send reports to Msasa and that their old friend is worried about them, they become sheepish."
        "Zoroq would like a few days—a week at most—to wrap up some hanging research and then deliver a more complete report to Msasa on their own. A PC who succeeds at a DC 15 Perception check to Sense Motive realizes that this time is likely to stretch into weeks or longer, given the entomologist’s obsessive dedication. If the PCs insist on returning Zoroq to Msasa right away, ghoul sighs, scoops up some relevant research notes, and is ready to go in only a few minutes."
    ])

    SkillCheckModel("Perception Check to Sense Motive",
                    [SkillModel("Perception", 15, 15)],
                    model_id="zoroqs_villa_b6_perception_check")


if __name__ == "__main__":
    study()