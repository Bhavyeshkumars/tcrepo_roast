import pytest
from collections import namedtuple

Properties = namedtuple("Properties", ["parameter", "expected"])

def get_test_properties():
    p1 = Properties("parameter1", "hello parameter 1")
    p2 = Properties("parameter2", "hello parameter 2")
    return [p1, p2]

@pytest.mark.parametrize("properties", get_test_properties())
def test_parameterized(properties, create_configuration):
    conf = create_configuration(test_name="", params=[properties.parameter])
    assert conf.var == properties.expected
