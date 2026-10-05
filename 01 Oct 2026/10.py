def find_substring_occurrences(main_str: str, sub_str: str) -> list[int]:
    indices = []
    start = 0
    while True:
        idx = main_str.find(sub_str, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1  # Move past the current match
    return indices

# Example usage:
print(find_substring_occurrences("abababab", "ab"))  # Output: [0, 2, 4, 6]