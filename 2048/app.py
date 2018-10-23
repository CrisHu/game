# coding=utf-8

import pyxel
from block import Block


class App:
    def __init__(self):
        self.zx, self.zy = 44, 44
        self.border = 2
        self.block_count = 2
        self.table = []
        self.order_table = list(range(16))
        self.__one_step()

        def _pyxel_init():
            pyxel.init(160, 120, caption='Hello: ②ø†∞')
            pyxel.load('test_resource.pyxel')
            import sound
            pyxel.run(self.update, self.draw)

        _pyxel_init()

    def __one_step(self):
        while True:
            if self.block_count > len(self.table):
                self.table.append(Block(self))
            else:
                break

    def __calculate(self, direction):
        _table = {}
        if direction == pyxel.KEY_DOWN:
            for block in self.table:
                try:
                    _table[block.x].append(block)
                except:
                    _table[block.x] = [block]
            _table = {k: v for k, v in _table.items() if not v.sort(key=lambda x: x.y)}
            _nt = []
            for _, v in _table.items():
                _nv = []
                if len(v) == 1:
                    _nv = [Block(self, v[0].x, 3, v[0].num)]
                    _nt.extend(_nv)
                elif len(v) == 2:
                    v0, v1 = v[0], v[1]
                    if v0.num == v1.num:
                        _nv = [Block(self, v0.x, 3, v0.num * 2)]
                    else:
                        _nv = [Block(self, v1.x, 3, v1.num),
                               Block(self, v0.x, 2, v0.num)]
                    _nt.extend(_nv)
                elif len(v) == 3:
                    v0, v1, v2 = v[0], v[1], v[2]
                    if v2.num == v1.num:
                        _nv = [Block(self, v2.x, 3, v2.num * 2),
                               Block(self, v0.x, 2, v0.num)]
                    elif v1.num == v0.num:
                        _nv = [Block(self, v1.x, 2, v1.num * 2),
                               Block(self, v2.x, 3, v2.num)]
                    else:
                        _nv = [Block(self, v0.x, 1, v0.num),
                               Block(self, v1.x, 2, v1.num),
                               Block(self, v2.x, 3, v2.num)]
                    _nt.extend(_nv)
                else:
                    v0, v1, v2, v3 = v[0], v[1], v[2], v[3]
                    if v3.num == v2.num:
                        _nv = [Block(self, v3.x, 3, v3.num * 2)]
                        if v1.num == v0.num:
                            _nv.append(Block(self, v1.x, 2, v1.num * 2))
                        else:
                            _nv.extend([Block(self, v1.x, 2, v1.num),
                                        Block(self, v0.x, 1, v0.num)])
                    elif v2.num == v1.num:
                        _nv = [Block(self, v0.x, 1, v0.num),
                               Block(self, v2.x, 2, v2.num * 2),
                               Block(self, v3.x, 3, v3.num)]
                    elif v1.num == v0.num:
                        _nv = [Block(self, v1.x, 1, v1.num * 2),
                               Block(self, v2.x, 2, v2.num),
                               Block(self, v3.x, 3, v3.num)]
                    else:
                        _nv = [Block(self, v0.x, 0, v0.num),
                               Block(self, v1.x, 1, v1.num),
                               Block(self, v2.x, 2, v2.num),
                               Block(self, v3.x, 3, v3.num)]
                    _nt.extend(_nv)
            self.table = _nt


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.block_count += 2
            self.__one_step()

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.__calculate(pyxel.KEY_DOWN)
        if pyxel.btnp(pyxel.KEY_UP):
            self.__calculate(pyxel.KEY_UP)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.__calculate(pyxel.KEY_LEFT)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.__calculate(pyxel.KEY_RIGHT)


    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, 'Hello', (pyxel.frame_count/8) % 16)
        pyxel.blt(30, 30, 0, 14, 14, 81, 81)

        for block in self.table:
            pyxel.text(*block.render_params())
