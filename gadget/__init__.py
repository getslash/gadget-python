# -*- coding: utf-8 -*-
import json

import logbook
import munch

__author__ = 'Rotem Yaari'
__email__ = 'vmalloc@gmail.com'
__version__ = '0.1.0'

_MARKER = 'GDGT::'


_setups = []

class Setup(object):

    def __init__(self, level=logbook.DEBUG):
        super(Setup, self).__init__()
        self.level = level

    def __enter__(self):
        _setups.append(self)
        return self

    def __exit__(self, *_):
        popped = _setups.pop()
        assert popped is self


def log_operation(entity, operation_name, params):
    """Logs an operation done on an entity, possibly with other arguments
    """
    p = {'name': operation_name, 'on': entity}
    if params:
        p['params'] = params
    _log('OP', p)

def _log(code, params):
    if not _setups:
        return
    logbook.log(
        _setups[-1].level,
        '{}{}:{}', _MARKER, code, _LazyJSON(params))


class _LazyJSON(object):
    def __init__(self, what):
        self._what = what
        self._rendered = None

    def __repr__(self):
        if self._rendered is None:
            self._rendered = json.dumps(self._what)
        return self._rendered

    __str__ = __repr__


## Parsing
def parse_log_line(line):
    index = line.index(_MARKER)
    if index < 0:
        return None

    line = line[index + len(_MARKER):]
    linetype, params = line.split(':', 1)
    returned = munch.Munch(type=linetype, params=json.loads(params))
    if returned.type == 'OP':
        returned.entity = returned.params.get('on')
        returned.name = returned.params.get('name')
    return returned
