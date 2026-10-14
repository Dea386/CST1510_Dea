# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try: 
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("records.txt was not found.")



# error as they is no such file leading to the program having no output if there isnt such a file 