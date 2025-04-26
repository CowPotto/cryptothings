

"""
    A fucking rot13 machine
    input: a string
    output: a rotated string
"""

def rot13(text):
    result = []
    for char in text:
        ascii_val = ord(char) # turn char to ascii value. Ex: A -> 65
        print(ascii_val)

        if "A" <= char <= "Z":
            new_ascii = ascii_val + 13 # (65 - 65 + 13) % 26 + 65 = 78 -> which is N in ascii
            result.append(chr(new_ascii))

        elif "a" <= char <= 'z':
            new_ascii = ascii_val + 13
            result.append(chr(new_ascii))

        else:
            result.append(char)

    jointed_result = "".join(result)
    print(jointed_result)

rot13('a')


