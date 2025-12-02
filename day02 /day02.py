def load_ranges(filename: str):
    ranges = []
    with open(filename, "r") as f:
        content = f.read().strip()
        for part in content.split(","):
            if part:
                start, end = part.split("-")
                ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id_part1(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def is_invalid_id_part2(n: int) -> bool:
    s = str(n)
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            subsection = s[:i]
            if subsection * (length // i) == s:
                return True
    return False


def solve_part1(filename: str):
    ranges = load_ranges(filename)
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id_part1(n):
                total += n
    return total


def solve_part2(filename: str):
    ranges = load_ranges(filename)
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id_part2(n):
                total += n
    return total


if __name__ == "__main__":
    print("Part 1:", solve_part1("day02_input.txt"))
    print("Part 2:", solve_part2("day02_input.txt"))
