import sys 
sys.path.append("../src")

#TODO make it with 'pip insfall -c'

from math_demo import add
def test_addition():
    assert 2 + 2 == 4
    print("test ADDIOTION PASSED")


if name == "__main__":
    test_addition()
