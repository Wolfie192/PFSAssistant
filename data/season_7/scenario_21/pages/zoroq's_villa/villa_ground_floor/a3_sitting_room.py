from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def sitting_room():
    ReadAloudModel([
        "This small sitting room contains torn, tattered, and dusty plush furniture. A thin glass case filled with soil occupies a low table between two chairs."
    ])

    TextModel([
        "Zoroq didn’t use this sitting room much even before they became captivated by research on Msasa’s behalf. The glass case is an ant farm, but all the striped yellow ants inside it died long ago."
    ])


if __name__ == "__main__":
    sitting_room()