"""Print the Collatz sequence beginning at 27 and its transition count."""


def collatz_sequence(start: int) -> list[int]:
    """Return the Collatz sequence from *start* through the terminal 1."""
    if start < 1:
        raise ValueError("start must be a positive integer")

    sequence = [start]
    while sequence[-1] != 1:
        current = sequence[-1]
        sequence.append(current // 2 if current % 2 == 0 else 3 * current + 1)
    return sequence


def main() -> None:
    sequence = collatz_sequence(27)
    print(" ".join(map(str, sequence)))
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
