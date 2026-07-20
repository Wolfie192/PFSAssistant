import copy


def update_character(app, c_idx, key, value):
    characters = app.state.get("characters", [])
    characters[c_idx][key] = value
    app.state.set("characters", characters)

    if key == "level":
        min_level = app.state.get("min_level", app.state.get("tier_min", 1))
        cp_map = {min_level: 2, min_level + 1: 3, min_level + 2: 4, min_level + 3: 6}
        characters[c_idx]["challenge points"] = cp_map.get(value, 2)
        app.state.set("characters", characters)


def update_skill(app, c_idx, skill_name, value):
    characters = app.state.get("characters", [])
    characters[c_idx]["skills"][skill_name] = value
    app.state.set("characters", characters)


def name(app, char: dict, idx: int):
    app.text_input(
        label="Character Name",
        value=char["name"],
        key=f"char_{idx}_name",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(app, l_idx, "name", app.session_state[f"char_{l_idx}_name"]),
    )


def level(app, char: dict, idx: int):
    app.number_input(
        label="Level",
        value=char["level"],
        min_value=app.state.get("tier_min", 1),
        max_value=app.state.get("tier_max", 20),
        key=f"char_{idx}_level",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(app, l_idx, "level", app.session_state[f"char_{l_idx}_level"]),
    )


def challenge_points(app, char: dict, idx: int):
    app.number_input(
        label="Challenge Points",
        value=char["challenge points"],
        min_value=2,
        max_value=6,
        disabled=True,
        persist_state="session",
        key=f"char_{idx}_challenge_points",
    )


def perception(app, char: dict, idx: int):
    app.number_input(
        label="Perception",
        value=char["perception"],
        key=f"char_{idx}_perception",
        persist_state="session",
        on_change=lambda l_idx=idx: update_character(app, l_idx, "perception", app.session_state[f"char_{l_idx}_perception"]),
    )


def skill(app, skill, modifier, idx: int):
    app.number_input(
        label=skill,
        value=modifier,
        key=f"char_{idx}_{skill}",
        persist_state="session",
        on_change=lambda l_idx=idx, s=skill: update_skill(app, l_idx, s, app.session_state[f"char_{l_idx}_{s}"]),
    )


def add_character(app, blank_char: dict):
    if app.button("Add Characters", icon=":material/add:"):
        characters = app.state.get("characters", [])
        characters.append(copy.deepcopy(blank_char))
        app.state.set("characters", characters)
        app.rerun()