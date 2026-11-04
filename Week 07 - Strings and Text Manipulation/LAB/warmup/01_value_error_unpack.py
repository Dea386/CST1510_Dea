# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, subkey, value = piece.split("=")
print(key, value)

# value error as there are more than 2 values.