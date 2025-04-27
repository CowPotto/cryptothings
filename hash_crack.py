import base64

# The input string provided by the user
encoded_string_outer = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg=="

try:
    # First decode: Base64
    decoded_bytes_outer = base64.b64decode(encoded_string_outer)

    # The result looks like a Python byte string representation: b'...'
    # including the b', the quotes, and a newline \n
    decoded_string_outer = decoded_bytes_outer.decode('utf-8')

    print(f"First decoding (Base64): {decoded_bytes_outer}")
    print(
        f"Interpreted as string: {repr(decoded_string_outer)}")  # Show the literal string including quotes and newline

    # Extract the inner Base64 string by removing the b'...' representation
    # It looks like it starts after b' and ends before '\n'
    # Find the start and end indices carefully
    start_index = decoded_string_outer.find("'") + 1
    end_index = decoded_string_outer.rfind("'")

    if start_index > 0 and end_index > start_index and decoded_string_outer.startswith("b'"):
        encoded_string_inner = decoded_string_outer[start_index:end_index]
        print(f"\nExtracted inner string: {encoded_string_inner}")

        # Second decode: The inner string also looks like Base64
        decoded_bytes_inner = base64.b64decode(encoded_string_inner)
        final_result = decoded_bytes_inner.decode('utf-8')

        print(f"\nSecond decoding (Base64): {decoded_bytes_inner}")
        print(f"\nFinal Decoded Result: {final_result}")
    else:
        print("\nCould not extract the inner Base64 string from the first decoding.")
        print("The first decoding result might not be in the expected b'...' format.")
        # As a fallback, let's try decoding the original string directly if the b'...' parsing fails
        try:
            decoded_bytes_direct = base64.b64decode(encoded_string_outer)
            final_result_direct = decoded_bytes_direct.decode('utf-8')
            print(f"\nAttempting direct decoding of original string: {final_result_direct}")
        except Exception as direct_e:
            print(f"\nDirect decoding also failed: {direct_e}")


except base64.binascii.Error as e:
    print(f"Error decoding Base64: {e}")
    print("The input string might not be valid Base64.")
except UnicodeDecodeError as e:
    print(f"Error decoding bytes to string: {e}")
    print("The decoded bytes might not represent valid UTF-8 text.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

