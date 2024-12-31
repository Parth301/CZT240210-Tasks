def file_word_count(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        word_count = len(text.split())
        with open(output_file, 'w') as file:
            file.write(f"Word Count: {word_count}")
        print(f"Word count written to {output_file}")
    except FileNotFoundError:
        print("Input file not found.")

file_word_count('input.txt', 'output.txt')
