def find_longest_and_shortest(sentence: str):
    words = sentence.split()
    if not words:
        return None, None
    
    shortest = min(words, key=len)
    longest = max(words, key=len)
    
    return shortest, longest

# Example usage:
short, long_word = find_longest_and_shortest("Programming in Python is amazing")
print(f"Shortest: {short}, Longest: {long_word}")