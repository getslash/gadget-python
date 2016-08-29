import pytest
import gadget

@pytest.mark.parametrize('invalid_line', [
    'beginningGDG::',
    'beginning::end',
    'nothing',
])
def test_parse_invalid_line(invalid_line):
    assert gadget.parse_log_line(invalid_line) is None
