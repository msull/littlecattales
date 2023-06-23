import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import streamlit as st
from logzero import logger

from utils.cat_tales_helpers import *
from utils.chat_session import check_for_flagged_content, ChatSession
from utils.page_helpers import save_session, load_session, date_id

st.set_page_config("Little Cat Tales", layout="wide")
SESSION_DIR = os.environ["SESSION_DIR"]
saved_tales_dir = Path(SESSION_DIR) / "cat_tales" / "adventures"
saved_tales_dir.mkdir(parents=True, exist_ok=True)


def init_state():
    if "story_in_progress" not in st.session_state:
        load_session(saved_tales_dir)
        if "story_in_progress" not in st.session_state:
            start_new_story = True
        else:
            start_new_story = False

        if start_new_story:
            logger.info("Starting new story")
            session_id = date_id()
            st.session_state.story_in_progress = False
            st.session_state.session_id = session_id
            st.session_state.bad_responses = []
            st.session_state.total_tokens_used = 0
            st.session_state.num_choices_made = 0
            st.session_state.max_choices_per_story = 4
            cat1, cat2 = random.choice(CAT_NAMES)
            st.session_state.cat1name = cat1[0]
            st.session_state.cat2name = cat2[0]
            st.session_state.cat1pronouns = cat1[1]
            st.session_state.cat2pronouns = cat2[1]


def reset_state():
    logger.debug("Resetting state")
    session_id = date_id()
    st.session_state.story_in_progress = False
    st.session_state.session_id = session_id
    st.session_state.bad_responses = []
    st.session_state.total_tokens_used = 0
    st.session_state.num_choices_made = 0
    st.session_state.max_choices_per_story = 4


def get_story_prompt_view():
    common_view()
    with st.expander("Change cat names"):
        if st.button("Random selection", use_container_width=True):
            cat1, cat2 = random.choice(CAT_NAMES)
            st.session_state.cat1name = cat1[0]
            st.session_state.cat2name = cat2[0]
            st.session_state.cat1pronouns = cat1[1]
            st.session_state.cat2pronouns = cat2[1]
            st.experimental_rerun()
        st.markdown(
            "<h2 style='text-align: center;'>OR</h2>",
            unsafe_allow_html=True,
        )
        with st.form("Update cat names"):
            columns = iter(st.columns(2))
            with next(columns):
                cat1name = st.text_input("Cat 1", st.session_state.cat1name)
            with next(columns):
                cat2name = st.text_input("Cat 2", st.session_state.cat2name)

            # cat pronoun selection
            pronoun_options = ("He/Him", "She/Her", "They/Them")
            columns = iter(st.columns(4))
            next(columns)  # throw the first one away for formatting
            with next(columns):
                cat1pronouns = st.selectbox(
                    "cat1pronouns",
                    pronoun_options,
                    pronoun_options.index(st.session_state.cat1pronouns),
                    label_visibility="collapsed",
                )
            with next(columns):
                cat2pronouns = st.selectbox(
                    "cat2pronouns",
                    pronoun_options,
                    pronoun_options.index(st.session_state.cat2pronouns),
                    label_visibility="collapsed",
                )

            if st.form_submit_button(use_container_width=True):
                logger.info(f"New cat names {cat1name=} {cat2name=}")
                check_for_flagged_content(f"{cat1name} {cat2name}")
                st.session_state.cat1name = cat1name
                st.session_state.cat2name = cat2name
                st.session_state.cat1pronouns = cat1pronouns
                st.session_state.cat2pronouns = cat2pronouns
                st.experimental_rerun()

    st.markdown(add_cat_names(USER_INTRO_TEXT))

    if "random_story_idea" not in st.session_state:
        st.session_state.random_story_idea = ""

    if st.button("Get a random story prompt"):
        st.session_state.random_story_idea = add_cat_names(random.choice(STORY_IDEAS))

    with st.form("prompt-form", clear_on_submit=True):
        prompt = st.text_area(
            "Input your story idea", value=st.session_state.random_story_idea
        )
        if st.form_submit_button("Begin the story"):
            check_for_flagged_content(prompt)
            chat_session = ChatSession()
            chat_session.user_says(prompt)
            st.session_state.chat_history = chat_session.history
            st.session_state.story_in_progress = True
            generate_story_page()


@dataclass
class ResponseWithChoices:
    choice1: str
    choice2: str

    content: str  # cleaned response without choices


def _extract_choices(content: str) -> ResponseWithChoices:
    """Extract choices from the message; return the cleaned string without those cmds."""
    choice1 = ""
    choice2 = ""
    remove_lines = []
    for line in content.splitlines():
        if "CHOICE1" in line:
            breakpoint()
        if line.startswith("CHOICE 1: "):
            choice1 = line.removeprefix("CHOICE 1: ")
            remove_lines.append(line)
        elif line.startswith("CHOICE 2: "):
            choice2 = line.removeprefix("CHOICE 2: ")
            remove_lines.append(line)

    for line in remove_lines:
        content = content.replace(line, "")
    content = content.replace("\n\n\n", "\n\n").strip()

    return ResponseWithChoices(choice1=choice1, choice2=choice2, content=content)


