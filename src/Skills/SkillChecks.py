from dataclasses import dataclass

import streamlit as st

from enum import Enum

from src.Text import text
from src.Skills import Widgets


class Training(Enum):
    NONE = "None"
    TRAINED = "Trained"
    EXPERT = "Expert"
    MASTER = "Master"
    LEGENDARY = "Legendary"


class Skills(Enum):
    ACROBATICS = "Acrobatics"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    CRAFTING = "Crafting"
    DECEPTION = "Deception"
    DIPLOMACY = "Diplomacy"
    INTIMIDATION = "Intimidation"
    LORE = "Lore"
    DEMON_LORE = "Demon Lore"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    OCCULTISM = "Occultism"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    RELIGION = "Religion"
    SOCIETY = "Society"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"
    THIEVERY = "Thievery"


def skill(name: Skills, low_dc: int, high_dc: int,
          training: Training = Training.NONE,
          auto_success: bool = False, auto_crit_success: bool = False):
    return {
        "name": name.value,
        "low": low_dc,
        "high": high_dc,
        "training": training,
        "auto success": auto_success,
        "auto crit success": auto_crit_success
    }


def secret_check(skills: list[dict], sid: str,
                 desc: str|list[str]|None = None,
                 crit_success_text: str|None = None, success_text: str|None = None,
                 failure_text: str|None = None, crit_failure_text: str|None = None):

    with st.expander("Secret Skill Check", expanded=True):
        if desc:
            if isinstance(desc, str):
                text(desc)
            elif isinstance(desc, list):
                for paragraph in desc:
                    text(paragraph)

        with st.container(border=True):
            headers = st.columns(6)
            headers[0].caption("Name")
            headers[1].caption("Skill")
            headers[2].caption("DC")
            headers[3].caption("Modifier")
            headers[4].caption("Roll")
            headers[5].caption("Result")


            for char in st.session_state["characters"]:
                cols = st.columns(6)

                with cols[0]:
                    Widgets.name(char.get("name"))

                with cols[1]:
                    options = list(s["name"] for s in skills)
                    Widgets.skill(char, options, sid)

                with cols[2]:
                    Widgets.dc(char, skills, sid)

                with cols[3]:
                    Widgets.modifier(char, sid)

                with cols[4]:
                    Widgets.roll(char, sid)

                with cols[5]:
                    Widgets.secret_result(char, skills, sid)

        if crit_success_text:
            st.markdown(f"**Critical Success** {crit_success_text}")
        if success_text:
            st.markdown(f"**Success** {success_text}")
        if failure_text:
            st.markdown(f"**Failure** {failure_text}")
        if crit_failure_text:
            st.markdown(f"**Critical Failure** {crit_failure_text}")


def check(skills: list[dict], sid: str,
                 desc: str|list[str]|None = None,
                 crit_success_text: str|None = None, success_text: str|None = None,
                 failure_text: str|None = None, crit_failure_text: str|None = None):

    with st.expander("Skill Check", expanded=True):
        if desc:
            if isinstance(desc, str):
                text(desc)
            elif isinstance(desc, list):
                for paragraph in desc:
                    text(paragraph)

        with st.container(border=True):
            headers = st.columns(7)
            headers[0].caption("Name")
            headers[1].caption("Skill")
            headers[2].caption("DC")
            headers[3].caption("Roll")
            headers[4].caption("Nat 20")
            headers[5].caption("Nat 1")
            headers[6].caption("Result")


            for char in st.session_state["characters"]:
                with st.container():
                    cols = st.columns(7)

                    with cols[0]:
                        Widgets.name(char.get("name"))

                    with cols[1]:
                        options = []
                        for s in skills:
                            if s["training"] != Training.NONE.value:
                                options.append(f"{s["name"]} ({s["training"]})")
                            else:
                                options.append(s["name"])
                        Widgets.skill(char, options, sid)

                    with cols[2]:
                        Widgets.dc(char, skills, sid)

                    with cols[3]:
                        Widgets.roll(char, sid)

                    with cols[4]:
                        Widgets.nat_20(char, sid)

                    with cols[5]:
                        Widgets.nat_1(char, sid)

                    with cols[6]:
                        Widgets.result(char, skills, sid)

        if crit_success_text:
            st.markdown(f"**Critical Success** {crit_success_text}")
        if success_text:
            st.markdown(f"**Success** {success_text}")
        if failure_text:
            st.markdown(f"**Failure** {failure_text}")
        if crit_failure_text:
            st.markdown(f"**Critical Failure** {crit_failure_text}")