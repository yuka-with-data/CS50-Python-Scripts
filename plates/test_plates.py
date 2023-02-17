from plates import is_valid

def test_min_max():
    assert not is_valid("P")
    assert not is_valid("PYTHOOOOON")
    assert not is_valid("")
    assert is_valid("PY")

def test_start_with_alpha():
    assert is_valid("PY311")
    assert not is_valid("C50S")
    assert not is_valid("311PY")
    assert not is_valid("1234")
    assert is_valid("PYTHON")

def test_first_int():
    assert not is_valid("CS05")
    assert not is_valid("PY0311")
    assert is_valid("DATA50")
    assert is_valid("PY301")

def test_int_middle():
    assert not is_valid("CS50P")
    assert not is_valid("PY311T")
    assert is_valid("CS50")

def test_find_punct():
    assert not is_valid("PI3.14")
    assert not is_valid("PYTH!")
    assert not is_valid("CS,50")
    assert is_valid("DSMLAI")

def main():
    test_min_max()
    test_start_with_alpha()
    test_first_int()
    test_int_middle()
    test_find_punct()

if __name__ == "__main__":
    main()