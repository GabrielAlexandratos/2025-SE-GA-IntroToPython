# Example starter code
def text_to_decimal(message):
    return [ord(char) for char in message]


def decimal_to_text(decimal_values):
    return "".join(chr(value) for value in decimal_values)


if __name__ == "__main__":
    # Test with a secret message
    secret = text_to_decimal("Hello World!")
    print(secret)
    decoded = decimal_to_text(secret)
    print(decoded)
