from pathlib import Path

from src.ImageModel import ImageModel
from src import Directory


def map():
    ImageModel(Path.joinpath(Directory.scenario_images_dir(), "A. Villa Ground Floor GM Map.svg"))


if __name__ == "__main__":
    map()