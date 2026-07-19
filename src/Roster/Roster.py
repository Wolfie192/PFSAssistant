import copy

from src.Roster import Widgets
from src.Skills.SkillChecks import Skills


def calc_tier(app):
    cp = 0
    characters = app.state.get("characters", [])
    for char in characters:
        cp += char["challenge points"]

    match cp:
        case c if c >= 19:
            app.state.set("tier", "high")
        case c if c >= 16 and len(characters) <= 4:
            app.state.set("tier", "high")
        case _:
            app.state.set("tier", "low")


def roster(app):
    blank_char = {
        "name": "",
        "level": app.state.get("tier_min", 1),
        "challenge points": 2,
        "perception": 0,
        "skills": {s: 0 for s in [Skills.RELIGION.value, Skills.DEMON_LORE.value]},
    }

    if not app.state.get("characters"):
        app.state.set("characters", [copy.deepcopy(blank_char) for _ in range(2)])
    if "min_level" not in app.state:
        app.state.set("min_level", app.state.get("tier_min", 1))

    characters = app.state.get("characters", [])
    for c_idx, character in enumerate(characters):
        with app.container(border=True):
            row_1 = app.columns(4)

            with row_1[0]:
                Widgets.name(app, character, c_idx)

            with row_1[1]:
                Widgets.level(app, character, c_idx)

            with row_1[2]:
                Widgets.challenge_points(app, character, c_idx)

            with row_1[3]:
                Widgets.perception(app, character, c_idx)

            cols_per_row = 9
            skill_items = list(character["skills"].items())

            for i in range(0, len(skill_items), cols_per_row):
                row = app.columns(cols_per_row)
                for j, (skill, modifier) in enumerate(skill_items[i : i + cols_per_row]):
                    with row[j]:
                        Widgets.skill(app, skill, modifier, c_idx)

    cols = app.columns([0.2, 0.7, 0.1])

    if len(characters) < 6:
        with cols[0]:
            Widgets.add_character(app, blank_char)

    calc_tier(app)