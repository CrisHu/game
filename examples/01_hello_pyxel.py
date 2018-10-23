import pyxel
import datetime

_dict = {
    '.1': 'c1', '.2': 'd1', '.3': 'e1', '.4': 'f1', '.5': 'g1', '.6': 'a1', '.7': 'b1',
    '.1#': 'c#1', '.2#': 'd#1', '.4#': 'f#1', '.5#': 'g#1', '.6#': 'a#1',
    '1': 'c2', '2': 'd2', '3': 'e2', '4': 'f2', '5': 'g2', '6': 'a2', '7': 'b2',
    '1#': 'c#2', '2#': 'd#2', '4#': 'f#2', '5#': 'g#2', '6#': 'a#1',
}
_note = [('.6', '.7'), '1', ('.7',), '1', '3', '.7']


def foo(note):
    a = ''
    b = ''
    for i in note:
        if isinstance(i, str) or len(i) <= 1:
            if isinstance(i, tuple):
                a += '-'
                b += _dict[i[0]] + '-'
                continue
            else:
                a += _dict[i] + '-'
                b += '----'
                continue
        a += '-'
        for j in i:
            b += _dict[j]
    return a, b


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        self.img_x = 0
        self.img_y = 0
        pyxel.image(0).load(self.img_x, self.img_y, "assets/pyxel_logo_38x16.png")

        # bgm
        a = "d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3c3 d3e3f3e3"
        c = "a1r e2r  a2r e2r  f1r c2r  a2r c2r  d1r a1r  a2r a1r  e1r b1r  a2r b2r "
        pyxel.sound(0).set(a, "p", "2", "f", 30)
        pyxel.sound(1).set(c, "t", "2", "n", 30)
        pyxel.play(0, 0, loop=True)
        pyxel.play(1, 1, loop=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):  # trigger
            pyxel.quit()


        if pyxel.btn(pyxel.KEY_W):  # trigger
            self.img_y -= 1
        if pyxel.btn(pyxel.KEY_A):  # trigger
            self.img_x -= 1
        if pyxel.btn(pyxel.KEY_S):  # trigger
            self.img_y += 1
        if pyxel.btn(pyxel.KEY_D):  # trigger
            self.img_x += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "Hello, {}".format(datetime.datetime(2018, 10, 20, 12, 0)),
                   (pyxel.frame_count/8) % 16)
        pyxel.blt(self.img_x, self.img_y, 0, 0, 0, 38, 16)


App()
