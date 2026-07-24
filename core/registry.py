from typing import Dict, List
from core import models, enums

class CampaignRegistry:
    def __init__(self):
        self._seasons: Dict[int, models.Season] = {}
        self._load_official_registry()

    def _load_official_registry(self):
        quests = models.Season(id=0, name="Quests")
        quests.scenarios = [
            models.Scenario(
                id=1,
                name="The Sandstone Secret",
                tier=(1, 4)
            ),
            models.Scenario(
                id=2,
                name="Unforgiving Fire",
                tier=(1, 4)
            ),
            models.Scenario(
                id=3,
                name="Grehunde's Gorget",
                tier=(1, 4)
            ),
            models.Scenario(
                id=4,
                name="Port Peril Pub Crawl",
                tier=(1, 4)
            ),
            models.Scenario(
                id=5,
                name="The Dragon Who Stole Evoking Day",
                tier=(3, 6)
            ),
            models.Scenario(
                id=6,
                name="Archaeology in Aspenthar",
                tier=(1, 4)
            ),
            models.Scenario(
                id=7,
                name="A Curious Claim",
                tier=(3, 6)
            ),
            models.Scenario(
                id=8,
                name="Shadows of the Black Sovereign",
                tier=(3, 6)
            ),
            models.Scenario(
                id=9,
                name="Wayfinder Origins",
                tier=(3, 6)
            ),
            models.Scenario(
                id=10,
                name="The Broken Scales",
                tier=(1, 4)
            ),
            models.Scenario(
                id=11,
                name="A Parchment Tree",
                tier=(1, 4)
            ),
            models.Scenario(
                id=12,
                name="Putrid Seeds",
                tier=(3, 6)
            ),
            models.Scenario(
                id=13,
                name="Falcon's Descent",
                tier=(1, 4)
            ),
            models.Scenario(
                id=14,
                name="The Swordlord's Challenge",
                tier=(1, 4)
            ),
            models.Scenario(
                id=15,
                name="In the Footsteps of Horror",
                tier=(1, 4)
            ),
            models.Scenario(
                id=16,
                name="The Winter Queen's Dollhouse",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            ),
            models.Scenario(
                id=17,
                name="Escorting a Mirage",
                tier=(1, 4)
            ),
            models.Scenario(
                id=18,
                name="Student Exchange",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            ),
            models.Scenario(
                id=19,
                name="The Elsewhere Feast",
                tier=(1, 4)
            ),
            models.Scenario(
                id=20,
                name="The Dacilane's Academy's Show Must Go On",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            ),
            models.Scenario(
                id=21,
                name="Infernal Infiltration",
                tier=(1, 4)
            ),
            models.Scenario(
                id=22,
                name="Friends In Need",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            ),
            models.Scenario(
                id=23,
                name="Lacking Respect",
                tier=(1, 4)
            ),
            models.Scenario(
                id=24,
                name="Tanuki Trouble",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            )
        ]
        self._seasons[0] = quests

        season_1 = models.Season(id=1, name="Year of the Open Road")
        season_1.scenarios = [
            models.Scenario(
                id=0,
                name="Origin of the Open Road",
                tier=(5, 5)
            ),
            models.Scenario(
                id=1,
                name="The Absalom Initiation",
                tier=(1, 4)
            ),
            models.Scenario(
                id=2,
                name="The Mosquito Witch",
                tier=(1, 4)
            ),
            models.Scenario(
                id=3,
                name="Escaping the Grave",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=4,
                name="Bandits of Immenwood",
                tier=(1, 4),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=5,
                name="Trailblazer's Bounty",
                tier=(1, 4),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=6,
                name="Lost on the Spirit Road",
                tier=(1, 4)
            ),
            models.Scenario(
                id=7,
                name="Flooded King's Court",
                tier=(1, 4),
                tags=[enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=8,
                name="Revolution on the Riverside",
                tier=(1, 4)
            ),
            models.Scenario(
                id=9,
                name="Star-Crossed Voyages",
                tier=(3, 6),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=10,
                name="Tarnbreaker's Trail",
                tier=(1, 4)
            ),
            models.Scenario(
                id=11,
                name="Flames of Rebellion",
                tier=(1, 4)
            ),
            models.Scenario(
                id=12,
                name="Burden of Envy",
                tier=(1, 4),
                tags=[enums.ScenarioTag.RADIANT_OATH]
            ),
            models.Scenario(
                id=13,
                name="Devil at the Crossroads",
                tier=(3, 6),
                tags=[enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=14,
                name="Lions of Katapesh",
                tier=(1, 4)
            ),
            models.Scenario(
                id=15,
                name="The Blooming Catastrophe",
                tier=(1, 4),
                tags=[enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=16,
                name="The Perennial Crown Part 1: Opal of Bhopan",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=17,
                name="The Perennial Crown Part 2: The Thorned Monarch",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=18,
                name="Lodge of the Living God",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=19,
                name="Iolite Squad Alpha",
                tier=(3, 6)
            ),
            models.Scenario(
                id=20,
                name="The Lost Legend",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=21,
                name="Mistress of the Maze",
                tier=(1, 4)
            ),
            models.Scenario(
                id=22,
                name="Doom of Cassomir",
                tier=(1, 4)
            ),
            models.Scenario(
                id=23,
                name="Star-Crossed Court",
                tier=(3, 6)
            ),
            models.Scenario(
                id=24,
                name="Lightning Strikes, Stars Fall",
                tier=(5, 8)
            ),
            models.Scenario(
                id=25,
                name="Grim Symphony",
                tier=(5, 8), tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            )
        ]
        self._seasons[1] = season_1

        season_2 = models.Season(id=2, name="Year of Corruption's Reach")
        season_2.scenarios = [
            models.Scenario(
                id=0,
                name="King in Thorns",
                tier=(1, 8),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=1,
                name="Citadel of Corruption",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="Mountain of Sea and Sky",
                tier=(3, 6),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=3,
                name="Catastrophe's Spark",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=4,
                name="Path of Kings",
                tier=(3, 6),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=5,
                name="Balancing the Scales",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=6,
                name="The Crashing Wave",
                tier=(3, 6)
            ),
            models.Scenario(
                id=7,
                name="The Blakros Deception",
                tier=(5, 8),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=8,
                name="A Frosty Mug",
                tier=(5, 8),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=9,
                name="The Seven Secrets of Dacilane Academy",
                tier=(1, 4)
            ),
            models.Scenario(
                id=10,
                name= "In Burning Dawn",
                tier=(5, 8),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=11,
                name= "The Pathfinder Trials",
                tier=(1, 1)
            ),
            models.Scenario(
                id=12,
                name= "Snakes in the Grass",
                tier=(3, 6)
            ),
            models.Scenario(
                id=13,
                name="A Gilded Test",
                tier=(1, 4)
            ),
            models.Scenario(
                id=14,
                name="Lost in Flames",
                tier=(3, 6),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=15,
                name="A Dirge for Sarkoris",
                tier=(3, 6)
            ),
            models.Scenario(
                id=16,
                name= "Freedom for Wishes",
                tier=(5, 8)
            ),
            models.Scenario(
                id=17,
                name="Lost Maid of Anactoria",
                tier=(3, 6)
            ),
            models.Scenario(
                id=18,
                name="The Fanciful March of Urwal",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=19,
                name="Enter the Pallid Peak",
                tier=(1, 4)
            ),
            models.Scenario(
                id=20,
                name="Breaking the Storm: Bastion in Embers",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=21,
                name="In Pursuit of Water",
                tier=(1, 4)
            ),
            models.Scenario(
                id=22,
                name="Breaking the Storm: Excising Ruination",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=23,
                name="An Agent's Obligation",
                tier=(3, 6)
            ),
            models.Scenario(
                id=24,
                name="Breaking the Storm: Parting Clouds",
                tier=(7, 10),
                tags=[enums.ScenarioTag.GLYPH, enums.ScenarioTag.METAPLOT]
            )
        ]
        self._seasons[2] = season_2

        season_3 = models.Season(id=3, name="Year of Shattered Sanctuaries")
        season_3.scenarios = [
            models.Scenario(
                id=1,
                name="Intro: Year of Shattered Sanctuaries",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="The East Hill Haunting",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=3,
                name="Echoes of Desperation",
                tier=(3, 6)
            ),
            models.Scenario(
                id=4,
                name="The Devil-Wrought Disappearance",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=5,
                name="Inheritor's Rite",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=6,
                name="Struck by Shadows",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=7,
                name="The Locked Lodge",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=8,
                name="Foundation's Price",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=9,
                name="The Secluded Siege",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=10,
                name="Delve the Pallid Depths",
                tier=(1, 4)
            ),
            models.Scenario(
                id=11,
                name="No Time for Treason",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=12,
                name="Fury's Toll",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=13,
                name="Guardian's Covenant",
                tier=(3, 6)
            ),
            models.Scenario(
                id=14,
                name="The Tomb Between Worlds",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.HORIZON_HUNTERS, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=15,
                name="Cavern of the Sundered Song",
                tier=(9, 12),
                tags=[enums.ScenarioTag.GLYPH, enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=16,
                name="Escape from Oppara",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=17,
                name="Dreams of a Dustbound Isle",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.RADIANT_OATH, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=18,
                name="Dacilane Academy's Delightful Disaster",
                tier=(1, 4)
            ),
            models.Scenario(
                id=19,
                name="Mean Streets of Shadow Absalom",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=98,
                name="Expedition Into Pallid Peril",
                tier=(1, 6),
                tags=[enums.ScenarioTag.EXCLUSIVE, enums.ScenarioTag.GLYPH]
            ),
            models.Scenario(
                id=99,
                name="Fate in the Future",
                tier=(1, 8),
                tags=[enums.ScenarioTag.EXCLUSIVE, enums.ScenarioTag.GLYPH]
            ),
        ]
        self._seasons[3] = season_3

        season_4 = models.Season(id=4, name="Year of Boundless Wonder")
        season_4.scenarios = [
            models.Scenario(
                id=1,
                name="Intro: Year of Boundless Wonder",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="Return to the Grave",
                tier=(1, 4),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS, enums.ScenarioTag.RADIANT_OATH]
            ),
            models.Scenario(
                id=3,
                name="Linnorm's Legacy",
                tier=(5, 8),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=4,
                name="To Seek the Heart of Calamity",
                tier=(3, 6),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=5,
                name="The Arclord Who Never Was",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=6,
                name="Signal from the Electric Laboratory",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.HORIZON_HUNTERS, enums.ScenarioTag.RADIANT_OATH]
            ),
            models.Scenario(
                id=7,
                name="A Most Wondrous Exchange!",
                tier=(5, 8)
            ),
            models.Scenario(
                id=8,
                name="Battle for Star's Fate",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=9,
                name="Killer in the Golden Mask",
                tier=(5, 8),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=10,
                name="Arclord's Abode",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=11,
                name="Prisoners of the Electric Castle",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=12,
                name="Negotiations for the Star Gun",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=13,
                name="Within the Prairies",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=14,
                name="Shattering Golden Chains",
                tier=(3, 6),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=15,
                name="In Glorious Battle",
                tier=(9, 12),
                tags=[enums.ScenarioTag.GLYPH]
            ),
            models.Scenario(
                id=16,
                name="Dacilane Academy's First Great Prank War",
                tier=(3, 6)
            ),
            models.Scenario(
                id=17,
                name="Trapping the Hag's Claw",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT]
            )
        ]
        self._seasons[4] = season_4

        season_5 = models.Season(id=5, name="Year of Unfettered Exploration")
        season_5.scenarios = [
            models.Scenario(
                id=1,
                name="Intro: Year of Unfettered Exploration",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE]
            ),
            models.Scenario(
                id=2,
                name="The Blackwood Lost",
                tier=(3, 6),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=3,
                name="Heidmarch Heist",
                tier=(5, 8)
            ),
            models.Scenario(
                id=4,
                name="Equal Exchanges - Necessary Introductions",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=5,
                name="The Island of the Vibrant Dead",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=6,
                name="Ukuja, The First Wall",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.HORIZON_HUNTERS, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=7,
                name="Sewer Dragon Crisis",
                tier=(1, 4),
                tags=[enums.ScenarioTag.RADIANT_OATH]
            ),
            models.Scenario(
                id=8,
                name="Protecting the Firelight",
                tier=(5, 8)
            ),
            models.Scenario(
                id=9,
                name="Equal Exchanges - Skymetal Hoard",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=10,
                name="The Crocodile's Smile",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=11,
                name="Equal Exchanges - The Hidden Current",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.RADIANT_OATH, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=12,
                name="Mischief in the Maze",
                tier=(1, 4)
            ),
            models.Scenario(
                id=13,
                name="Thick as Thieves",
                tier=(5, 8)
            ),
            models.Scenario(
                id=14,
                name="Poisonous Council",
                tier=(3, 6),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=15,
                name="Cleansing the Flame",
                tier=(5, 8)
            ),
            models.Scenario(
                id=16,
                name="A Lie Told to Strangers",
                tier=(3, 6),
                tags=[enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=17,
                name="Stranded on Yesterday's Tide",
                tier=(1, 4),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=18,
                name="Tapestry of the Mind",
                tier=(9, 12),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=19,
                name="Demonic Afterparty",
                tier=(3, 6)
            ),
            models.Scenario(
                id=20,
                name="The Rakshasa's Court",
                tier=(7, 10)
            )
        ]
        self._seasons[5] = season_5

        season_6 = models.Season(id=6, name="Year of Immortal Influence")
        season_6.scenarios = [
            models.Scenario(
                id=0,
                name="Salt of the Ocean",
                tier=(1, 8),
                tags=[enums.ScenarioTag.EXCLUSIVE]
            ),
            models.Scenario(
                id=1,
                name="Intro to the Year of Immortal Influence",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="Rain Falls on the Mountain of Sea and Sky",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=3,
                name="Godsrain in a Godless Land",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=4,
                name="An Enkindled Carnival",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=5,
                name="Silver Bark, Golden Blades",
                tier=(1, 4)
            ),
            models.Scenario(
                id=6,
                name="Rotten Apples",
                tier=(3, 6),
                tags=[enums.ScenarioTag.RADIANT_OATH, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=7,
                name="A God Falls Where Magic Fails",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=8,
                name="Upon Wheels and Rime",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ALL_AGES]
            ),
            models.Scenario(
                id=9,
                name="The Power of Legends",
                tier=(9, 12),
                tags=[enums.ScenarioTag.GLYPH, enums.ScenarioTag.METAPLOT, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=10,
                name="Once in Whispers",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=11,
                name="The Godsrain and the Dragon",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=12,
                name="The Burning of Greensteeples",
                tier=(3, 6),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.RADIANT_OATH]
            ),
            models.Scenario(
                id=13,
                name="All That Glitters",
                tier=(1, 4),
                tags=[enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=14,
                name="Twice in Steel",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.RADIANT_OATH, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=15,
                name="Lost and Forgotten",
                tier=(5, 8),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=16,
                name="The Heart of the City",
                tier=(5, 8),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=17,
                name="The Devil in the Details",
                tier=(7, 10),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=18,
                name="Symposium on a Fallen God",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=19,
                name="What Walks Again",
                tier=(11, 14),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.GLYPH, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=20,
                name="The Overthrow of Ambition",
                tier=(9, 12),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.GLYPH]
            )
        ]
        self._seasons[6] = season_6

        season_7 = models.Season(id=7, name="Year of Battle's Spark")
        season_7.scenarios = [
            models.Scenario(
                id=1,
                name="Enough is Enough",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="Shipyard Sabotage",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=3,
                name="A Foot in the Door",
                tier=(5, 8)
            ),
            models.Scenario(
                id=4,
                name="Sulfuric Negotiations",
                tier=(3, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=5,
                name="Battle of the Thorns",
                tier=(9, 12),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=6,
                name="Brastlewark at War Part 1: The Gnome Defection",
                tier=(1, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=7,
                name="Draconic Folly",
                tier=(7, 10)
            ),
            models.Scenario(
                id=8,
                name="The Haunted Corridor",
                tier=(1, 4),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE]
            ),
            models.Scenario(
                id=9,
                name="The Chitterwood Walks, Part 1: Scrambling the Tribes",
                tier=(3, 4),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.ENVOYS_ALLIANCE, enums.ScenarioTag.VERDANT_WHEEL]
            ),
            models.Scenario(
                id=10,
                name="Shattered Blades",
                tier=(13, 14),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=11,
                name="The Darkness Within",
                tier=(7, 8),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=12,
                name="The Chitterwood Walks, Part 2: The Battle of Logas",
                tier=(5, 6),
                tags=[enums.ScenarioTag.METAPLOT, enums.ScenarioTag.RADIANT_OATH, enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=13,
                name="Ancient Beyond Imagining",
                tier=(9, 10),
                tags=[enums.ScenarioTag.VIGILANT_SEAL]
            ),
            models.Scenario(
                id=14,
                name="Brastlewark at War, Part 2: The Gnome Liberation",
                tier=(3, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=15,
                name="Within Antiquated Halls",
                tier=(7, 8),
                tags=[enums.ScenarioTag.HORIZON_HUNTERS]
            ),
            models.Scenario(
                id=16,
                name="A Star's Journey",
                tier=(1, 2)
            ),
            models.Scenario(
                id=17,
                name="Perch of Liberty",
                tier=(3, 4),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=18,
                name="Freedom on the Sea",
                tier=(5, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=19,
                name="The Lost Legacy",
                tier=(7, 8)
            ),
            models.Scenario(
                id=20,
                name="The Strings of Hell",
                tier=(1, 2),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=21,
                name="The Home of Empty Breath",
                tier=(5, 6),
                tags=[enums.ScenarioTag.GRAND_ARCHIVE, enums.ScenarioTag.RADIANT_OATH]
            )
        ]
        self._seasons[7] = season_7

        season_8 = models.Season(id=8, name="Year of Clockwork Mystery")
        season_8.scenarios = [
            models.Scenario(
                id=1,
                name="Intro to the Year of Clockwork Mystery",
                tier=(1, 2),
                tags=[enums.ScenarioTag.METAPLOT]
            ),
            models.Scenario(
                id=2,
                name="The Fey Reclamation",
                tier=(3, 4)
            ),
            models.Scenario(
                id=3,
                name="For the Love of Vanity",
                tier=(5, 6)
            ),
            models.Scenario(
                id=4,
                name="A Theft in Riddleport",
                tier=(1, 2)
            ),
            models.Scenario(
                id=5,
                name="A Shark's Guide to Piracy",
                tier=(1, 2)
            ),
            models.Scenario(
                id=6,
                name="Falling Sparks",
                tier=(5, 6)
            ),
            models.Scenario(
                id=7,
                name="In the Halls of Dead Justice",
                tier=(7, 8)
            ),
            models.Scenario(
                id=8,
                name="Treatise on the Study of Clockwork",
                tier=(5, 6),
                tags=[enums.ScenarioTag.METAPLOT]
            )
        ]
        self._seasons[8] = season_8

    def get_seasons(self) -> List[models.Season]:
        return list(self._seasons.values())

    def get_season_by_number(self, season_num: int) -> models.Season:
        return self._seasons[season_num]

    def get_scenarios_for_season(self, season_num: int, include_dev: bool = False) -> List[models.Scenario]:
        season = self._seasons.get(season_num)
        if not season:
            return []
        if include_dev:
            return season.scenarios
        return [s for s in season.scenarios if s.data]