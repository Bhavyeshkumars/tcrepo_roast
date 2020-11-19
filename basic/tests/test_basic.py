import pytest

def test_basic(create_configuration):
    conf = create_configuration()
    assert conf.var == "hello world"
