def more_than_five(lst):
	new_lst = []
	for number in lst:
		if abs(number) > 5:
			new_lst.append(number)
	return new_lst
print(more_than_five([-11, 4, -2, 90, 400, 0, -5]))
print(more_than_five([-2, 2, 3, 4, 0, -1]))
print(more_than_five([70, -900, 41, 0]))