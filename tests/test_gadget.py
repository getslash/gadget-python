import pytest

from gadget import Setup

def test_gadget(setup):
    pass

@pytest.yield_fixture
def setup():
    yield Setup()
