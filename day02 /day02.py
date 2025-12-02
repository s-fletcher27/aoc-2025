def load_ranges(filename: str):
    ranges = []
    with open(filename, "r") as f:
        content = f.read().strip()
        for part in content.split(","):
            if part:
                start, end = part.split("-")
                ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def solve_day2(filename: str):
    ranges = load_ranges(filename)
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total


if __name__ == "__main__":
    print("Answer:", solve_day2("day02_input.txt"))
