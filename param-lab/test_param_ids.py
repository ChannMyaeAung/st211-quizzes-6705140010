import pytest 
from discount import apply_discount 

@pytest.mark.parametrize("price,percent,expected", [
    pytest.param(100, 0, 100, id="no discount"), # no discount
    pytest.param(100, 50, 50, id="half off"), # 50% discount
    pytest.param(100, 100, 0, id="free"), # free
])
def test_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected 