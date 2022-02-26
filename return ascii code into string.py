## Ascii code of given sample

def my_asc(sample):
	return [ord(i) for i in "python"]
print(my_asc("python"))

## return ascii code into list of strings

def my_asc(sample):
	return [chr(ord(i)) for i in "python"]
print(my_asc("python"))