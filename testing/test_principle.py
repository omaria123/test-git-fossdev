import sys 
sys.path.append("../src")

#TODO make it with 'pip insfall -c'
#in project root_dir after setup.py defind

from math_demo import {
	add,
	add_with_bug
}
def test_addition():
    assert 2 + 2 == 4
    print("test ADDIOTION PASSED")

def test_addication_with_bug():
	assert add_with_bug(2, 2) == 4
	assert add_with_bug(0, 0) == 0
	print("test BUGGED ADDICATION PASSED")
	assert add_with_bug(7, 6) == 13
if name == "__main__":
    test_addition()
