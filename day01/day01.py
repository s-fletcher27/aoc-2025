def load_instructions(filename: str):
    """
    Reads the puzzle input file and returns a list of (direction, steps) tuples.
    Example: 'L50' -> ('L', 50)
    """
    instructions = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                direction = line[0]
                steps = int(line[1:])
                instructions.append((direction, steps))
    return instructions

if __name__ == "__main__":
    data = load_instructions("day01_input.txt")
    print(data)