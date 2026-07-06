from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel
from src.SkillModel import SkillModel
from src.SkillCheckModel import SkillCheckModel


def grand_stair():
    ReadAloudModel([
        "A narrow staircase rises from the center of this room, its wooden railing now only shattered debris on the floor. Ash, soot, and strange rust-colored stains spread out from the stair, obviously from some sort of explosion or eruption from the chamber above. The room atop the stairs is illuminated with a glow that flickers ominously."
    ])

    TextModel([
        "The dark octagon on the map isn’t a set of stairs that lead down—Zoroq’s villa has no basement—but shows the extent of the damage from the laboratory above (area **B1**). A PC who examines the area of the explosion and succeeds at a DC 15 Nature check or a DC 18 Perception check realizes that amid the ashes is a large amount of rust-colored dust, as from some very old machine. If the Nature check is a critical success, the PCs remembers that certain elementals from the Plane of Metal emit a rust cloud with this type of dust."
    ])

    SkillCheckModel("Nature or Perception Check on Rust",
                    [SkillModel("Nature", 15, 15),
                     SkillModel("Perception", 18, 18)],
                    model_id="zoroqs_villa_a4_nature_perception_check")

    TextModel([
        "The stairs are difficult terrain and creak ominously if used, but they are stable. They lead to area **B1.**"
    ])


if __name__ == "__main__":
    grand_stair()