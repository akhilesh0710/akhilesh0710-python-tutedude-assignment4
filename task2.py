# Prompt the user to enter text to write to the file
user_input = input("Enter text to write to the file: ")

# Open 'output.txt' in write mode and write the user's input
with open('output.txt', 'w') as f:
    f.write(user_input)

print('Data successfully written to output.txt.')

# Prompt the user to enter additional text to append to the file
user_append = input("Enter additional text to append: ")

# Open 'output.txt' in append mode and write the additional input on a new line
with open('output.txt', 'a') as f:
    f.write('\n' + user_append)

print('Data successfully appended.')

# Open 'output.txt' in read mode and display its final content
with open('output.txt', 'r') as f:
    content = f.read()
    print("Final content of output.txt:")
    print(content)