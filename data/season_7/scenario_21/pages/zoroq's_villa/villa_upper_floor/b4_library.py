from src.ReadAloudModel import ReadAloudModel
from src.TextModel import TextModel


def library():
    ReadAloudModel([
        "The walls of this long room contain several bookshelves whose contents have mostly been pulled out and stacked in untidy piles. Several pillars support the ceiling; each carved with stylized images of marching insects Stairs lead downward."
    ])

    TextModel([
        "Although the PCs might assume the priests whose bodies they have found around the villa ransacked this library, Zoroq is actually to blame. The entomologist has, over the past several weeks, sorted and re-sorted through their books to bring relevant texts into their study. A quick look at the remaining books reveals several about natural history in Geb, basic necromantic treatises, curses, and studies in spoliation and rot—all topics that Zoroq doesn’t currently need."
        "The stairs descend to area **A1**."
    ])


if __name__ == "__main__":
    library()