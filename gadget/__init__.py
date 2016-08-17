# -*- coding: utf-8 -*-

__author__ = 'Rotem Yaari'
__email__ = 'vmalloc@gmail.com'
__version__ = '0.1.0'


_setups = []

class Setup(object):

    def __init__(self):
        super(Setup, self).__init__()

    def __enter__(self):
        _setups.append(self)
        return self

    def __exit__(self, *_):
        popped = _setups.pop()
        assert popped is self
