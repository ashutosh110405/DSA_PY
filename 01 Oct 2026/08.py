def print_patterns():
    print("--- Pattern 1: Number Pyramid ---")
    for i in range(1, 6):
        row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        print(" ".join(map(str, row)))

    print("\n--- Pattern 2: Alternating 0/1 Matrix ---")
    for i in range(5):
        row = [(i + j) % 2 for j in range(5)]
        print("".join(map(str, row)))

print_patterns()