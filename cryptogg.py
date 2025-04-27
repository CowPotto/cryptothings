result = []

def rot():
    print("Enter the string: ")
    text = str(input())

    print("Which rot using: ")
    rot_mapping = int(input())

    #invert ascii to int then back to ascii
    for char in text:
        ascii_val = ord(char)

        if 'A' <= char <= 'Z':
            new_ascii_val = (ascii_val - ord('A') + rot_mapping) % 26 + ord('A')
            result.append(chr(new_ascii_val))
        elif 'a' <= char <= 'z':
            new_ascii_val = (ascii_val - ord('a') + rot_mapping) % 26 + ord('a')
            result.append(chr(new_ascii_val))
        else:
            result.append(char)

    join_value = "".join(result)
    print(join_value)



rot()





