import my_mod


def test_my_func():
    test_val1, test_val2 = 2, 3
    expected = 6
    actual = my_mod.my_func(test_val1, test_val2)
    assert expected == actual
