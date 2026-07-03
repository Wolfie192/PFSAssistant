import streamlit as st

from pathlib import Path


class ImageModel():
    """
    Model for displaying images within a scenario page.
    """
    def __init__(self, image_path: Path, width: int = 720):
        self.image_path = image_path
        self.width = width


    def render(self):
        if not self.image_path.exists():
            st.warning(f"No image found at {self.image_path}")
            return

        st.image(self.image_path, width=self.width)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    bin_dir = Path.joinpath(root, "bin")
    images = Path.joinpath(bin_dir, "images")
    season = Path.joinpath(images, "season_7")
    scenario = Path.joinpath(season, "scenario_21")
    image = Path.joinpath(scenario, "Area Map.svg")

    ImageModel(image).render()