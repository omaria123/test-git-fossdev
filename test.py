from script import sum, devide

def test_sum():
 a = 1
 b = 2
 result = 3
 assert sum(a, b) == result

def test_devide():
 a = 4
 b = 2
 result = 0.5
 assert devide(b, a) == result

if __name__ ==  "__main__":
 test_devide()
 test_sum()

