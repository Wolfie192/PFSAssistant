from pathlib import Path

from src import Directory
from src.ImageModel import ImageModel
from src.TextModel import TextModel


def map():
    TextModel([
        "The upper floor of Zoroq’s villa is where the entomologist spends all their time; recently, they’ve retreated to their study (area **B6**)."
    ])

    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "B. Villa Upper Floor GM Map.svg"))


if __name__ == "__main__":
    map()