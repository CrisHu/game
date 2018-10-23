import pyxel
from pyxel.ui import Widget

from .constants import (
    TOOL_BUCKET,
    TOOL_CIRC,
    TOOL_CIRCB,
    TOOL_PENCIL,
    TOOL_RECT,
    TOOL_RECTB,
    TOOL_SELECT,
)


class Editor(Widget):
    """
    Events:
        __on_undo(data)
        __on_redo(data)
    """

    def __init__(self, parent):
        super().__init__(parent, 0, 0, 0, 0, is_visible=False)

        self._edit_history_list = []
        self._edit_history_index = 0

    @property
    def help_message(self):
        return self.parent.help_message

    @help_message.setter
    def help_message(self, value):
        self.parent.help_message = value

    @property
    def can_undo(self):
        return self._edit_history_index > 0

    @property
    def can_redo(self):
        return self._edit_history_index < len(self._edit_history_list)

    def undo(self):
        if not self.can_undo:
            return

        self._edit_history_index -= 1
        self.call_event_handler(
            "undo", self._edit_history_list[self._edit_history_index]
        )
        self.parent.edit_count -= 1

    def redo(self):
        if not self.can_redo:
            return

        self.call_event_handler(
            "redo", self._edit_history_list[self._edit_history_index]
        )
        self._edit_history_index += 1
        self.parent.edit_count += 1

    def add_edit_history(self, data):
        self._edit_history_list = self._edit_history_list[: self._edit_history_index]
        self._edit_history_list.append(data)
        self._edit_history_index += 1
        self.parent.edit_count += 1

    def add_number_picker_help(self, number_picker):
        number_picker.dec_button.add_event_handler(
            "mouse_hover", self.__number_picker_on_mouse_hover
        )
        number_picker.inc_button.add_event_handler(
            "mouse_hover", self.__number_picker_on_mouse_hover
        )

    def __number_picker_on_mouse_hover(self, x, y):
        self.help_message = "x10:SHIFT+CLICK"

    def check_tool_button_shortcuts(self):
        if pyxel.btn(pyxel.KEY_CONTROL):
            return

        if pyxel.btnp(pyxel.KEY_S):
            self._tool_button.value = TOOL_SELECT
        elif pyxel.btnp(pyxel.KEY_P):
            self._tool_button.value = TOOL_PENCIL
        elif pyxel.btnp(pyxel.KEY_R):
            self._tool_button.value = (
                TOOL_RECT if pyxel.btn(pyxel.KEY_SHIFT) else TOOL_RECTB
            )
        elif pyxel.btnp(pyxel.KEY_C):
            self._tool_button.value = (
                TOOL_CIRC if pyxel.btn(pyxel.KEY_SHIFT) else TOOL_CIRCB
            )
        elif pyxel.btnp(pyxel.KEY_B):
            self._tool_button.value = TOOL_BUCKET

    def add_tool_button_help(self, tool_button):
        tool_button.add_event_handler("mouse_hover", self.__tool_button_on_mouse_hover)

    def __tool_button_on_mouse_hover(self, x, y):
        value = self._tool_button.check_value(x, y)

        if value == TOOL_SELECT:
            s = "SELECT:S"
        elif value == TOOL_PENCIL:
            s = "PENCIL:P"
        elif value == TOOL_RECTB:
            s = "RECTANGLE:R"
        elif value == TOOL_RECT:
            s = "FILLED-RECT:SHIFT+R"
        elif value == TOOL_CIRCB:
            s = "CIRCLE:C"
        elif value == TOOL_CIRC:
            s = "FILLED-CIRC:SHIFT+C"
        elif value == TOOL_BUCKET:
            s = "BUCKET:B"
        else:
            s = ""

        self.help_message = s

    def draw_not_implemented_message(self):
        pyxel.rect(78, 83, 163, 97, 11)
        pyxel.rectb(78, 83, 163, 97, 1)
        pyxel.text(84, 88, "NOT IMPLEMENTED YET", 1)
