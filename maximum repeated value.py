def sample(my_list):
    return max(set(my_list), key = my_list.count)
print(sample([2, 1, 2, 2, 2, 2, 1, 2, 1, 3]))