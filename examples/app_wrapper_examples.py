import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfsassistant import PFSAssistantStreamlitApp


app = PFSAssistantStreamlitApp()


def render_roster_workflow():
    app.state.ensure("characters", [])
    app.section_header("Roster")

    if app.button("Add character"):
        app.state.set("characters", app.state.get("characters") + [{"name": "", "level": 1}])

    for character in app.state.get("characters"):
        app.text(character.get("name", "Unnamed"))


def render_skill_workflow():
    app.state.ensure("tier", "low")
    app.subsection_header("Skill Checks")

    if app.button("Roll skill"):
        app.text("A skill check would be resolved here.")


def render_scenario_workflow():
    app.state.ensure("season", "Season 5")
    app.state.ensure("scenario", "Scenario 19")

    app.text(f"Season: {app.state.get('season')}")
    app.text(f"Scenario: {app.state.get('scenario')}")


render_roster_workflow()
render_skill_workflow()
render_scenario_workflow()
