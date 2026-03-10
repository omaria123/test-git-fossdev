def calculate_ndfl(income):
	result = 0
	if income < 2400000:
		result = income * 0.13
	else:
		result = (income * 0.15 + (income - 2400000) * 0.15) 
	return result
