def sum(a, b):
 return a + b

def devide(a, b):
 if b == 0:
  raise ValueError("Denominator could not be zero")
 if isinstance(a, str) or isinstance(b, str):
  raise ValueError("Could not devide strings")
 if isinstance(a, list) or isinstance(b, list):
  raise ValueError("Could not devide lists")
 return a / b

