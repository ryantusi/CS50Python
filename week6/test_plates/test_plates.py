from plates import is_valid

# testing true case min length in letter
def test_min_char():
    assert is_valid("CS") == True

# testing true case mmax length in letter
def test_max_char():
    assert is_valid("RYANAT") == True

# testing true case min length in number
def test_min_num():
    assert is_valid("CS50") == True

# testing true case max length in number
def test_max_num():
    assert is_valid("CS2023") == True

# testing false cases
def test_fail():
    assert is_valid("C") == False
    assert is_valid("50CS") == False
    assert is_valid("10") == False
    assert is_valid("CS50PY") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS05") == False
    assert is_valid("CS502023") == False
