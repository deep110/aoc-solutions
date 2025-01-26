from os import path

PROJECT_ROOT = path.dirname(path.dirname(path.abspath(__file__)))
ALPHABET_6 = {
    ".##.\n#..#\n#..#\n####\n#..#\n#..#": "A",
    "###.\n#..#\n###.\n#..#\n#..#\n###.": "B",
    ".##.\n#..#\n#...\n#...\n#..#\n.##.": "C",
    "####\n#...\n###.\n#...\n#...\n####": "E",
    "####\n#...\n###.\n#...\n#...\n#...": "F",
    ".##.\n#..#\n#...\n#.##\n#..#\n.###": "G",
    "#..#\n#..#\n####\n#..#\n#..#\n#..#": "H",
    ".###\n..#.\n..#.\n..#.\n..#.\n.###": "I",
    "..##\n...#\n...#\n...#\n#..#\n.##.": "J",
    "#..#\n#.#.\n##..\n#.#.\n#.#.\n#..#": "K",
    "#...\n#...\n#...\n#...\n#...\n####": "L",
    ".##.\n#..#\n#..#\n#..#\n#..#\n.##.": "O",
    "###.\n#..#\n#..#\n###.\n#...\n#...": "P",
    "###.\n#..#\n#..#\n###.\n#.#.\n#..#": "R",
    ".###\n#...\n#...\n.##.\n...#\n###.": "S",
    "#..#\n#..#\n#..#\n#..#\n#..#\n.##.": "U",
    "#...\n#...\n.#.#\n..#.\n..#.\n..#.": "Y",
    "####\n...#\n..#.\n.#..\n#...\n####": "Z",
}


def read_input(year, day):
    """
    Read input file for a specific Advent of Code day

    Args:
        year (int): Year of the Advent of Code challenge
        day (int): Day number of the challenge

    Returns:
        str: Contents of the input file
    """
    input_path = path.join(PROJECT_ROOT, "input", str(year), f"day{day:02d}.txt")

    with open(input_path, "r") as f:
        return f.read()


def image_arr_to_str(array: list[list[str]]) -> str:
    # Validate input
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise ValueError("all rows should have the same number of columns")
    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    # Convert each letter
    indices = [slice(start, start + 4) for start in range(0, cols, 5)]
    result = [
        ALPHABET_6["\n".join("".join(row[index]) for row in array)] for index in indices
    ]

    return "".join(result)
