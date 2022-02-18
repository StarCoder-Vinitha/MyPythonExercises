def func(word):
    string=""
    for each in word:
        if each == " ":
            string +="."
        else:
            string +=each
    return string
print(func("p th on"))