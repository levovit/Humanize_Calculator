import pytest
from Humanize_calculator import convert, fix


def setup_module():
    print("\nTests Started")


def teardown_module():
    print("\nTests Ended")


def test_space_1():
    s = "3+2"
    assert fix(s) == "three plus two"


def test_space_2():
    s = "3 + 2"
    assert fix(s) == "three plus two"


def test_space_3():
    s = " 3 + 2 "
    assert fix(s) == "three plus two"


def test_space_4():
    s = "3         +     2    "
    assert fix(s) == "three plus two"


def test_space_5():
    s = "3+2 2"
    assert fix(s) == "three plus twenty two"


def test_exception_1():
    s = ""
    assert fix(s) == "invalid input"


def test_exception_2():
    s = "2+*3"
    assert fix(s) == "invalid input"


def test_exception_3():
    s = "*3 +2"
    assert fix(s) == "invalid input"


def test_exception_4():
    s = "1 + 2 = x"
    assert fix(s) == "invalid input"


def test_exception_5():
    s = "2.5 + 3"
    assert fix(s) == "invalid input"


def test_exception_6():
    s = "22x2 + 23"
    assert fix(s) == "invalid input"


def test_exception_7():
    with pytest.raises(TypeError):
        convert(2+2)


def test_unary_operator_1():
    s = "2 ++ 2"
    assert fix(s) == "two plus two"


def test_unary_operator_2():
    s = "2+-2"
    assert fix(s) == "two plus minus two"


def test_big_number_1():
    s = "80"
    assert fix(s) == "eighty"


def test_big_number_2():
    s = "800"
    assert fix(s) == "eight hundred"


def test_big_number_3():
    s = "8 000"
    assert fix(s) == "eight thousand"


def test_big_number_4():
    s = "80 000"
    assert fix(s) == "eighty thousand"


def test_big_number_5():
    s = "800 000"
    assert fix(s) == "eight hundred thousand"


def test_big_number_6():
    s = "8 000 000"
    assert fix(s) == "eight million"


def test_big_number_7():
    s = "1222 222 + 1200 000 + 1 000 000"
    assert fix(s) == "one million two hundred twenty two thousand two hundred twenty" \
                     " two plus one million two hundred thousand plus one million"


def test_big_number_8():
    s = "-80 000 + -66 666 = +3033 + -72 = 10 - 5 * 207 - 643 / 800 + 30 + 3000 + 3200"
    assert fix(s) == "minus eighty thousand plus minus sixty six thousand six " \
                     "hundred sixty six equals three thousand thirty three plus" \
                     " minus seventy two equals ten minus five times two hundred" \
                     " seven minus six hundred forty three divided eight hundred" \
                     " plus thirty plus three thousand plus three thousand two hundred"


def test_big_number_9():
    s = "1 + 12 + 123 + 1234 + 12345 + 123456 + 1234567"
    assert fix(s) == "one plus twelve plus one hundred twenty three plus one " \
                     "thousand two hundred thirty four plus twelve thousand " \
                     "three hundred forty five plus one hundred twenty three " \
                     "thousand four hundred fifty six plus one million " \
                     "two hundred thirty four thousand five hundred sixty seven"


def convert_test_1():
    s = "123"
    assert convert(s) == "one hundred twenty three"


def convert_test_2():
    s = "0"
    assert convert(s) == "zero"
