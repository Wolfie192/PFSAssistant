from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def kitchen():
    ReadAloudModel([
        "Meat packages bearing the labels of local Gebbite farms show signs of being recently prepared in this functional kitchen."
    ])

    TextModel([
        "The most recent activity in this kitchen is only a few days old, giving a clue that someone has been eating here. The pantry doesn’t include stairs leading down, as Zoroq’s villa has no basement."
    ])


if __name__ == "__main__":
    kitchen()