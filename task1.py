try:
    # Open sample.txt in read mode
    with open('sample.txt', 'r') as f:
        # Print each line with line number
        for idx, line in enumerate(f, start=1):
            print(f"Line {idx} : {line.strip()}")

# Show error if file not found
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
