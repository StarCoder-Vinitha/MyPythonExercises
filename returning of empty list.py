def my_list(sample):
	for each in sample:
		if each == []:
			print(each)
		else:
			each.clear()
			print(each)
my_list([[1,2,3],[],[4,5],[],[2,3]])