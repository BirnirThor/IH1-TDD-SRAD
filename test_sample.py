from sample import fizzbuzz

def test_return_the_input_num():
    assert fizzbuzz(16) == 16

def test1_return_buzz_if_div_by_5():
    assert fizzbuzz(5) == "Buzz"

def test2_return_buzz_if_div_by_5():
    assert fizzbuzz(-5) == "Buzz"

def test3_return_buzz_if_div_by_5():
    assert fizzbuzz(115) == "Buzz"
