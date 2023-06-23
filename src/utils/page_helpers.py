import json
from pathlib import Path

import streamlit as st
import random
from datetime import datetime
from string import ascii_lowercase
from typing import Callable, List, Optional, Union


def item_paginator(
    title: str,
    items: Union[int, List[str]],
    item_handler_fn: Callable,
    item_actions: Optional[dict] = None,
    display_item_names=False,
    enable_keypress_nav=False,
    st=None,
):
    """
    This function implements a paginator for items in a Streamlit application.

    Args:
        title (str): The title of the paginator, displayed at the top.
        items (Union[int, List[str]]): If an integer is provided, it denotes the total number of items.
            If a list of strings is provided, each string is considered an item and its length denotes the
            total number of items.
        item_handler_fn (Callable): A function called to handle displaying the current item. This function should
            accept an integer as an argument, representing the current item's index.
        item_actions (Optional[dict]): An optional dictionary of actions that can be applied to the current item.
            The keys of the dictionary should be the names of the actions, and the values should be functions
            that accept the current item's index as an argument. If this argument is not provided, the paginator
            will not display any actions.
        display_item_names (bool, optional): If set to True, item names will be displayed in the selection dropdown
            instead of indices when items is a list of strings. If items is an integer, setting this to True will
            raise a ValueError. Defaults to False.
        enable_keypress_nav (bool, optional): If set to True, enables left and right key navigation to go to the
            previous or next item, respectively. Defaults to False.
    """
    if not st:
        import streamlit as st

    item_num_var = f"ItemPaginator:{title}#item_num"
    if item_num_var not in st.session_state:
        st.session_state[item_num_var] = 0

    st.markdown(f"<h3 style='text-align: center'>{title}</h3>", unsafe_allow_html=True)
    if display_item_names:
        c1, c2, c3, c4, c6, c7 = st.columns((2, 2, 1, 3, 3, 2))
        c5 = None
    else:
        c1, c2, c3, c4, c5, c6, c7 = st.columns((2, 2, 1, 3, 1, 2, 2))
    if isinstance(items, int):
        if display_item_names:
            raise ValueError("Cannot set display_item_names=True when passing an integer for items")
    item_count = items if isinstance(items, int) else len(items)

    if st.session_state[item_num_var] > item_count - 1:
        st.session_state[item_num_var] = item_count - 1

    if st.session_state[item_num_var] < 0:
        st.session_state[item_num_var] = 0



    if not item_count:
        st.write("No items to display")
        return

    def decrement_item_index():
        st.session_state[item_num_var] = max(0, st.session_state[item_num_var] - 1)

    def set_item_index(item_num: int):
        st.session_state[item_num_var] = item_num

    c1.button(
        "Prev",
        on_click=decrement_item_index,
        key=f"ItemPaginator:{title}#Previous_btn",
        use_container_width=True,
    )

    if item_actions:
        with c2:
            selected_action = st.selectbox("select-item-action", sorted(item_actions), label_visibility="collapsed")

        if c3.button("Go", use_container_width=True, key=f"ItemPaginator:{title}#Go_btn") and selected_action:
            item_actions[selected_action](st.session_state[item_num_var])
            st.experimental_rerun()

    c4.markdown(
        f"<div style='text-align: center'>Viewing {st.session_state[item_num_var] + 1} of {item_count}</div>",
        unsafe_allow_html=True,
    )
    # hide the "Goto" label when displaying item labels in the select box, to give it more room to display
    if not display_item_names:
        c5.write("Goto:")

    with c6:

        def _format_for_select(idx):
            return items[idx] if display_item_names else idx

        selected_value = st.selectbox(
            "goto_item_number",
            range(item_count),
            format_func=_format_for_select,
            index=st.session_state[item_num_var],
            label_visibility="collapsed",
            key=f"ItemPaginator:{title}#goto_item_number_select",
        )
        if selected_value != st.session_state[item_num_var]:
            set_item_index(selected_value)
            st.experimental_rerun()

    def increment_item_index():
        st.session_state[item_num_var] = min(item_count - 1, st.session_state[item_num_var] + 1)

    c7.button(
        "Next",
        on_click=increment_item_index,
        key=f"ItemPaginator:{title}#Next_btn",
        use_container_width=True,
    )

    if enable_keypress_nav:
        enable_keypress_navigation()

    item_handler_fn(st.session_state[item_num_var])


def reset_paginator(title, st=None):
    if not st:
        import streamlit as st
    item_num_var = f"{title}#item_num"
    st.session_state[item_num_var] = 0


def date_id(now=None):
    now = now or datetime.utcnow()
    return now.strftime("%Y%m%d%H%M") + "".join(random.choices(ascii_lowercase, k=6))


def enable_keypress_navigation(prev_button="Prev", next_button="Next"):
    """Enables keypress navigation in Streamlit. Allows navigation using left and right arrow keys.

    You must have existing buttons to navigate back / forth, with text matching the supplied parameter values.

    https://github.com/streamlit/streamlit/issues/1291#issuecomment-1022408379
    """
    import streamlit.components.v1 as components

    components.html(
        f"""
    <script>
    const doc = window.parent.document;
    buttons = Array.from(doc.querySelectorAll('button[kind=secondary]'));
    window.parent.console.log(buttons);
    const left_button = buttons.find(el => el.innerText === "{prev_button}");
    window.parent.console.log(left_button);
    const right_button = buttons.find(el => el.innerText === "{next_button}");
    window.parent.console.log(right_button);
    doc.addEventListener('keydown', function(e) {{
        switch (e.keyCode) {{
            case 37: // (37 = left arrow)
                left_button.click();
                break;
            case 39: // (39 = right arrow)
                right_button.click();
                break;
        }}
    }});
    </script>
    """,
        height=0,
        width=0,
    )


def check_or_x(value: bool) -> str:
    return "✅" if value else "❌"


def load_session(session_dir: Union[Path, str]):
    if isinstance(session_dir, str):
        session_dir = Path(session_dir)
    query_session = st.experimental_get_query_params().get("s")
    if query_session:
        query_session = query_session[0]

        # these are used by the streamlit-authenticator
        preserve_keys = ["authentication_status", "name", "username", "logout", "init"]

        preserved = {key: st.session_state.get(key) for key in preserve_keys}

        if "session_id" in st.session_state and st.session_state.session_id != query_session:
            st.session_state.clear()
            for key, value in preserved.items():
                st.session_state[key] = value

    if "session_id" not in st.session_state:
        if query_session:
            path = session_dir / (query_session + ".json")
            try:
                loaded_session_data = json.loads(path.read_text())
            except:
                pass
            else:
                for k, v in loaded_session_data.items():
                    if not k.startswith("FormSubmitter") and not k.startswith("ItemPaginator"):
                        st.session_state[k] = v
                assert st.session_state["session_id"] == query_session


def save_session(session_dir: Union[Path, str], set_query_param: bool = True):
    if set_query_param:
        st.experimental_set_query_params(s=st.session_state.session_id)

    if isinstance(session_dir, str):
        session_dir = Path(session_dir)
    session_dir.mkdir(parents=True, exist_ok=True)
    path = session_dir / (st.session_state.session_id + ".json")
    path.write_text(json.dumps(st.session_state.to_dict()))
