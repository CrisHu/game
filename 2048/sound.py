# coding=utf-8

import pyxel


# bgm
a = 'd3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3e3 d3e3d3c3 d3e3f3e3 r'
c = 'a1r e2r  a2r e2r  f1r c2r  a2r c2r  d1r a1r  a2r a1r  e1r b1r  a2r b2r  r'
pyxel.sound(0).set(a, 'p', '2', 'f', 30)
pyxel.sound(1).set(c, 't', '2', 'n', 30)
pyxel.play(0, 0, loop=True)
pyxel.play(1, 1, loop=True)

# add
pyxel.sound(2).set('g1a#1d#2b2', 's', '1', 's', 5)
# pyxel.play(2, 2)

# appear
pyxel.sound(3).set('e1a#1d#2', 's', '1', 's', 5)
# pyxel.play(3, 3)
