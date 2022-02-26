# Using Index Value
def sample(my_list):
	my_list[0] = 5
	return my_list
print(sample([1,2,3]))



# Using List Comprehension
my_list = ['1:', '2:', '3:']
my_list = [(item+' color') for item in my_list ]
print(my_list)



# Using Lambda Function
my_list = ['1:', '2:', '3:', '4:', '5:']
my_list = list(map(lambda item: (item +' color'), my_list))
print(my_list)