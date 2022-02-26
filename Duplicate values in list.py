# Without using of function

x = [1,2,1,3,2,4,3,5]
print(set([i for i in x if x.count(i)>1]))

# Using function

def sample(my_list):
	return set([i for i in x if x.count(i)>1])
print(sample([[1,2,1,3,2,4,3,5]]))