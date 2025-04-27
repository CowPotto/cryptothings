import os

# Function to calculate the sum of ASCII values for characters in a string
def ascci_trans(text):
    """
    Calculates the sum of ASCII values for characters in a string.

    Args:
        text (str): The input string.

    Returns:
        int: The sum of ASCII values, or None if an error occurs.
    """
    result = 0
    try:
        # Ensure input is treated as a string
        text_str = str(text)
        # Iterate through each character in the string representation
        for char in text_str:
            # Get the ASCII value of the character
            ascii_val = ord(char)
            # Add it to the running total
            result += ascii_val
        return result
    except TypeError:
        # Handle cases where input might not be easily convertible
        print(f"Error: Could not process input '{text}'. It might not be convertible to string or contain non-character elements.")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred for input '{text}': {e}")
        return None

# Function to read a text file line by line
def read_list_file(filepath):
    """
    Reads a text file line by line and returns a list of strings.

    Args:
        filepath (str): The path to the text file.

    Returns:
        list: A list of strings, where each string is a line from the file
              with leading/trailing whitespace removed. Returns an empty list
              if the file cannot be read or is empty.
              Returns None if the file is not found.
    """
    lines_list = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    lines_list.append(stripped_line)
        return lines_list
    except FileNotFoundError:
        print(f"Error: Input file not found at '{filepath}'")
        return None # Indicate that the file was not found
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return [] # Return empty list on other errors

# --- Main execution ---
if __name__ == "__main__":
    input_filename = "cheese_list.txt"  # Input file containing the list
    output_filename = "result.txt"     # Output file for the results

    print(f"Reading input from: '{input_filename}'")
    print(f"Calculating sum of ASCII values for each item...")
    print(f"Output will be saved to '{output_filename}'")
    print("-" * 60)

    # Read the list from the input file
    input_list = read_list_file(input_filename)

    # Proceed only if the file was read successfully and is not empty
    if input_list is None:
        print("Processing stopped because the input file was not found.")
    elif not input_list:
         print("Processing stopped because the input file is empty or could not be read properly.")
    else:
        try:
            # Open the output file in write mode ('w')
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                # Loop through each item (cheese name) in the list
                for item_str in input_list:
                    # Get the sum of ASCII values from the function
                    ascii_sum = ascci_trans(item_str)

                    # Check if the function returned a valid sum
                    if ascii_sum is not None:
                        # Format the output string to contain only the sum and a newline
                        output_line = f"{ascii_sum}\n"
                        # Write the formatted line (just the number) to the file
                        outfile.write(output_line)
                    else:
                        # Log error for specific item if calculation failed
                        # Write an indicator like 'ERROR' or keep it blank
                        error_line = f"ERROR processing: '{item_str}'\n" # Indicate error in output file
                        outfile.write(error_line)

            print("-" * 60)
            print(f"\nCalculation complete. Results saved to '{output_filename}'.")
            print(f"Processed {len(input_list)} items.")

        except IOError as e:
            print(f"\nError: Could not write to file '{output_filename}'. {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred during file writing: {e}")

