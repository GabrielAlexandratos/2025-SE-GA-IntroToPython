def convertCase(string):
    for char in string:
        if char.isupper():
            print(f"_{char.lower()}", end="")
        else:
            print(char, end="")


if __name__ == "__main__":
    convertCase("thisIsACamelCaseString")
