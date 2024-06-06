import sys

script, encoding, error = sys.argv

# Reads lines from the language_file.
def main(language_file, encoding, errors):
    #reads a single line from the file.
    line = language_file.readline()

# If the line is not empty (if line:), it calls print_line to process and print the line.

    if line:
        print_line(line, encoding, errors)
# After processing, it recursively calls main to read the next line.
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    # Remove the white space.
    next_lang = line.strip()
    # Encode the stripped line in to bytes.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Decode the byte back in to the string.
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # Print the encoded bytes bytes and decoded string in a formatted manner.
    print(raw_bytes, "<===>", cooked_string)
# Open the file in readmode with utf-8 encoding.
languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)