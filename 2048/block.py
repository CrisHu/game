# coding=utf-8

import random


class Block(object):
    _width = 14

    def __init__(self, app, x=None, y=None, num=None):
        self.app = app
        order = random.sample(app.order_table, 1)[0]
        self.y = y if y is not None else int(order / 4)
        self.x = x if x is not None else order % 4
        self.num = num if num else random.sample([1, 2], 1)[0]
        app.order_table.remove(order)

    def __repr__(self):
        return 'Block<id:{0}, (x, y): <{1},{2}>, num: {3}>'.format(
            id(self), self.x, self.y, self.num
        )

    @property
    def exist(self):
        return self.x and self.y and self.num

    def render_params(self):
        return (
            self.app.zx + (self.x + 0.5) * self.app.border + (self.x - 0.5) * self._width,
            self.app.zy + (self.y + 0.5) * self.app.border + (self.y - 0.5) * self._width,
            str(self.num),
            5
        )