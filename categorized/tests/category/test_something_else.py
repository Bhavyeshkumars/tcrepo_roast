import pytest
from collections import namedtuple

Properties = namedtuple("Properties", ["parameter", "expected"])

def get_test_properties():
    p1 = Properties("parameter1", "hello parameter 3")
    p2 = Properties("parameter2", "hello parameter 4")
    return [p1, p2]

@pytest.mark.parametrize("properties", get_test_properties())
def test_something_else(properties, create_configuration):
    conf = create_configuration(params=[properties.parameter])
    assert conf.var == properties.expected
