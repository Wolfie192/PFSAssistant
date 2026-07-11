from src.ReadAloudModel import ReadAloudModel
from src.SkillCheckModel import SkillCheckModel
from src.SubsectionHeaderModel import SubsectionHeaderModel
from src.TextModel import TextModel
from src.SkillModel import SkillModel


def getting_started():
    TextModel([
        'This scenario starts in Augustana, within a private room that Venture-Captain Brackett has rented in the Brine Shark\'s Bistro, a modest eatery in the  Shipyard district that has some local fame for its savory crab cakes and compelling view of the docks and tall warships of the Great Salt Harbor. In addition to Brackett, the room also includes the two heads of Procurement and Supply, the fastidious Nairaba and the boisterous Kitsch. Read or paraphrase the following to get the adventure underway.'
    ])

    ReadAloudModel([
        "“Excellent, you're all here,” Venture-Captain Brackett says as he gestures to seats around a large wooden table in this private dining room. “I have two people you need to meet. They're responsible for fulfilling the Pathfinder supplies that you equip yourselves with before each mission. First, is our head quartermaster, Kitsch.”",
        "He points to an ysoki woman using a full toolkit, including various pliers, saws and picks, to dismember a large crab carcass. Kitsch's overalls are liberally smeared and spattered with both grease and shell bits. She glances up, waves, and then returns her focus to trying to break apart the crab shell without saying a word.",
        "Then Brackett points out a tall mwangi man in an elegant tunic unsuccessfully trying to stay out of spatter range. “And this man is our Head of Procurement, Immaculate-Weaving-Under-Moonlight Nairaba.”",
        "“Please, that is such a long mouthful,” the man says as he passes out napkins and cleaning cloths. “Feel free to call me, Nairaba. Tell me, what are you called?”"
    ])

    TextModel([
        "Allow the PCs to introduce themselves to Nairaba, Kitsch and Brackett if they haven't already.",
        "While they talk, waiters bring in wine, savory crab cakes and other seafood dishes. Nairaba pours wine for everyone and then tastes it, nearly spitting it out. “Oh my, has this gone off? It may be more suitable as cleaning solvent than as a beverage.”",
        "A PC wishing to inspect the wine can do so with a successful DC 10 Alcohol Lore (or DC 13 Society) to recognize the vintage as Sauerton Red, a local Andoren vintage known for being both cheap and nearly undrinkable to those unused to its acidic aftertaste."
    ])

    SkillCheckModel("Recall Knowledge on wine.",
                    [
                        SkillModel("Alcohol Lore", 10, 12),
                        SkillModel("Society", 13, 15)
                    ],
                    model_id="getting_started_recall_knowledge_wine")

    TextModel([
        "Kitsch glances furtively around for waitstaff, then dumps the bottle of Sauerton Red into a dropping plant. She holds up her hands for a moment and pulls three bottles of wine o ut of her cheek pouches. The moment she empties her pouches she says, “Sometimes the secret to a good supply chain is knowing when you need to smuggle things in. I think you'll find these bottles are much better, Nairaba.”",
        "“Thank you.” Nairaba carefully wipes each bottle down before passing them around; they are an excellent Galtan vintage."
    ])

    ReadAloudModel([
        "Brackett closes the door firmly so that no other waitstaff can invade. “Now that you've all been sufficiently wined and dined,” he says, “it's time to explain why we've scheduled this little excursion to Augustana. Cheliax has never embraced the Society, even at the best of times. They made Pathfinders illegal within their country. Then a few months ago, they burnt Greensteeples, the secret lodge we had there.”",
        "“But since the Battle of Hellknight Hill, they've grown positively restless,” Nairaba says. “We've always had Chelaxian smugglers and the like willing to deal with the Society, but now they're all treating us like pariahs, and some have told us that the Chelaxian military is requisitioning all the supplies they would normaly sell to us.”",
        "Brackett nods. “Immediately after the battle, Zarta Dralneen warned us that Cheliax does not forgive slights. Since Isger is under the protection of Cheliax, Queen Abrogail will want revenge. With an Inner Sea war brewing, the Society's leadership believes that we need more ships for our naval defenses.”",
        "“So that's why Nairaba and I are here,” Kitsch says, “This is the biggest shipyard in the Inner Sea. But Nairaba and I aren't fighters. We're asking you to escort us and look for signs of trouble.”",
        "“No one believes that Cheliax will do anything direct without a formal declaration of war,” Brackett says coldly. “But that doesn't mean that they won't try indirect and underhanded methods.”"
    ])

    TextModel([
        "Brackett, Nairaba and Kitsch attempt to answer the PCs questions.",
        "**What is our budget for ship purchases? How many ships are we buying today?** “Let us worry about the money,” Nairaba says gently, “But we will welcome your feedback on the ships we see. Do tell us what you think of them.”",
        "**What kind of trouble do you expect?** “Anything short of actual Chelaxian troops on Andoran soil.” Nairaba says. “The Chelaxians have a diabolical love of intrigue.”",
        "**What have Chelaxians done before?** “What haven't they done?” Brackett grimaces. “They're not above smear campaigns, assassination attempts, soul extraction and third-party actions through cat's paws.”",
        "**Did Venture-Captain Jeggare escape the Greensteeples attack?** “Venture-Captain Jeggare is a man who's very hard to kill.” Brackett  notes. “The last I heard, he was free and currently traveling around Varisia.”",
        "**What was the Battle of Hellknight Hill?** Kitsch grins. “Andoran sent troops to liberate the Isgeri town of Breachill, which housed Citadel Altaerein, a fully staffed Hellknight fort. Fortunately, the Andoren forces caught the Hellknights with their pants down and achieved a victory.”",
        "**How long ago did this happen?** “About a month,” Brackett sighs, “one filled with icy diplomacy and ever-increasing wariness.”",
        "**Rewards:** Nairaba and Kitsch offer the PCs the following items for accompanying them: a *choker of elocution* (reloaded with the diabolic language), a set of *dragon turtle scale*, an *effervescent ampoule*, and a pair of moderate blast boots."
    ], first_line_indent=False)

    SubsectionHeaderModel("Hero Points")

    TextModel([
        "Once the PCs have finished their preparations, remind them that they each have 1 Hero Point available."
    ])


if __name__ == "__main__":
    getting_started()