def faces():
    user_input = input()
    output = user_input.replace(":)", "🙂")
    output = output.replace(":(", "🙁")
    print(output)


if __name__ == "__main__":
    faces()
