def calculate_ndfl(income, investment=False, has_children=False):
	result = 0
	tiers = [(0, 0, 0.13),
		(2_400_000, 312_000, 0.15),
		(5_000_000, 702_000, 0.18),
		(20_000_000, 3_402_000, 0.20),
		(30_000_000, 9_402_000, 0.22)]
	for start, addition, taxrate in tiers:
		if incime > start:
			return (income - start) * taxrate + addition
	raise RuntimeError(f"error in tax calculation {income}")

