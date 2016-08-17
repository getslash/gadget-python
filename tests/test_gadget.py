import logbook

import gadget
import pytest


def test_operation(parser, params):

    gadget.log_operation('someobj', 'myop', params)
    [op] = parser.parse()

    assert op.type == 'OP'
    assert op.entity == 'someobj'
    assert op.name == 'myop'
    assert op.params['params'] == params


@pytest.fixture
def params():
    return {'somevalue1': 1, 'somevalue2': 'string'}


@pytest.yield_fixture
def parser(setup):
    with logbook.TestHandler(level=logbook.TRACE) as h:
        yield Parser(h)


@pytest.yield_fixture
def setup():
    with gadget.Setup() as s:
        yield s


class Parser(object):

    def __init__(self, handler):
        self.handler = handler

    def parse(self):
        for record in self.handler.records:
            yield gadget.parse_log_line(record.message)
