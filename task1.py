try:
    with open('sample.txt', 'r') as f:
        for idx, line in enumerate(f, start=1):
            print(f"Line {idx} : {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")