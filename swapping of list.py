def sample(list_):
	for i in range(len(list_)):
		for k in range(i+1,len(list_)):	
			if list_[i] < list_[k]:
				list_[i],list_[k] = list_[k],list_[i]
			return list_
print(sample([1,2,3,4,5,7,6,90]))