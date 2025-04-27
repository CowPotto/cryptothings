import os

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
        # Open the file in read mode ('r') with UTF-8 encoding
        # Use 'with' statement to ensure the file is automatically closed
        with open(filepath, 'r', encoding='utf-8') as f:
            # Iterate over each line in the file
            for line in f:
                # Strip leading/trailing whitespace (like newline characters)
                stripped_line = line.strip()
                # Optionally, check if the line is not empty after stripping
                if stripped_line:
                    lines_list.append(stripped_line)
        return lines_list
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None # Indicate that the file was not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return [] # Return empty list on other errors

# --- Example Usage ---
if __name__ == "__main__":
    # Replace with the actual path if the script is not in the same directory
    # as the file, or if running in an environment where the path is different.
    file_to_read = "cheese_list.txt"

    print(f"Attempting to read: {file_to_read}")

    # Check if the file exists before attempting to read
    if os.path.exists(file_to_read):
        cheese_data = read_list_file(file_to_read)

        if cheese_data is not None:
            print(f"\nSuccessfully read {len(cheese_data)} lines.")
            # Print the first 10 items as a sample
            print("\nFirst 10 cheeses:")
            for i, cheese in enumerate(cheese_data[:10]):
                print(f"{i+1}. {cheese}")

            # Print the last 5 items as a sample
            print("\nLast 5 cheeses:")
            for i, cheese in enumerate(cheese_data[-5:]):
                 print(f"{len(cheese_data) - 5 + i + 1}. {cheese}")
        # The case where read_list_file returned [] due to an error other than FileNotFoundError
        elif cheese_data == []:
             print("File read, but might be empty or an error occurred during processing.")
    else:
        print(f"\nError: The file '{file_to_read}' does not exist in the current directory.")
        print("Please ensure the file path is correct.")

