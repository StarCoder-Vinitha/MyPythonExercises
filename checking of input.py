
def sample(input):
    if input.isalpha():
        return ('alphabet')
    elif input.isdigit():
        return ('integer')
    elif input.isalnum():
        return ('alphanumeric')
print(sample('python'))

