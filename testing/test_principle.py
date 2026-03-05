import sys 
sys.path.append("../src")

#TODO make it with 'pip insfall -c'
#in project root_dir after setup.py defind

from math_demo import (
	add,
	add_with_bug,
	calculate_tax
)
def test_addition():
    assert 2 + 2 == 4
    print("test ADDIOTION PASSED")

def test_addication_with_bug():
	assert add_with_bug(2, 2) == 4
	assert add_with_bug(0, 0) == 0
	print("test BUGGED ADDICATION PASSED")
	assert add_with_bug(7, 6) == 13
def test_addication_dublicate():
	assert add(6, 7) == 6 + 7
	print("test DUBLICATE ADDICATIN PASSED")

def test_addication_overkill():
	for i in range(0, 2 ** 32):
		for j in range(0, 2 ** 32):
			assert add(i, j) == i + j
			assert add(-i, j) == i + j
			assert add(-i, -j) == i + j
			assert add(i, -j) == i + j
def test_addication_clusters():
	assert add(7, 6) == 13
	assert add(0, 6) == 6
	assert add(7, 6) == 7
	assert add(10, -11) == -1
	print("test CLUSTERS ADDICATION PASSED")

def test_tax_calculator():
	assert calculate_tax(1000) == 150
	assert calculate_tax(100) == 15
	assert calculate_tax(10) == 1.5
	assert calculate_tax(1) == 0.15
	print("test TAX CALCULATOR PASSED")

def test_negative_income():
	try:
		calculate_tax(-100)
		print("test NEGATIVE INCOME FAILED")
	except ValueError as e:
		print("test NEGATIVE INCOME PASSED")
if __name__ == "__main__":
	test_addition()
	test_addication_with_bug()
	#test_addication_dublicate()
	#test_addication_overkill()
	#test_addication_clusters()
	test_tax_calculator()
