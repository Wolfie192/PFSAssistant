import streamlit as st

from src.ImageModel import Image
from src.SkillCheckModel import SkillCheck
from src.TextModel import Text
from src.SkillModel import Skill


def touring_the_shipyards():
    cols = st.columns(2)

    with cols[0]:
        Text([
            "As soon as the PCs are ready, Kitsch rubs her paws together. “Enough talking! Let’s go shopping!”",
            "“Remember, we would like your honest opinion on all the ships you see,” Nairaba says gently. “It’s important to have multiple opinions when we’re considering a purchase as large as a ship.”",
            "Nairaba and Kitsch lead the way down the five blocks from the Brine Shark’s Bistro, down a steep incline to the dockside office of **Olad the Alright Shipwright** (overzealous male halfling salesman). Soon, the sounds of the Shipyard district grow more raucous. Gangs of workers sing Consortium lumberjack chants as they haul timber, and a cacophony of saws and hammers fills the air as craftsmen put together hulls in the dry docks. Augustana is sultry in summer; Nairaba and Kitsch fan themselves but heat radiates off the streets. The occasional cool breeze blowing off the Great Salt Harbor brings some relief not just from the heat, but from the mingling smells of sweat, sawdust, oil, and tar.",
            "Olad greets that Pathfinder delegation as if they were long lost friends, pumping their hands (or claws, or whatever the party has for appendages) and expressing his joy in meeting them all. “Buying ships for a navy, yes? Why then, you’ll be needing lots of ships! Small ships! Tall ships! So many ships, and Trustworthy Olad has them all for you!”",
            "Olad takes the party on a tour of substandard ships. A PC who makes a successful DC 15 Perception check to Sense Motive quickly realizes that Olad is viewing their delegation as a golden opportunity to offload the worst of his inventory on a bunch of moneyed landlubbers. PCs who want to help assess the ships can do so with a successful DC 13 Warfare or sailing-related Lore to Recall Knowledge, a DC 15 Crafting check to Recall Knowledge or DC 17 Perception check to Seek (for levels 3–4 increase each DC by 2). Encourage the PCs to do an assessment for each ship and have Nairaba ask their opinions if they forget to tell him."
        ])

    with cols[1]:
        Image("Olad", width=400)

    Text([
        "**The Pert Peach** is a squat, mid-sized ship painted in gaudy colors and replete with the eye-watering scent of perfume belowdeck. Olad gestures expansively on the ship tour. “This pre-owned beauty is one we’re refurbishing! In addition to an excellent galley, there are so many private rooms, useful for storage!” A PC who makes a successful assessment of the ship realizes that while it would make a great passenger or hospital vessel, the ship is much too slow and unwieldy for the rapid transportation the Society often needs."
    ])

    SkillCheck("Recall Knowledge on The Pert Peach",
                    [
                        Skill("Warfare Lore", 13, 15),
                        Skill("Sailing Related Lore", 13, 15),
                        Skill("Crafting", 15, 17),
                        Skill("Perception", 17, 19)
                    ], model_id="touring_the_shipyard_pert_peach_recall_knowledge")

    Text([
        "The Scurvy Scamp is a lean, two-masted brig. “Okay, so you want fast, you want lean, you want this ship! She’s fast and can be used for discreet merchandise,” Olad pauses to wink at Nairaba and Kitsch, “or for stealthy drops of soldiers on an enemy coast.” The Scurvy Scamp is indeed seaworthy and fast, but a PC who makes a successful assessment of the ship realizes that its rudder is in terrible repair and needs replacement. If the price was reduced for the bad rudder, it might be something the Pathfinder Society could fix in a few weeks."
    ])

    SkillCheck("Recall Knowledge on The Scurvy Scamp",
                    [
                        Skill("Warfare Lore", 13, 15),
                        Skill("Sailing Related Lore", 13, 15),
                        Skill("Crafting", 15, 17),
                        Skill("Perception", 17, 19)
                    ], model_id="touring_the_shipyard_scurvy_scamp_recall_knowledge")

    Text([
        "As the players travel to the third ship, aimless sailors wander around the dock area of the shipyard. Some have opened a crate of Sauerton Red and are passing bottles around. The sailors sit on the docks, drinking and watching the nearby ships. Olad detours around a pair of sailors who are stretched out on the dock and then complains, “Those louts are getting in the way of honest work.” He turns to the sailors and shakes a fist. “Hey! We’re trying to work here! Move on!” but the sailors shrug and ignore him. A PC making a successful DC 15 check to Sense Motive might realize that this is unusual behavior for sailors off-duty. Why are they hanging around a busy shipyard instead of enjoying the nearby bars and entertainment a few blocks away?"
    ])

    SkillCheck("Sense Motive on sailors",
                    [
                        Skill("Perception", 15, 17)
                    ], model_id="touring_the_shipyard_sense_motive_sailors")

    Text([
        "The Lucky Duck is a full-rigged ship with three tall masts. There are recently repaired battle scars on the hull. PCs making a successful DC 13 Perception check to Seek hear squeaking and scurrying noises, and if their check meets or exceeds a DC 18, they spot rats running along the floor, including one that runs directly over Olad’s bare foot, though Olad pretends to make no notice of this. “This ship may need a good scrub down and a little love, but she can carry a lot of personnel and has the space for 50 cannons onboard.” A PC who makes a successful assessment of this ship realizes that this vessel, despite its very prevalent rat problem, is ready now and would serve the Pathfinder fleet just fine."
    ])

    SkillCheck("Seek at The Lucky Duck",
                    [
                        Skill("Perception", 13, 15)
                    ], model_id="touring_the_shipyard_seek_the_lucky_duck")

    SkillCheck("Notice rats at The Lucky Duck",
                    [
                        Skill("Perception", 18, 20)
                    ], model_id="touring_the_shipyard_notice_rats_the_lucky_duck")

    SkillCheck("Recall Knowledge on The Lucky Duck",
                    [
                        Skill("Warfare Lore", 13, 15),
                        Skill("Sailing Related Lore", 13, 15),
                        Skill("Crafting", 15, 17),
                        Skill("Perception", 17, 19)
                    ], model_id="touring_the_shipyard_recall_knowledge_lucky_duck")


if __name__ == "__main__":
    touring_the_shipyards()