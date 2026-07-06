import streamlit as st

from pathlib import Path

def get_root():
    return Path(__file__).resolve().parent.parent


def data_dir():
    return Path.joinpath(get_root(), "data")


def season_dir():
    return Path.joinpath(data_dir(), st.session_state.selected_season.split(":")[0].replace(" ", "_").lower())


def scenario_dir():
    return Path.joinpath(season_dir(), st.session_state.selected_scenario.split(":")[0].replace(" ", "_").lower())


def scenario_images_dir():
    return Path.joinpath(scenario_dir(), "images")


def scenario_monsters_dir():
    return Path.joinpath(scenario_dir(), "monsters")


def scenario_pages_dir():
    return Path.joinpath(scenario_dir(), "pages")


def scenario_state_path():
    return Path.joinpath(scenario_dir(), "save_state.json")