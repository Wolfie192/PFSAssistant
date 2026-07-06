from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def banquet_hall():
    ReadAloudModel([
        "This grand banquet hall is lit by faint sconces that line the walls The food upon the table, for mortals and otherwise, has either rotted or dried out long ago and is too shriveled to identify."
    ])

    TextModel([
        "The door to the greenhouse (area **A7**) is ajar."
    ])


if __name__ == "__main__":
    banquet_hall()