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


def is_zero(input_data, start_pos=50):
    """
    Processes the list of (direction, steps) instructions starting from start_pos.
    Returns the number of times the dial points at 0.
    """
    pos = start_pos
    zero_count = 0

    for direction, steps in input_data:
        if direction == "L":
            pos = (pos - steps) % 100
        elif direction == "R":
            pos = (pos + steps) % 100

        if pos == 0:
            zero_count += 1

    return zero_count


def pass_zero(input_data, start_pos=50):
    """
    Processes the list of (direction, steps) instructions starting from start_pos.
    Returns the number of times the dial rotates past 0.
    """
    pos = start_pos
    total = 0

    for direction, steps in input_data:
        for _ in range(steps):
            if direction == "L":
                pos = (pos - 1) % 100
            elif direction == "R":
                pos = (pos + 1) % 100
            else:
                raise ValueError("Direction must be 'L' or 'R'")

            if pos == 0:
                total += 1

    return total


if __name__ == "__main__":
    data = load_instructions("day01_input.txt")
    print("Instructions:", data)

    lands = is_zero(data, start_pos=50)
    print("Part 1 (land on 0):", lands)

    passes = pass_zero(data, start_pos=50)
    print("Part 2 (pass over 0):", passes)
