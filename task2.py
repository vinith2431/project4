text = input("Enter some text: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")

more_text = input("Enter more text to append: ")
with open("output.txt", "a") as file:
    file.write(more_text + "\n")

with open("output.txt", "r") as file:
    print("Final content of output.txt:")
    for line in file:
        print(line.strip())