def generate_story_page(spinner_msg: Optional[str] = None, expect_more_choices=True):
    chat_session = ChatSession(history=st.session_state.chat_history)

    if not spinner_msg:
        spinner_msg = add_cat_names(random.choice(SPINNER_MSGS))

    with st.spinner(spinner_msg):
        got_valid_response = False
        attempts = 0
        max_attempts = 3
        while not got_valid_response:
            logger.info("Generating AI Response for story")
            attempts += 1
            if expect_more_choices:
                reinforce_with = add_cat_names(AI_REINFORCEMENT_MSG)
            else:
                reinforce_with = ""
            response = chat_session.get_ai_response(
                initial_system_msg=add_cat_names(AI_ASSISTANT_MSG),
                reinforcement_system_msg=reinforce_with,
            )
            logger.debug(response)
            st.session_state.total_tokens_used += response["usage"]["total_tokens"]
            try:
                choices = _extract_choices(response["choices"][0]["message"]["content"])
                if expect_more_choices and not (choices.choice1 and choices.choice2):
                    logger.warning("Bad response -- did not find expected choices")
                    raise ValueError()
                elif not expect_more_choices and (choices.choice1 or choices.choice2):
                    logger.warning("Bad response -- found unexpected choices")
                    raise ValueError()
                break
            except Exception:
                st.session_state.chat_history = chat_session.history
                logger.info("Got bad response, trying again")
                st.session_state.bad_responses.append(response)

                if attempts >= max_attempts:
                    logger.info("Out of attempts")
                    st.error(
                        "Encountered an error generating your story, sorry about that"
                    )
                    return
    chat_session.assistant_says(response["choices"][0]["message"]["content"])
    st.session_state.chat_history = chat_session.history
    save_session(saved_tales_dir)
    st.experimental_rerun()


def main_view():
    common_view()
    with st.expander("Intro"):
        st.markdown(add_cat_names(USER_INTRO_TEXT))

    chat_session = ChatSession(history=st.session_state.chat_history)

    st.subheader("Prompt: " + chat_session.history[0]["content"])

    choices = None
    for msg in chat_session.history[1:]:
        if msg["role"] == "assistant":
            choices = _extract_choices(msg["content"])
            st.write(choices.content)
        elif msg["role"] == "user":
            st.write(
                f"<div style='color: green;'> &gt; {msg['content']}</div>",
                unsafe_allow_html=True,
            )
    # last choices we receive are the current ones:
    if choices.choice1 and choices.choice2:
        with st.form("prompt-form"):
            story_choice = st.radio("Which option?", (choices.choice1, choices.choice2))
            if st.form_submit_button("Choose"):
                chat_session.user_says(story_choice)
                st.session_state.num_choices_made += 1
                # st.session_state.num_choices_made = 0
                # st.session_state.max_choices_per_story = 4
                remaining = (
                    st.session_state.max_choices_per_story
                    - st.session_state.num_choices_made
                )
                expect_more = True
                if remaining > 0:
                    s = "" if remaining == 1 else "s"
                    system_msg = f"Conclude the story after {remaining} more choice{s} from the user."
                else:
                    expect_more = False
                    system_msg = "The user has no choices remaining; conclude the story with your response"
                chat_session.system_says(system_msg)
                st.session_state.chat_history = chat_session.history
                save_session(saved_tales_dir)
                generate_story_page(expect_more_choices=expect_more)
    else:  # no more choices, story is over
        _, c1, _ = st.columns(3)
        link = f"[Link to this story](?s={st.session_state.session_id})"
        c1.subheader(link)
        del c1
        if st.button("Start Over", use_container_width=True, type="primary"):
            st.experimental_set_query_params(s="")
            reset_state()
            st.experimental_rerun()
        return


def common_view():
    st.header(add_cat_names(HEADER_TEXT))


def add_cat_names(input: str) -> str:
    substitutions = {
        "CAT_NAME1": st.session_state.cat1name,
        "CAT_NAME2": st.session_state.cat2name,
        "CAT1HE": _he(st.session_state.cat1pronouns),
        "CAT2HE": _he(st.session_state.cat2pronouns),
        "CAT1HIM": _him(st.session_state.cat1pronouns),
        "CAT2HIM": _him(st.session_state.cat2pronouns),
        "CAT1HIS": _his(st.session_state.cat1pronouns),
        "CAT2HIS": _his(st.session_state.cat2pronouns),
        "CAT1BROTHER": _brother(st.session_state.cat1pronouns),
        "CAT2BROTHER": _brother(st.session_state.cat2pronouns),
    }
    if substitutions["CAT1BROTHER"] != substitutions["CAT2BROTHER"]:
        substitutions["BROTHER"] = "sibling"
    else:
        substitutions["BROTHER"] = substitutions["CAT1BROTHER"]
    return input.format(**substitutions)


def _he(pronoun_val):
    if pronoun_val == "He/Him":
        return "he"
    elif pronoun_val == "She/Her":
        return "she"
    elif pronoun_val == "They/Them":
        return "they"
    raise ValueError("Unknown value")


def _his(pronoun_val):
    if pronoun_val == "He/Him":
        return "his"
    elif pronoun_val == "She/Her":
        return "her"
    elif pronoun_val == "They/Them":
        return "their"
    raise ValueError("Unknown value")


def _him(pronoun_val):
    if pronoun_val == "He/Him":
        return "him"
    elif pronoun_val == "She/Her":
        return "her"
    elif pronoun_val == "They/Them":
        return "them"
    raise ValueError("Unknown value")


def _brother(pronoun_val):
    if pronoun_val == "He/Him":
        return "brother"
    elif pronoun_val == "She/Her":
        return "sister"
    elif pronoun_val == "They/Them":
        return "sibling"
    raise ValueError("Unknown value")


init_state()
if not st.session_state.story_in_progress:
    get_story_prompt_view()
else:
    main_view()

with st.expander("Session State"):
    st.write(st.session_state)
