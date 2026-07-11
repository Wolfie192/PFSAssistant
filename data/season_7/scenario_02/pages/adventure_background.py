import streamlit as st

from src.ImageModel import Image
from src.TextModel import Text


def adventure_background():
    Text([
        "The Battle of Hellknight Hill, a conflict in which Andoran deployed soldiers to attack a fortified Hellknight position and liberate a town within the neighboring nation of Isger, has ratcheted up tensions in the Inner Sea to heights never before seen. Isger is under the protection of Cheliax, and it remains to be seen how the Chelaxian ruler Queen Abrogail Thrune II will respond. The Pathfinder Society has found itself on the Andoran side of the conflict after numerous run-ins with Chelaxian forces and the burning of Greensteeples, the only Pathfinder Society lodge in Cheliax.",
        "Considering the rising tension and move toward war, the Society's leadership, the Decemvirate, has decided to increase the Society's naval capabilities. To that end, **Immaculate-Weaving-Under-Moonlight Nairaba (fastidious male anadi dilettante) and **Kitsch** (boisterous female ysoki quartermaster), the two heads of the Procurement and Supplies Division of the Pathfinder Society, have been sent to secure a new vessel from the famed Augustana shipyards in Andoran. Though little trouble is expected, **Venture-Captain Brackett** (brash male human community organizer), head of operations in Andoran, feels it's better to be safe than sorry and deploys a group of newer agents to act as bodyguards for Nairaba and Kitsch.",
        "This was a fortuitous decision, as Cheliax has secretly funded a group of privateers to disrupt Andoren naval movements and shipping in the Inner Sea. One of their captains, **Conziva** (determined female nephilim human pirate), new to her command, has taken it upon herself to go all-out and assault the shipyard themselves. This is far beyond what Cheliax expected. Conziva will receive no further aid, nor will Cheliax act to stop her. She's slowly brought her crew into the docks of Augustana, acting like sailors looking for work. She's now ready to begin her assault, dreaming of both a safe home for her crew and of closure, as the Chelaxian government has promised, as part of their arrangement, to force her estranged family to meet with her."
    ])

    cols = st.columns(3)
    with cols[0]:
        Image("Nairaba", width=300)

    with cols[1]:
        Image("Kitsch")

    with cols[2]:
        Image("Venture-Captain Brackett", width=350)


if __name__ == "__main__":
    adventure_background()