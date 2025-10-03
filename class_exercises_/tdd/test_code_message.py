import pytest
from class_exercises_.tdd.code_message import code_mssg

test_data1c = [("hello", 2, "jgnnq"),
              ("hello", 0, "hello"),
              ("cats", 1, "dbut"),
              ("HeLlo", 2, "jgnnq"),
              ("Howdy!", 2, "jqyfa!"),
              ]

test_data2c = [("zebra", 3, "cheud"),
              ("cat", -3, "zxq"),
              ("j4Ck13", 25, "i4bj13"),
              ]

test_data3c = [("hello", "hi"),
              ("hello", 3.5),
              ]

def test_normal():
    assert code_mssg("hello",2) == "jgnnq"


@pytest.mark.parametrize("message, shift, result", test_data1c)
def test_normal_chars(message, shift, result):
    assert code_mssg(message, shift) == result

@pytest.mark.parametrize("message, shift, result", test_data2c)
def test_boundaries(message, shift, result):
    assert code_mssg(message, shift) == result

@pytest.mark.parametrize("message, shift", test_data3c)
def test_erroneous(message, shift):
    assert code_mssg(message, shift) is TypeError
