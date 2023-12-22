from twttr import shorten

# testing lower case vowels
def test_shorten_lower():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Plates") == "Plts"
    assert shorten("bing") == "bng"

# testing upper case vowels
def test_shorten_upper():
    assert shorten("EASports") == "Sprts"
    assert shorten("Animal") == "nml"

# testing numbers omitted
def test_shorten_number():
    assert shorten("ronaldo7") == "rnld7"
    assert shorten("messi10") == "mss10"

# testing punctuations omitted
def test_shorten_punc():
    assert shorten("Lets GO!") == "Lts G!"
    assert shorten("Stop.") == "Stp."
