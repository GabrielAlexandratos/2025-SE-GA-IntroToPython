def calculate(x, y, z):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z


if __name__ == "__main__":
    user_input = input("Write equation here: ")
    x, y, z = user_input.split(" ")
    print(calculate(float(x), y, float(z)))
