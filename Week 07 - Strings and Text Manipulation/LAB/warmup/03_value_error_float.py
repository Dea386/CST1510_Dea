# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    try:
        print(key, str(value))
    except ValueError:
        print(f"Invalid float for {key}: {value}")

#value error as the string is not a float meaning it cannot be converted to a float.