import pyxel
from pyxel.constants import AUDIO_MUSIC_COUNT
from pyxel.ui import ImageButton, NumberPicker

from .constants import EDITOR_IMAGE_X, EDITOR_IMAGE_Y
from .editor import Editor


class MusicEditor(Editor):
    def __init__(self, parent):
        super().__init__(parent)

        self._music_picker = NumberPicker(self, 45, 17, 0, AUDIO_MUSIC_COUNT - 1, 0)
        self._play_button = ImageButton(self, 190, 17, 3, 126, 16)
        self._stop_button = ImageButton(self, 200, 17, 3, 135, 16)
        self._loop_button = ImageButton(self, 210, 17, 3, 144, 16)

        self.add_event_handler("draw", self.__on_draw)

    def __on_draw(self):
        self.draw_frame(11, 16, 218, 9)
        pyxel.text(23, 18, "MUSIC", 6)

        for i in range(4):
            x = i * 59 + 11
            self.draw_frame(x, 30, 41, 143)
            pyxel.text(x + 15, 32, "CH{}".format(i), 6)

            pyxel.blt(
                12 + i * 59, 39, 3, EDITOR_IMAGE_X + 67, EDITOR_IMAGE_Y + 8, 39, 127
            )

        self.draw_not_implemented_message()
