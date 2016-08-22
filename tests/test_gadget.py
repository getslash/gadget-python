import datetime

import logbook
import pytest

import gadget


def test_operation(parser, params):

    gadget.log_operation('someobj', 'myop', params)
    [op] = parser.parse()

    assert op.type == gadget.TYPE_CODES.OPERATION
    assert op.entities == ['someobj']
    assert op.name == 'myop'
    assert op.params['params'] == params
    assert isinstance(op.timestamp, datetime.datetime)


def test_state(parser, state):

    gadget.log_state('someobj', state)
    [op] = parser.parse()

    assert op.type == gadget.TYPE_CODES.STATE
    assert op.entity == 'someobj'
    assert op.state == state
    assert isinstance(op.timestamp, datetime.datetime)

def test_update(parser):

    update = {'x': 1, 'y': 2}

    gadget.log_update('someobj', update)
    [op] = parser.parse()

    assert op.type == gadget.TYPE_CODES.UPDATE
    assert op.entity == 'someobj'
    assert op.update == update
    assert isinstance(op.timestamp, datetime.datetime)


def test_unserializable_objects(parser):
    gadget.log_update('someobj', {'x': 1, 'obj': object()})
    [op] = parser.parse()
    assert op.update['obj'].startswith('<object object at 0x')


@pytest.fixture
def params():
    return {'somevalue1': 1, 'somevalue2': 'string'}


@pytest.fixture
def state():
    return {'attr1': 1, 'attr2': 'string'}


@pytest.yield_fixture
def parser():
    with logbook.TestHandler(level=logbook.TRACE) as h:
        yield Parser(h)


class Parser(object):

    def __init__(self, handler):
        self.handler = handler

    def parse(self):
        for record in self.handler.records:
            yield gadget.parse_log_line(record.message)
