# -*- coding: utf-8 -*-
import json
import datetime
import time

import logbook
import munch

__author__ = 'Rotem Yaari'
__email__ = 'vmalloc@gmail.com'

_MARKER = 'GDGT::'

TYPE_CODES = munch.Munch(
    CREATE='CR',
    DELETE='DL',
    OPERATION='OP',
    STATE='ST',
    UPDATE='UP',
    ERROR='ER',
)

_ALL_TYPE_CODES = set(TYPE_CODES.values())


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

_setups = [Setup()]

def log_entity_creation(entity, params=None):
    """Logs an entity creation
    """
    p = {'entity': entity}
    if params:
        p['params'] = params
    _log(TYPE_CODES.CREATE, p)


def log_entity_deletion(entity, params=None):
    """Logs an entity creation
    """
    p = {'entity': entity}
    if params:
        p['params'] = params
    _log(TYPE_CODES.DELETE, p)


def log_operation(entities, operation_name, params=None):
    """Logs an operation done on an entity, possibly with other arguments
    """
    if isinstance(entities, (list, tuple)):
        entities = list(entities)
    else:
        entities = [entities]

    p = {'name': operation_name, 'on': entities}
    if params:
        p['params'] = params
    _log(TYPE_CODES.OPERATION, p)


def log_state(entity, state):
    """Logs a new state of an entity
    """
    p = {'on': entity, 'state': state}
    _log(TYPE_CODES.STATE, p)

def log_update(entity, update):
    """Logs an update done on an entity
    """
    p = {'on': entity, 'update': update}
    _log(TYPE_CODES.UPDATE, p)


def log_error(error, result):
    """Logs an error
    """
    p = {'error': error, 'result':result}
    _log(TYPE_CODES.ERROR, p)


def _log(code, params):
    if not _setups:
        return
    logbook.log(
        _setups[-1].level,
        '{}{}:{}:{}', _MARKER, code, time.time(), _LazyJSON(params))


class _LazyJSON(object):

    def __init__(self, what):
        self._what = what
        self._rendered = None

    def __repr__(self):
        if self._rendered is None:
            self._rendered = json.dumps(self._what, default=repr)
        return self._rendered

    __str__ = __repr__


# Parsing
def parse_log_line(line):
    try:
        index = line.index(_MARKER)
    except ValueError:
        return None

    line = line[index + len(_MARKER):]
    linetype, timestamp, params = line.split(':', 2)
    returned = munch.Munch(type=linetype, params=json.loads(params), timestamp=datetime.datetime.fromtimestamp(float(timestamp)))
    if returned.type == TYPE_CODES.OPERATION:
        returned.entities = returned.params.get('on')
        returned.name = returned.params.get('name')
    elif returned.type == TYPE_CODES.STATE:
        returned.entity = returned.params.get('on')
        returned.state = returned.params.get('state')
    elif returned.type == TYPE_CODES.UPDATE:
        returned.entity = returned.params.get('on')
        returned.update = returned.params.get('update')
    elif returned.type in [TYPE_CODES.CREATE, TYPE_CODES.DELETE]:
        returned.entity = returned.params.get('entity')
    return returned
