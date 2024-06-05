def dis(price, discount):
	percent = discount / 100
	saving = price * percent
	answer = price - saving
	return round(answer, 2)