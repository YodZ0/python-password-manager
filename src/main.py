import ctypes
import pyperclip
import dearpygui.dearpygui as dpg

from config import settings

from utils.database import DBHandler
from utils.pass_generator import get_charset, password_generator


db_handler = DBHandler()
db_handler.create_data_table()

pos_center = [settings.window.width // 2 - 200, settings.window.height // 2 - 190]
input_width = settings.window.width // 2


def add_new(sender, data, user_data: dict):
    user_data.pop("id")
    db_handler.insert_row(**user_data)


def fetch_data() -> list[dict[str, int | str]]:
    data = db_handler.select_all()
    return data


def copy_to_clipboard(sender, data, user_data):
    value = user_data.get("password")
    pyperclip.copy(value)

    # Set row unselected
    dpg.set_value(sender, False)


def update_table():
    row_ids = dpg.get_item_children("SelectRows", slot=1)
    if row_ids:
        for row_id in row_ids:
            dpg.delete_item(row_id)

    table_data = fetch_data()
    for row in table_data:
        with dpg.table_row(parent="SelectRows"):
            for column in ["id", "source", "login", "password"]:
                value = row.get(column)
                dpg.add_selectable(
                    label=value,
                    span_columns=True,
                    user_data=row,
                    callback=copy_to_clipboard,
                )


def _clear_form(inputs: tuple[int]):
    for item in inputs:
        dpg.set_value(item, value="")


def submit_form(sender, data, user_data):
    source_value, login_value, password_value = user_data

    source = dpg.get_value(source_value)
    login = dpg.get_value(login_value)
    password = dpg.get_value(password_value)

    new_data = {
        "source": source.strip(),
        "login": login.strip(),
        "password": password.strip(),
    }
    db_handler.insert_row(**new_data)

    _clear_form(user_data)
    update_table()


def generate_password(sender, data, user_data):
    nums_val, chars_val, capitals_val, specific_val, length_val = user_data

    nums: bool = dpg.get_value(nums_val)
    chars: bool = dpg.get_value(chars_val)
    capitals: bool = dpg.get_value(capitals_val)
    specific: bool = dpg.get_value(specific_val)
    length: int = dpg.get_value(length_val)

    charset = get_charset(nums, chars, capitals, specific)
    new_password = password_generator(length, charset)
    dpg.set_value("generated_password_field", value=new_password)


dpg.create_context()

with dpg.font_registry():
    regular = dpg.add_font(
        file=settings.fonts.regular,
        size=30,
    )
    italic = dpg.add_font(
        file=settings.fonts.italic,
        size=30,
    )
    bold = dpg.add_font(
        file=settings.fonts.bold,
        size=30,
    )

with dpg.window(
    no_collapse=True,
    no_resize=True,
    no_close=True,
    no_title_bar=True,
    tag="main",
):
    with dpg.tab_bar(tag="TabBar"):
        # TABLE WITH DATA
        with dpg.tab(label="Passwords"):
            table_tab_title = dpg.add_text("Table with your passwords")
            table_tab_descr = dpg.add_text("Click on a row to copy password...")
            dpg.bind_item_font(table_tab_title, bold)
            dpg.bind_item_font(table_tab_descr, italic)

            dpg.add_spacer(height=10)
            with dpg.table(
                tag="SelectRows",
                header_row=True,
                row_background=True,
                borders_outerH=True,
                borders_innerV=True,
            ):
                dpg.add_table_column(label="ID", width_fixed=True)
                dpg.add_table_column(label="Source")
                dpg.add_table_column(label="Login")
                dpg.add_table_column(label="Password")
            update_table()

        # TAB CREATE NEW
        with dpg.tab(label="Create"):
            with dpg.group(pos=pos_center):
                form_title = dpg.add_text("Fill creation form:")
                dpg.bind_item_font(form_title, bold)

                form_source_label = dpg.add_text("Source")
                source_input = dpg.add_input_text(
                    hint="google.com",
                    width=input_width,
                )

                form_login_label = dpg.add_text("Login")
                login_input = dpg.add_input_text(
                    hint="example@example.com",
                    width=input_width,
                )

                form_password_label = dpg.add_text("Password")
                password_input = dpg.add_input_text(
                    password=False,
                    hint="Enter your password",
                    width=input_width,
                )

                form_inputs = [source_input, login_input, password_input]

                dpg.add_spacer(height=20)
                form_btn = dpg.add_button(
                    label="Create",
                    width=100,
                    user_data=form_inputs,
                    callback=submit_form,
                )

        # TAB GENERATE PASSWORD
        with dpg.tab(label="Generate"):
            with dpg.group(pos=pos_center):
                gen_tab_title = dpg.add_text("Generate random password")
                dpg.bind_item_font(gen_tab_title, bold)
                dpg.add_spacer(height=10)

                new_pass_field = dpg.add_input_text(
                    hint="Generate me!",
                    width=input_width,
                    readonly=True,
                    tag="generated_password_field",
                )
                dpg.add_spacer(height=20)

                with dpg.group(horizontal=True):
                    cb_nums = dpg.add_checkbox(label="0-9")
                    dpg.add_spacer(width=15)

                    cb_chars = dpg.add_checkbox(
                        label="a-z",
                        default_value=True,
                    )
                    dpg.add_spacer(width=15)

                    cb_capitals = dpg.add_checkbox(
                        label="A-Z",
                        default_value=True,
                    )
                    dpg.add_spacer(width=15)

                    cb_specific = dpg.add_checkbox(label="@#%$")

                dpg.add_spacer(height=20)
                slider_len_title = dpg.add_text("Select password length:")
                slider_len = dpg.add_slider_int(
                    default_value=5,
                    min_value=5,
                    max_value=16,
                    width=input_width,
                )

                parameters = [cb_nums, cb_chars, cb_capitals, cb_specific, slider_len]

                dpg.add_spacer(height=20)
                gen_tab_btn = dpg.add_button(
                    label="Generate",
                    user_data=parameters,
                    callback=generate_password,
                )
                dpg.bind_item_font(gen_tab_btn, bold)


ctypes.windll.shcore.SetProcessDpiAwareness(2)  # to fix text blur

dpg.bind_font(regular)
dpg.create_viewport(
    title="Password manager",
    width=settings.window.width,
    height=settings.window.height,
)

dpg.set_primary_window(window="main", value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
